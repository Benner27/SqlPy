def calculate_squared_error(first_function, second_function):
    """ Computes squared error to a different function
    :param: other_function
    :return: complete_deviation from squared error. 
    """
    diff = second_function - first_function
    diff["y"] = diff["y"] ** 2
    deviation = diff["y"].sum()
    return deviation
