from function import IdealFunction


def minimise_loss(training_function, loss_function, list_of_candidate_functions):
    """ IdealFunction established on a training function and a list of ideal functions
    :param training_fn: training function
    
    :param error_fn: utilizes error minimization
    :param candidate_fn_list: Ideal functions list
    :return: a IdealFunction object with least error. """
    best_fit = None
    least_error = None
    for fn in candidate_fn_list:
        current_error = error_fn(training_fn, fn)
        if (lowest_error == None) or current_error < lowest_error:
            lowest_error = current_error
            best_fit = fn

    ideal_function = IdealFunction(function=best_fit, training_function=training_fn,
                                   error=lowest_error)
    return ideal_function


def classify_point(point, ideal_fn_list):
    """ Points within the Ideal objects and their tolerance of a closest classification to lead to computation
    :param ideal_fn_list: list of IdealFunction objects
   
    :param point: Contain an "x" dict object and a "y" dict object
    :return:Comprises a tuple encompassing min available closest classification and the distance. """
    closest_classification = None
    closest_distance = None

    for fn in ideal_fn_list:
        try:
            y_value = fn.locate_y_based_on_x(point["x"])
        except IndexError:
            print("Classification function does not represent this point")
            raise IndexError

        distance = abs(y_value - point["y"])

        # Operates several classifications to return the least distance
        if abs(distance) < fn.tolerance:
            if closest_classification == None or distance < closest_distance:
                closest_classification = fn
                closest_distance = distance

     return closest_classification, closest_distance

