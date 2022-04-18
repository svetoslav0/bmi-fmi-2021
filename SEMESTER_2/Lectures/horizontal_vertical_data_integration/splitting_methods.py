from enum import Enum
from sklearn.model_selection import LeavePOut
from sklearn.model_selection import LeaveOneOut
from sklearn.model_selection import KFold
from sklearn.model_selection import ShuffleSplit
import inspect


class _BaseSplitter:
    def get_splited_data(self, _x, _y, split_num=100):
        pass


class _KFold(_BaseSplitter):
    def get_splited_data(self, _x, _y, split_num=100):
        __kf = KFold(n_splits=split_num)

        for train, test in __kf.split(_x, y=_y):
            yield train, test

class _LeavePOut(_BaseSplitter):
    def get_splited_data(self, _x, _y, split_num=100):
        lpo = LeavePOut(p=split_num)
        for train_index, test_index in lpo.split(_x):
            yield train_index, test_index

class _ShuffleSplit(_BaseSplitter):
    def get_splited_data(self, _x, _y, split_num=100):
        ss = ShuffleSplit(n_splits=split_num)
        for train_index, test_index in ss.split(X=_x):
            yield train_index, test_index


class SplitMethod(Enum):
    '''
    >>>>LEAVE_P_OUT use 'from sklearn.model_selection import LeaveOneOut'<<<<
    Provides train/test indices to split data in train/test sets. Each
    sample is used once as a test set (singleton) while the remaining
    samples form the training set.

    Note: ``LeaveOneOut()`` is equivalent to ``KFold(n_splits=n)`` and
    ``LeavePOut(p=1)`` where ``n`` is the number of samples.

    Due to the high number of test sets (which is the same as the
    number of samples) this cross-validation method can be very costly.
    For large datasets one should favor :class:`KFold`, :class:`ShuffleSplit`
    or :class:`StratifiedKFold`.

    Read more in the :ref:`User Guide <cross_validation>`.

    >>>LEAVE_P_OUT use from sklearn.model_selection import LeavePOut<<<<
    Provides train/test indices to split data in train/test sets. This results
    in testing on all distinct samples of size p, while the remaining n - p
    samples form the training set in each iteration.

    Note: ``LeavePOut(p)`` is NOT equivalent to
    ``KFold(n_splits=n_samples // p)`` which creates non-overlapping test sets.

    Due to the high number of iterations which grows combinatorically with the
    number of samples this cross-validation method can be very costly. For
    large datasets one should favor :class:`KFold`, :class:`StratifiedKFold`
    or :class:`ShuffleSplit`.


    >>>K_FOLD use from sklearn.model_selection import KFold<<<<
    Provides train/test indices to split data in train/test sets. Split
    dataset into k consecutive folds (without shuffling by default).

    Each fold is then used once as a validation while the k - 1 remaining
    folds form the training set.

    '''

    LEAVE_P_OUT = _LeavePOut
    K_FOLD = _KFold
    SHUFFLE_SPLIT = _ShuffleSplit

class _SplitterFactory:
    __splitt_methods = {SplitMethod.K_FOLD: _KFold, SplitMethod.LEAVE_P_OUT: _LeavePOut, SplitMethod.SHUFFLE_SPLIT: _ShuffleSplit}

    @staticmethod
    def get_splitter_instance(_splitt_method):
        return _SplitterFactory.__splitt_methods[_splitt_method]()

class Splitter:
    '''
    Split data set _x, _y to train and test data sets.
    Use SplitMethod enum to define chouse method for splitting
    '''

    def __init__(self, split_method):
        self.split_method = split_method
        self._splitter = _SplitterFactory.get_splitter_instance(split_method)

    def split(self, _x, _y, split_n=100):
        """Generate indices to split data into training and test set.

        Parameters
        ----------
        _x : array-like, shape (n_samples, n_features)
            Training data, where n_samples is the number of samples
            and n_features is the number of features.

        _y : array-like, shape (n_samples,), optional
            The target variable for supervised learning problems.

        split_n : n_sample
        the samples used while splitting the dataset into train/test set."""

        return self.__get_splitted_data(_x, _y, self.split_method, split_n)

    def __get_splitted_data(self, __x, __y, __spliting_method, __split_n=100):
        _x_train = []
        _y_train = []
        _x_test = []
        _y_test = []

        for _train_index, _test_index in self._splitter.get_splited_data(__x, __y, split_num=__split_n):
            _x_train.extend(__x[_train_index])
            _x_test.extend(__x[_test_index])
            _y_train.extend(__y[_train_index])
            _y_test.extend(__y[_test_index])
            break

        return [_x_train, _y_train, _x_test, _y_test]
