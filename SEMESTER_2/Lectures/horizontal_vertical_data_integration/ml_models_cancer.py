from enum import Enum
from sklearn.svm import SVR
from sklearn import tree
from sklearn import linear_model
from sklearn import preprocessing
from sklearn.kernel_ridge import KernelRidge
from sklearn.model_selection import cross_validate
from sklearn.neural_network import MLPRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.multioutput import RegressorChain
import numpy as np


class ML_MODELS_TYPES(Enum):
    SVR_LINEAR = 1
    SVR_RBF = 2
    SVR_POLY = 3
    DTR = 4
    LASSO = 5
    KERNEL_RIDGE = 6
    MLP_REGRESSOR = 7
    K_NEIGHBORS_REGRESSOR = 8


class NORMALIZATION_TYPE(Enum):
    STANDARD_SCALER = 1
    MIN_MAX_SCALER = 2
    MAX_ABS_SCALER = 3
    NORMALIZER = 4
    NONE = 5


class _BaseModel:
    def predict(self, _x):
        pass

    def fix(self, _x, _y):
        pass

    def cross_validate(self, _estimator, _X, _y=None, _groups=None,
                       _scoring=('r2', 'neg_mean_squared_error', 'explained_variance',
                                 'neg_mean_absolute_error', 'neg_median_absolute_error'),
                       _cv=5, _n_jobs=None, _verbose=0, _fit_params=None,
                       _pre_dispatch='2*n_jobs', _return_train_score="warn",
                       _return_estimator=False, _error_score='raise-deprecating'):
        """Parameters
    ----------
    estimator : estimator object implementing 'fit'
        The object to use to fit the data.

    X : array-like
        The data to fit. Can be for example a list, or an array.

    y : array-like, optional, default: None
        The target variable to try to predict in the case of
        supervised learning.

    groups : array-like, with shape (n_samples,), optional
        Group labels for the samples used while splitting the dataset into
        train/test set.

    scoring : string, callable, list/tuple, dict or None, default: None
        A single string (see :ref:`scoring_parameter`) or a callable
        (see :ref:`scoring`) to evaluate the predictions on the test set.

        For evaluating multiple metrics, either give a list of (unique) strings
        or a dict with names as keys and callables as values.

        NOTE that when using custom scorers, each scorer should return a single
        value. Metric functions returning a list/array of values can be wrapped
        into multiple scorers that return one value each.

        See :ref:`multimetric_grid_search` for an example.

        If None, the estimator's default scorer (if available) is used.

    cv : int, cross-validation generator or an iterable, optional
        Determines the cross-validation splitting strategy.
        Possible inputs for cv are:

        - None, to use the default 3-fold cross validation,
        - integer, to specify the number of folds in a `(Stratified)KFold`,
        - :term:`CV splitter`,
        - An iterable yielding (train, test) splits as arrays of indices.

        For integer/None inputs, if the estimator is a classifier and ``y`` is
        either binary or multiclass, :class:`StratifiedKFold` is used. In all
        other cases, :class:`KFold` is used.

        Refer :ref:`User Guide <cross_validation>` for the various
        cross-validation strategies that can be used here.

        .. versionchanged:: 0.20
            ``cv`` default value if None will change from 3-fold to 5-fold
            in v0.22.

    n_jobs : int or None, optional (default=None)
        The number of CPUs to use to do the computation.
        ``None`` means 1 unless in a :obj:`joblib.parallel_backend` context.
        ``-1`` means using all processors. See :term:`Glossary <n_jobs>`
        for more details.

    verbose : integer, optional
        The verbosity level.

    fit_params : dict, optional
        Parameters to pass to the fit method of the estimator.

    pre_dispatch : int, or string, optional
        Controls the number of jobs that get dispatched during parallel
        execution. Reducing this number can be useful to avoid an
        explosion of memory consumption when more jobs get dispatched
        than CPUs can process. This parameter can be:

            - None, in which case all the jobs are immediately
              created and spawned. Use this for lightweight and
              fast-running jobs, to avoid delays due to on-demand
              spawning of the jobs

            - An int, giving the exact number of total jobs that are
              spawned

            - A string, giving an expression as a function of n_jobs,
              as in '2*n_jobs'

    return_train_score : boolean, optional
        Whether to include train scores.

        Current default is ``'warn'``, which behaves as ``True`` in addition
        to raising a warning when a training score is looked up.
        That default will be changed to ``False`` in 0.21.
        Computing training scores is used to get insights on how different
        parameter settings impact the overfitting/underfitting trade-off.
        However computing the scores on the training set can be computationally
        expensive and is not strictly required to select the parameters that
        yield the best generalization performance.

    return_estimator : boolean, default False
        Whether to return the estimators fitted on each split.

    error_score : 'raise' | 'raise-deprecating' or numeric
        Value to assign to the score if an error occurs in estimator fitting.
        If set to 'raise', the error is raised.
        If set to 'raise-deprecating', a FutureWarning is printed before the
        error is raised.
        If a numeric value is given, FitFailedWarning is raised. This parameter
        does not affect the refit step, which will always raise the error.
        Default is 'raise-deprecating' but from version 0.22 it will change
        to np.nan.

    Returns
    -------
    scores : dict of float arrays of shape=(n_splits,)
        Array of scores of the estimator for each run of the cross validation.

        A dict of arrays containing the score/time arrays for each scorer is
        returned. The possible keys for this ``dict`` are:

            ``test_score``
                The score array for test scores on each cv split.
            ``train_score``
                The score array for train scores on each cv split.
                This is available only if ``return_train_score`` parameter
                is ``True``.
            ``fit_time``
                The time for fitting the estimator on the train
                set for each cv split.
            ``score_time``
                The time for scoring the estimator on the test set for each
                cv split. (Note time for scoring on the train set is not
                included even if ``return_train_score`` is set to ``True``
            ``estimator``
                The estimator objects for each cv split.
                This is available only if ``return_estimator`` parameter
                is set to ``True``.
            """

        return cross_validate(estimator=_estimator, X=_X, y=_y, groups=_groups, scoring=_scoring, cv=_cv, n_jobs=_n_jobs, verbose=_verbose,
                              fit_params=_fit_params, pre_dispatch=_pre_dispatch, return_train_score=_return_train_score, return_estimator=_return_estimator,
                              error_score=_error_score)


