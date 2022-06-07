"""
Interface class for estimators.
"""
from abc import ABC, abstractmethod
from typing import Any, Dict, List, TypeVar

E = TypeVar("E", bound="AnEstimator")
DataType = Dict[str, List[Any]]


class AnEstimator(ABC):
    """Estimators are classes that learn parameters on data and can use those
    to make predictions.

    The estimator interface offers 2 methods: `fit` and `predict`.
    """

    @abstractmethod
    def fit(self: E, data: DataType, features: List[str], target: str) -> E:
        """
        Using the features in the data, build a model to predict the target.

        Parameters
        ----------
        data: Dict[str, List[Any]]
            data is a primitive representation of a data frame. More precisely,
            data is a dict where the keys are the column names and the values
            are a list of the values in that column. See the example below.
        features: List[str]
            A list of column names in data to use as features for training.
        target: str
            The name of the target column.

        Returns
        -------
        self: the estimator itself.

        Examples
        --------
        >>> est: AnEstimator
        >>> train = {"x_1": [1, 2], "x_2": ["a", "b"], "y": ["y", "n"]}
        >>> est.fit(train, ["x_1"], "y")
        """
        raise NotImplementedError

    @abstractmethod
    def predict(self, data: DataType, pred_col: str) -> DataType:
        """
        Make predictions on the data.

        Parameters
        ----------
        data: Dict[str, List[Any]]
            data is a primitive representation of a data frame. More precisely,
            data is a dict where the keys are the column names and the values
            are a list of the values in that column. See the example below.
        pred_col: str
            the name of the column containing the predictions.

        Returns
        -------
        predictions: Dict[str, List[Any]]
            the predictions, represented in the same format as the `data`
            parameter. The name of the (single) column will be `pred_name`.

        Examples
        --------
        >>> est: AnEstimator
        >>> train = {"x_1": [1, 2], "x_2": ["a", "b"], "y": ["y", "n"]}
        >>> test = {"x_1": [1, 2, 1]}
        >>> est.fit(train, ["x_1"], "y").predict(test,"y_pred")
        {"y_pred": ["y", "n", "y"]}
        """
        raise NotImplementedError
