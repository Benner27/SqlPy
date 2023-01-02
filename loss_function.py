def squared_error(first_function, second_function):
    """ Computes squared error to a different function
    :param: other_function
    :return: complete_deviation from squared error. """
    distances = second_function - first_function
    distances["y"] = distances["y"] ** 2
    complete_deviation = sum(distances["y"])
    return complete_deviation