class ML_Configuration():
    '''
    Parameters
    ----------
    kernel : string, optional (default='rbf')
         Specifies the kernel type to be used in the algorithm.
         It must be one of 'linear', 'poly', 'rbf', 'sigmoid', 'precomputed' or
         a callable.
         If none is given, 'rbf' will be used. If a callable is given it is
         used to precompute the kernel matrix.

    degree : int, optional (default=3)
        Degree of the polynomial kernel function ('poly').
        Ignored by all other kernels.

    gamma : float, optional (default='auto')
        Kernel coefficient for 'rbf', 'poly' and 'sigmoid'.

        Current default is 'auto' which uses 1 / n_features,
        if ``gamma='scale'`` is passed then it uses 1 / (n_features * X.std())
        as value of gamma. The current default of gamma, 'auto', will change
        to 'scale' in version 0.22. 'auto_deprecated', a deprecated version of
        'auto' is used as a default indicating that no explicit value of gamma
        was passed.

    coef0 : float, optional (default=0.0)
        Independent term in kernel function.
        It is only significant in 'poly' and 'sigmoid'.

    tol : float, optional (default=1e-3)
        Tolerance for stopping criterion.

    C : float, optional (default=1.0)
        Penalty parameter C of the error term.

    epsilon : float, optional (default=0.1)
         Epsilon in the epsilon-SVR model. It specifies the epsilon-tube
         within which no penalty is associated in the training loss function
         with points predicted within a distance epsilon from the actual
         value.

    shrinking : boolean, optional (default=True)
        Whether to use the shrinking heuristic.

    cache_size : float, optional
        Specify the size of the kernel cache (in MB).

    verbose : bool, default: False
        Enable verbose output. Note that this setting takes advantage of a
        per-process runtime setting in libsvm that, if enabled, may not work
        properly in a multithreaded context.

    max_iter : int, optional (default=-1)
        Hard limit on iterations within solver, or -1 for no limit.

    Attributes
    ----------
    support_ : array-like, shape = [n_SV]
        Indices of support vectors.

    support_vectors_ : array-like, shape = [nSV, n_features]
        Support vectors.

    dual_coef_ : array, shape = [1, n_SV]
        Coefficients of the support vector in the decision function.

    coef_ : array, shape = [1, n_features]
        Weights assigned to the features (coefficients in the primal
        problem). This is only available in the case of a linear kernel.

        `coef_` is readonly property derived from `dual_coef_` and
        `support_vectors_`.

    intercept_ : array, shape = [1]
        Constants in decision function.
    '''

    def __init__(self, C=1.0, cache_size=200, coef0=0.0, degree=3, epsilon=0.1, gamma='auto',
                 max_iter=-1, shrinking=True, tol=0.001, verbose=False, warm_start=True, max_depth=4):
        self.C = C
        self.cache_size = cache_size
        self.coef0 = coef0
        self.degree = degree
        self.epsilon = epsilon
        self.gamma = gamma
        self.max_iter = max_iter
        self.shrinking = shrinking
        self.tol = tol
        self.verbose = verbose
        self.warm_start = warm_start
        self.max_depth = max_depth


