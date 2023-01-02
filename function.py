import pandas as pd
from sqlalchemy import create_engine


class FunctionManager:

    def __init__(self, path_of_csv):
        """ Iterates over object, analyses CSV file (all columns contain y- values except first column
        that has x-values) into a list of returned Functions restored through .functions property.
        param path_of_csv: local path of the csv. """
        self._functions = []

        # Scans Csv file using Panda module and changes into a dataframe
        try:
            self._function_data = pd.read_csv(path_of_csv)
        except FileNotFoundError:
            print("Complications reading file {}".format(path_of_csv))
            raise

        # Storage of x values and loaded into each Function
        x_values = self._function_data["x"]

        # Contemporary Function object is established as Panda dataframe iterates over independent columns.
        # Y column is developed, and Concat function is then used to combine x and y columns
        for name_of_column, data_of_column in self._function_data.items():
            if "x" in name_of_column:
                continue
            subset = pd.concat([x_values, data_of_column], axis=1)
            function = Function.from_dataframe(name_of_column, subset)
            self._functions.append(function)

    @property
    def functions(self):
        """ Produces a list of all functions that user utilizes to iterate over object.
        :rtype: object. """
        return self._functions

    def __iter__(self):
        """ Iterates over the object."""
        return FunctionManagerIterator(self)

    def __repr__(self):
        return "Holds {} different functions".format(len(self.functions))


class FunctionManagerIterator():

    def __init__(self, function_manager):
        """ Iterates over a FunctionManager
        :param function_manager: Function Manager. """
        self._index = 0
        self._function_manager = function_manager

    def __next__(self):
        """ Iteration over list of functions produces function object
        :rtype: function. """
        if self._index < len(self._function_manager.functions):
            value_requested = self._function_manager.functions[self._index]
            self._index = self._index + 1
            return value_requested
        raise StopIteration


class Function:

    def __init__(self, name):
        """ Stores retrievable names and the X and Y values of a function.
        i) Utilizes Panda dataframe and eases regression calculations
        ii) Iterates and returns points symbolized as dict
        iii) Fetches Y-Value by providing an X-Value
        iv) Returns dataframe with the deviation by subtracting two functions
        :param name: the function name. """
        self._name = name
        self.dataframe = pd.DataFrame()

    def locate_y_based_on_x(self, x):
        """ Panda iloc function is utilized to locate x and return matching y function otherwise
        causes exception if it fails
        :param x: X-Value
        :retrieves: Y-Value. """
        search_key = self.dataframe["x"] == x
        try:
            return self.dataframe.loc[search_key].iat[0, 1]
        except IndexError:
            raise IndexError

    @property
    def name(self):
        """ Tags the function as str."""
        return self._name

    def __iter__(self):
        return FunctionIterator(self)

    def __sub__(self, other):
        """ Returns recent dataframe upon subtracting two functions
        :rtype: object. """
        diff = self.dataframe - other.dataframe
        return diff

    @classmethod
    def from_dataframe(cls, name, dataframe):
        """ Delivers a dataframe by instantly creating a function hence replacing primary column names to "x" and "y"
        :rtype: a Function. """
        function = cls(name)
        function.dataframe = dataframe
        function.dataframe.columns = ["x", "y"]
        return function

    def __repr__(self):
        return "Function for {}".format(self.name)


class IdealFunction(Function):
    def __init__(self, function, training_function, error):
        """ An ideal function deposits predicting function, training data and the regression.
        To avoid reverting to maximum deviation between ideal and training function, ensure tolerance_factor
        availability incase classification purpose tolerance is permitted
        :param function: the ideal function
        :param training_function: the classifying data relies on training data
        :param squared_error: calculated in advance regression. """
        super().__init__(function.name)
        self.dataframe = function.dataframe
        self.training_function = training_function
        self.error = error
        self._tolerance_value = 1
        self._tolerance = 1

    def _determine_tremendous_deviation(self, ideal_function, train_function):
        """ Takes two functions and subtracts them to decide the maximum outcome of dataframe. """
        distances = train_function - ideal_function
        distances["y"] = distances["y"].abs()
        tremendous_deviation = max(distances["y"])
        return tremendous_deviation

    @property
    def tolerance(self):
        """ Explains accepted tolerance regarding the regression for it to be considered as classification.
        Rather than setting a direct tolerance, issuing a tolerance_factor is advised.
        :return: the tolerance """
        self._tolerance = self.tolerance_factor * self.greatest_deviation
        return self._tolerance

    @tolerance.setter
    def tolerance(self, value):
        self._tolerance = value

    @property
    def tolerance_factor(self):
        """ Dictates the tolerance through greatest_deviation factor
        :return: tolerance. """
        return self._tolerance_value

    @tolerance_factor.setter
    def tolerance_factor(self, value):
        self._tolerance_value = value

    @property
    def greatest_deviation(self):
        """ Relies on retrieving the largest deviation between ideal function and the training function"""
        tremendous_deviation = self._determine_tremendous_deviation(self, self.training_function)
        return tremendous_deviation


class FunctionIterator:

    def __init__(self, function):
        """ Returns a dict which explains the point after iterating over a function"""
        self._function = function
        self._index = 0

    def __next__(self):
        """ Returns a dict describing the point after iterating over a function"""
        if self._index < len(self._function.dataframe):
            value_requested_series = (self._function.dataframe.iloc[self._index])
            point = {"x": value_requested_series.x, "y": value_requested_series.y}
            self._index += 1
            return point
        raise StopIteration
