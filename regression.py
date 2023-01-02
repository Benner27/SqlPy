from function import IdealFunction


def minimise_loss(training_function, loss_function, list_of_candidate_functions):
    """ IdealFunction established on a training function and a list of ideal functions
    :param training_function: training function
    :param loss_function: utilizes error minimization
    :param list_of_candidate_functions: Ideal functions list
    :return: a IdealFunction object. """
    function_with_least_error = None
    least_error = None
    for function in list_of_candidate_functions:
        error = loss_function(training_function, function)
        if (least_error == None) or error < least_error:
            least_error = error
            function_with_least_error = function

    ideal_function = IdealFunction(function=function_with_least_error, training_function=training_function,
                                   least_error=error)
    return ideal_function


def find_classification(point, ideal_functions):
    """ Points within the tolerance of a classification to lead to computation
    :param ideal_functions: list of IdealFunction objects
    :param point: Contain an "x" dict object and a "y" dict object
    :return:Comprises a tuple encompassing min available closest classification and the distance. """
    current_lowest_classification = None
    current_lowest_distance = None

    for ideal_function in ideal_functions:
        try:
            encounter_y_in_classification = ideal_function.encounter_y_based_on_x(point["x"])
        except IndexError:
            print("Classification function does not represent this point")
            raise IndexError

        # Perceives absolute distance utilization
        distance = abs(encounter_y_in_classification - point["y"])

        # Operates several classifications to return the least distance
        if abs(distance < ideal_function.tolerance):

            if ((current_lowest_classification == None) or (distance < current_lowest_distance)):
                current_lowest_classification = ideal_function
                current_lowest_distance = distance

    return current_lowest_classification, current_lowest_distance
