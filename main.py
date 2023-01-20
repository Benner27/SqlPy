import math
from utils import Utils, DBUtils
from loss_function import squared_error
from models import TrainingData, IdeaFunction
from function import FunctionManager, FunctionManagerIterator
from regression import minimise_loss, find_classification
from plotting import plot_ideal_functions, plot_points_with_their_ideal_function

train_data_path = 'data/train_datasetsPy.csv'
ideal_funcs_path = 'data/ideal_datasetsPy.csv'

# Constant criterion assignment factor
Exclusive_Factor = math.sqrt(2)

if __name__ == "__main__":
    # Pandas effectivity is utilized to stack up "X" and "Y" Function points
    # FunctionManager receives steps to CSV file and analyses Function objects amidst the data

    candidate_ideal_function_manager = FunctionManager(ideal_funcs_path)
    train_function_manager = FunctionManager(path_of_csv=train_data_path)

    # Establishes SQLite database for our data storage
    # Generates tables according to the required database models
    DBUtils.create_db()

    # The train data CSV is transmitted then transferred into the SQLite db
    DBUtils.populate_db(train_data_path, TrainingData)

    # Transmission of CSV file containing ideal functions data is then transferred into the SQLite db
    DBUtils.populate_db(ideal_funcs_path, IdeaFunction)

    # Ideal_function_manager inhabits 50 functions.
    # Train_function_manager inhabits 4 functions to be iterated upon and calculate tolerance.
    # The data is utilized to evaluate most exceptional IdealFunction, it also keeps a list.
    ideal_functions = []

    # The train function utilizes minimise_loss to fabricate an exceptional function
    for train_function in train_function_manager:
        ideal_function = minimise_loss(training_function=train_function,
                                       list_of_candidate_functions=candidate_ideal_function_manager.functions,
                                       loss_function=squared_error)
        ideal_function.tolerance_factor = Exclusive_Factor
        ideal_functions.append(ideal_function)

    # Classification is utilized to map points
    create_ideal_functions_plots(ideal_functions, "plots/train_and_ideal")

    # FunctionManager reuses assembled CSV file.
    # Assessment of every test data point that are iterated through function object
    # At location [0], different functions are reduced to a distinct "Function"
    test_path = "data/datasetsPy.csv"
    test_function_manager = FunctionManager(csv_path=test_path)
    test_function = test_function_manager.functions[0]

    # Dictionaries contain findings for every classification point
    # Overview: list of dictionaries stowed in points_with_ideal_function
    points_with_ideal_function = []
    for point in test_function:
        ideal_function, delta_y = classify_point(point=point, ideal_fn_list=ideal_functions)
        result = {"point": point, "classification": ideal_function, "delta_y": delta_y}
        points_with_ideal_function.append(result)

    # Utilizing corresponding classification function to map points
    create_plot_points_with_their_ideal_function(points_with_ideal_function, "plots/point_and_ideal")

    # Finalize by utilizing dict object to note it to a SQLite database
    # Utilization of SQLAlchemy technique with a MetaData object process
    Utils.write_deviation_results_to_db(points_with_ideal_function)
    print("main.db: Well-equipped SQLite file")
    print("train_and_ideal.html: Observe training data as scatter and the most convenient ideal function as curve")
    
    print("points_and_ideal.html: Contemplate matching ideal function for the points and frame distance inbetween them")
    print("Victorious Assignment accomplishment")
