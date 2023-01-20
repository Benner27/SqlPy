from bokeh.models import ColumnDataSource, Band
from bokeh.plotting import output_file, figure, show
from bokeh.layouts import grid, column


def create_ideal_function_plots(ideal_functions, file_name):
    """ Maps every ideal functions. Issues arguments through unpacking
    :param ideal_functions: list of ideal functions
    :param file_name: .html file name. """
    ideal_functions.sort(key=lambda ideal_function: ideal_function.training_function.name, reverse=False)
    plots = []
    for ideal_function in ideal_functions:
        p = create_graph_plot(line_function=ideal_function,
                                          scatter_function=ideal_function.training_function,
                                          squared_error=ideal_function.error)
        plots.append(p)

    output_file("{}.html".format(file_name))
    show(column(*plots))


def create_plot_points_with_their_ideal_function(points_with_classification, file_name):
    """ Complimented classified points are mapped together
    :param points_with_classification: a list containing dicts with "classification" and "point"
    :param file_name: the .html file. """
    plots = []
    for index, item in enumerate(points_with_classification):
        if item["classification"] is not None:
            p = create_classification_plot(item["point"], item["classification"])
            plots.append(p)
    output_file("{}.html".format(file_name))
    show(column(*plots))


def create_graph_plot(scatter_function, line_function, squared_error):
    """ Maps dissipation for train_function and a line for the ideal_function
    :param scatter_function: the train function
    
    :param line_function: ideal function
    :param squared_error: Mapped in the heading. """
    f1_dataframe = scatter_function.dataframe
    f1_name = scatter_function.name

    f2_dataframe = line_function.dataframe
    f2_name = line_function.name

    squared_error = round(squared_error, 2)
    p = figure(title="train model {} vs ideal {}. Total squared error = {}".format(f1_name, f2_name, squared_error),
               x_axis_label='x', y_axis_label='y')
    p.scatter(f1_dataframe["x"], f1_dataframe["y"], fill_color="red", legend_label="Train")
    p.line(f2_dataframe["x"], f2_dataframe["y"], legend_label="Ideal", line_width=2)
    return p


def create_classification_plot(point, ideal_function):
    """ Reveals tolerance, maps an elevated point and the classification,
    :param point: a dict with "x" and "y"
    :param ideal_function: a classification object. """
    if ideal_function is not None:
        classification_function_dataframe = ideal_function.dataframe

        point_str = "({},{})".format(point["x"], round(point["y"], 2))
        title = "point {} with classification: {}".format(point_str, ideal_function.name)

        p = figure(title=title, x_axis_label='x', y_axis_label='y')

        # Maps ideal function
        p.line(classification_function_dataframe["x"], classification_function_dataframe["y"],
               legend_label="Classification function", line_width=2, line_color='black')

        # Design exhibits tolerance inside the graph
        criterion = ideal_function.tolerance
        classification_function_dataframe['upper'] = classification_function_dataframe['y'] + criterion
        classification_function_dataframe['lower'] = classification_function_dataframe['y'] - criterion

        source = ColumnDataSource(classification_function_dataframe.reset_index())

        band = Band(base='x', lower='lower', upper='upper', source=source, level='underlay',
                    fill_alpha=0.3, line_width=1, line_color='green', fill_color="green")

        # Increases band layout
        p.add_layout(band)

        # Transfers points
        p.scatter([point["x"]], [round(point["y"], 4)], fill_color="red", legend_label="Test point", size=8)

        return p
