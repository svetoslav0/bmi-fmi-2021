from ast import Try
import sys
import random
from sklearn.svm import SVR
from sklearn import tree
from sklearn import linear_model
from sklearn.preprocessing import *
from pymongo import MongoClient
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_validate
from sklearn.metrics import recall_score
from sklearn.model_selection import KFold
from sklearn.metrics import precision_recall_curve
from sklearn.metrics import cohen_kappa_score
from sklearn.metrics import classification_report
from sklearn.metrics.scorer import make_scorer
from matplotlib.ticker import MaxNLocator
import matplotlib.ticker as ticker
from splitting_methods import SplitMethod
from splitting_methods import Splitter
from ml_models_cancer import MachineLearningModelsScore
from ml_models_cancer import ML_Configuration
from ml_models_cancer import ML_MODELS_TYPES


class DataTransofrmer:
    def __init__(self, feature_type, spliter_type, n_split):
        self._feature_type = feature_type
        self._spliter_type = spliter_type
        self._n_split = n_split

    def get_data_from_driver(self, _driver):
        result = []
        if self._feature_type == "NPI":
            result = session.run("MATCH p=(s:Sample)-[m:MUTATION]->(h:HugoSymbol) " + " WHERE " +
                                 " s.OS_MONTHS <> $null AND toInt(s.OS_MONTHS) > 0" +
                                 " AND s.NPI <> $null " +
                                 " RETURN distinct s.OS_MONTHS AS months " +
                                 " ,s.NPI", living="Living", died="Died of Disease", null="null")
        else:
            for u in _driver.samples.aggregate([
    {
        "$match": {
            "OS_MONTHS": {"$exists": True,"$ne": "", "$ne": "null"},
            "TUMOR_STAGE": {"$exists": True,"$ne": "","$ne": "null"},
            "TUMOR_SIZE": {"$exists": True,"$ne": "", "$ne": "null"},
            "AGE_AT_DIAGNOSIS": {"$exists": True,"$ne": "", "$ne": "null"}
        }
    },
    {
        "$project": {
            "OS_MONTHS": 1,
            "FEATURE": {"$concat": [{"$toString": "$TUMOR_STAGE"},{"$toString": "$TUMOR_SIZE"},{"$toString": "$AGE_AT_DIAGNOSIS"}]}
        }
    }
]):
                result.append(u)
        x = []
        y = []
        for indx, rec in enumerate(result):
            try:
                float(rec["FEATURE"])
            except ValueError:
                continue

            x.append([rec["FEATURE"], rec["OS_MONTHS"]])
            y.append(rec["OS_MONTHS"])

        x = np.array(x)
        y = np.array(y)

        return Splitter(self._spliter_type).split(x, y, int(len(x)/100))


def main(_db):
    data_transformer = DataTransofrmer("TICF", SplitMethod.SHUFFLE_SPLIT, 100)
    values = data_transformer.get_data_from_driver(_db)
    x = values[0]
    y = values[1]
    x_test = values[2]
    y_test = values[3]
    chart_config = {ML_MODELS_TYPES.SVR_LINEAR: [
        'grey', '//', 'SVR_LINEAR'], ML_MODELS_TYPES.SVR_RBF: ['#3A3A3A', '', 'SVR_RBF'], ML_MODELS_TYPES.DTR: ['#8A8A8A', '', 'DTR'],
        ML_MODELS_TYPES.SVR_POLY: ['green', '', 'SVR_POLY'], ML_MODELS_TYPES.LASSO: ['#9A9A3A', '-', 'LASSO'],
        ML_MODELS_TYPES.KERNEL_RIDGE: ['#7A7A3A', '', 'KERNEL_RIDGE'], ML_MODELS_TYPES.MLP_REGRESSOR: ['#3A1A1A', '', 'MLP_REGRESSOR'],
        ML_MODELS_TYPES.K_NEIGHBORS_REGRESSOR: ['#4A4A4A', '', 'K_NEIGHBORS_REGRESSOR']}

    ml_models = MachineLearningModelsScore()
    scores = ml_models.get_models_score(x, y, x_test, y_test)
    show_score_chart(scores, chart_config)
    chart_config = {ML_MODELS_TYPES.SVR_LINEAR: ['SVR_LINEAR'], ML_MODELS_TYPES.SVR_RBF: ['SVR_RBF'],
                    ML_MODELS_TYPES.DTR: ['DTR'], ML_MODELS_TYPES.SVR_POLY: ['SVR_POLY'],
                    ML_MODELS_TYPES.LASSO: ['LASSO'], ML_MODELS_TYPES.KERNEL_RIDGE: ['KERNEL_RIDGE'],
                    ML_MODELS_TYPES.MLP_REGRESSOR: ['MLP_REGRESSOR'], ML_MODELS_TYPES.K_NEIGHBORS_REGRESSOR: ['K_NEIGHBORS_REGRESSOR']}
    predict_results = ml_models.predit(x_test)

    show_predict_chart(predict_results, y_test, chart_config,
                       'fit_test.svg')
    plt.show(block=True)


def show_predict_chart(array, y_test, config, file_name):
    y_test=np.array(y_test)
    figure_number=0
    fig=plt.figure()
    fig.subplots_adjust(hspace = 0.2, wspace = 0.3)

    for (key, value) in array.items():
        item=value
        figure_number=figure_number + 1
        _ax=fig.add_subplot(4, 2, figure_number)
        _ax.plot([y_test.min(), y_test.max()], [
                 y_test.min(), y_test.max()], 'k--', lw = 2)
        _ax.scatter(y_test, item, color = 'grey')
        _ax.set_title('\n ' + config[key][0])
        _ax.set_xlabel('Measured')
        _ax.set_ylabel('Predicted')

    fig.savefig(file_name, format = 'svg')


def show_score_chart(_scores, _config):
    ind=np.arange(5) * 1.9
    width=0.2
    rects={}
    fig=plt.figure()
    fig.subplots_adjust(hspace = 0.5, wspace = 0.3)
    types=[['train_r2', 'Trained R2', 'Success Rate', [_scores]],
             ['train_explained_variance', 'Trained Explained Variance',
                 'Success Rate', [_scores]],
             ['test_neg_mean_absolute_error',
                 'Neg Mean Absolute Error', 'Error Rate', [_scores]],
             ['test_neg_median_absolute_error', 'Neg Mean Median Absolute Error', 'Error Rate', [_scores]]]

    chart_number = 0
    for i, type in enumerate(types):
        for index, sourc in enumerate(type[3]):
            chart_number = chart_number + 1
            ax = fig.add_subplot(2, 2, chart_number)
            for indx, (k, v) in enumerate(sourc.items()):
                bar = ax.bar(ind + (indx * width), v[type[0]], width, color=_config[k][0], yerr=np.std(
                    v[type[0]], axis=0), hatch=_config[k][1])
                rects[_config[k][2]] = bar
            ax.set_ylabel(type[2])
            ax.set_title(type[1])
            ax.set_xticks(ind + width * 3 / 2)
            #ax.set_xticklabels(range(1, 5))
    fig.legend((bar for (name, bar) in rects.items()), (name for (
        name, bar) in rects.items()), ncol=len(rects), loc='lower center', borderaxespad=0.)
    fig.savefig('error_test1.svg', format='svg')


if __name__ == '__main__':
    client = MongoClient("mongodb://root:rootpassword@localhost:27017")
    _db = client.proteins

    main(_db)
