import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import KNNImputer
from sklearn.feature_selection import RFE
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.svm import SVR
from sklearn.model_selection import cross_validate
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split
import pickle

class MLPipeline:

    model = None
    filename = 'SVM_trained.pkl'
    features = ["yearstobirth", "vitalstatus", "daystodeath", "daystolastfollowup", "pathologicstage", "pathologyTstage"
        ,"pathologyNstage", "dateofinitialpathologicdiagnosis", "daystolastknownalive", "radiationtherapy",
        "histologicaltype", "numberoflymphnodes"]
    gle = LabelEncoder()

    def load_model(self):
        self.model = pickle.load(open(self.filename, 'rb'))

    def run_pipeline(self, input_data):
        new_model, _ = self.train_new_model(input_data)
        pickle.dump(new_model, open(self.filename, 'wb'))

    def predict(self, input_data):
        df = pd.DataFrame.from_dict([input_data])
        self.categorical_to_numerical(df)
        return self.model.predict(df)

    def train_new_model(self, input_data):
        preprocessed_df = self.preprocess_data(input_data)
        shrinked_df = preprocessed_df[self.features]
        x_train, x_test, y_train, y_test = self.split_data(preprocessed_df)
        regressor = SVR(kernel='linear')
        regressor.fit(x_train,y_train)
        score = regressor.score(x_test, y_test)
        yfit = regressor.predict(x_test)
        print("R-squared:", score)
        print("MSE:", mean_squared_error(y_test, yfit))
        return regressor, mean_squared_error(y_test, yfit)

    def preprocess_data(self, input_data):
         df = pd.DataFrame.from_dict(input_data)
         for i in ['_id', 'gender']:
             df.drop(i, axis='columns', inplace=True)
         self.categorical_to_numerical(df)
         df = self.fillNA(df)
         return df

    def feature_selection(self, df):
        y = df['daystodeath']
        modified_df = df.drop("daystodeath", axis='columns')
        x = modified_df.iloc[:, 0:15]
        lab = preprocessing.LabelEncoder()
        y_transformed = lab.fit_transform(y)

        rfe = RFE(estimator=RandomForestClassifier(), n_features_to_select=12)
        selector = rfe.fit(x, y_transformed)
        cols_idx = selector.get_support(indices=True)
        columns = []
        for i in cols_idx:
            columns.append(df.columns[i])

        return columns

    def categorical_to_numerical(self, df):
        categorical_columns = df.select_dtypes(include=['object']).columns

        for i in categorical_columns:
            df[i] = self.gle.fit_transform(df[i])


    def fillNA(self, df):
        imputer = KNNImputer(n_neighbors=5)
        return pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

    def split_data(self, df):
        y = df['daystodeath']
        modified_df = df.drop("daystodeath", axis='columns')
        x = modified_df.iloc[:, 0:len(modified_df.columns)]
        return train_test_split(x, y, test_size=0.1, random_state=42)