class _LASSO(_BaseModel):
    def __init__(self, configuration):
        self.configuration = configuration
        self._instance = linear_model.Lasso()

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


class _KNeighborsRegressor(_BaseModel):
    def __init__(self, configuration):
        self.configuration = configuration
        self._instance = KNeighborsRegressor()

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


class _MLPRegressor(_BaseModel):
    def __init__(self, configuration):
        self.configuration = configuration
        self._instance = MLPRegressor(hidden_layer_sizes=(500,))

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


class _KERNEL_RIDGE(_BaseModel):
    def __init__(self, configuration):
        self.configuration = configuration
        self._instance = KernelRidge()

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


class _SVR(_BaseModel):
    def __init__(self, kernel, configuration):
        self.kernel = kernel
        self.configuration = configuration
        self._instance = SVR(C=1.0, cache_size=configuration.cache_size, coef0=configuration.coef0,
                             degree=configuration.degree, epsilon=configuration.epsilon, gamma=configuration.gamma,
                             kernel=kernel, max_iter=configuration.max_iter, shrinking=configuration.shrinking,
                             tol=configuration.tol, verbose=configuration.verbose)

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


class _SVR_Linear(_SVR):
    def __init__(self, configuration):
        super().__init__('linear', configuration)


class _SVR_RBF(_SVR):
    def __init__(self, configuration):
        super().__init__('rbf', configuration)


class _SVR_Poly(_SVR):
    def __init__(self, configuration):
        super().__init__('poly', configuration)


class _SGDRegressor(_BaseModel):
    def __init__(self, configuration):
        self.configuration = configuration
        self._instance = linear_model.SGDRegressor(
            warm_start=configuration.warm_start, max_iter=configuration.max_iter)

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


class _DecisionTreeRegressor(_BaseModel):
    def __init__(self, configuration):
        self.configuration = configuration
        self._instance = tree.DecisionTreeRegressor(
            max_depth=configuration.max_depth)

    def fit(self, _x, _y):
        return self._instance.fit(X=_x, y=_y)

    def predict(self, _x):
        return self._instance.predict(X=_x)


INSTANCE_CACHE = {NORMALIZATION_TYPE.MIN_MAX_SCALER: preprocessing.MinMaxScaler(feature_range=(0, 10))}


