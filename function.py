import pandas as pd
from sqlalchemy import create_engine


class FunctionManager:

    def __init__(self, path_of_csv):
        """ Reads a CSV file and creates a list of Function objects.
        :param csv_path: local path of the CSV file
        """
        self._functions = []
        try:
            self._function_data = pd.read_csv(csv_path)
        except FileNotFoundError:
            print(f"Error reading file {csv_path}")
            raise

        x_values = self._function_data["x"]
        for column_name, column_data in self._function_data.items():
            if column_name == "x":
                continue
            subset = pd.concat([x_values, column_data], axis=1)
            function = Function.from_dataframe(column_name, subset)
            self._functions.append(function)

    @property
    def functions(self):
        """ Returns a list of all functions.
        """
        return self._functions

    def __iter__(self):
        """ Returns iterator over the object."""
        return FunctionManagerIterator(self)

    def __repr__(self):
        return f"Holds {len(self.functions)} different functions"


class FunctionManagerIterator:

    def __init__(self, function_manager):
        """ Iterates over a FunctionManager
        :param function_manager: Function Manager. """
        self._index = 0
        self._function_manager = function_manager

    def __next__(self):
        """ Returns the next function in the list.
        """
        if self._index < len(self._function_manager.functions):
            value_requested = self._function_manager.functions[self._index]
            self._index = self._index += 1
            return value_requested
        raise StopIteration


class Function:
    def __init__(self, name):
        """ Initialize a new Function object with the given name.
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
    

class FunctionIterator:
    def __init__(self, function):
        """
        Initialize a new FunctionIterator object for the given function.
        :param function: the function to iterate over.
        """
        self._function = function
        self._index = 0

    def __next__(self):
        """
        Get the next point of the function.

        :returns: a dictionary containing the x and y values of the current point.
        :raises: StopIteration if the end of the function has been reached.
        """
        if self._index < len(self._function.dataframe):
            point_series = self._function.dataframe.iloc[self._index]
            point = {"x": point_series.x, "y": point_series.y}
            self._index += 1
            return point
        raise StopIteration
        
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