class ModelFactory:

    def __init__(self):
        self.MODEL_TYPE_CLASSES = {ML_MODELS_TYPES.SVR_LINEAR: _SVR_Linear, ML_MODELS_TYPES.SVR_POLY: _SVR_Poly,
                                   ML_MODELS_TYPES.SVR_RBF: _SVR_RBF, ML_MODELS_TYPES.DTR: _DecisionTreeRegressor,
                                   ML_MODELS_TYPES.LASSO: _LASSO, ML_MODELS_TYPES.KERNEL_RIDGE: _KERNEL_RIDGE,
                                   ML_MODELS_TYPES.MLP_REGRESSOR: _MLPRegressor, ML_MODELS_TYPES.K_NEIGHBORS_REGRESSOR: _KNeighborsRegressor,
                                   NORMALIZATION_TYPE.MAX_ABS_SCALER: preprocessing.MaxAbsScaler, NORMALIZATION_TYPE.MIN_MAX_SCALER: preprocessing.MinMaxScaler,
                                   NORMALIZATION_TYPE.NORMALIZER: preprocessing.Normalizer, NORMALIZATION_TYPE.STANDARD_SCALER: preprocessing.StandardScaler}

    def get_instance(self, model_type, config):
        if not INSTANCE_CACHE.get(model_type):
            model = self.MODEL_TYPE_CLASSES.get(model_type)
            if not model:
                return None
            if not config:
                INSTANCE_CACHE[model_type] = model()
            else:
                INSTANCE_CACHE[model_type] = model(config)

        return INSTANCE_CACHE.get(model_type)


class MachineLearningModelsScore:
    def __init__(self, models=[(ML_MODELS_TYPES.SVR_LINEAR, NORMALIZATION_TYPE.STANDARD_SCALER), (ML_MODELS_TYPES.SVR_POLY, NORMALIZATION_TYPE.MIN_MAX_SCALER),
                               (ML_MODELS_TYPES.SVR_RBF, NORMALIZATION_TYPE.STANDARD_SCALER), (ML_MODELS_TYPES.DTR, NORMALIZATION_TYPE.MIN_MAX_SCALER),
                               (ML_MODELS_TYPES.LASSO, NORMALIZATION_TYPE.MIN_MAX_SCALER), (ML_MODELS_TYPES.KERNEL_RIDGE, NORMALIZATION_TYPE.MIN_MAX_SCALER),
                               (ML_MODELS_TYPES.MLP_REGRESSOR, NORMALIZATION_TYPE.MIN_MAX_SCALER), (ML_MODELS_TYPES.K_NEIGHBORS_REGRESSOR, NORMALIZATION_TYPE.MIN_MAX_SCALER)],
                 models_config=ML_Configuration(), normalization=True):
        self._models = models
        self._models_config = models_config
        self._normalization = normalization

    def predit(self, _x):
        factory = ModelFactory()
        result = {}

        for model in self._models:
            model_ml = model[0]
            model_nor = model[1]
            obj = factory.get_instance(model_ml, self._models_config)
            x = self._get_normal_data(_x, factory.get_instance(model_nor, None))
            result[model_ml] = obj.predict(x)

        return result

    def _get_normal_data(self, x, normalizer):
        if self._normalization and normalizer:
            x = normalizer.fit(X=x).transform(X=x)
        return x

    def get_models_score(self, x, y, x_test, y_test):
        factory = ModelFactory()
        scores = {}
        for model in self._models:
            model_ml = model[0]
            model_nor = model[1]
            obj = factory.get_instance(model_ml, self._models_config)
            x = self._get_normal_data(x, factory.get_instance(model_nor, None))
            fit = obj.fit(x, y)
            x_test = self._get_normal_data(x_test, factory.get_instance(model_nor, None))
            score = obj.cross_validate(fit, x_test, y_test)
            scores[model_ml] = score
        return scores
