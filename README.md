# Assignment Py
Algorithm of the Task

The core objective of this project, is to find the best fitting function for a given dataset by comparing the performance of different candidate functions using a loss function such as mean squared error (MSE). MSE is calculated by taking the average of the squares of the differences between the predicted values (from the candidate function) and the true values (from the training dataset). The function with the lowest MSE will be selected as the best fitting function.

The results of this analysis will be stored in a SQLite database, along with the training data and any additional relevant information. We will use the SQLite3 module in Python to connect to the database and execute SQL commands to create tables and insert data. The pandas library will be used to read in the data from the CSV file and write it to the SQLite database using the 'to_sql' method.

To visualize the data and results, we will use Panda's 'read_sql' method to retrieve the data from the SQLite database and then use Bokeh and SQLAlchemy to create plots and visualizations.
The implementation of exception handling in the code to handle any unexpected errors that may occur. This can be done using try-except blocks to catch specific exceptions or using a generic except block to catch any exception.

Finally, unit tests will be written using a testing framework like PyTest to ensure that our code is working correctly. These tests will consist of functions that test specific aspects of the code, and these tests will be run to confirm the correctness of the code.

The implementation itself is explained in chapter 5 and 6.

# Running the code

1. Create a virtual environment with

```
python -m venv env
```

2. On windows, activate it with

```
E:\my_env\Script\activate.bat
```

3. Install requirements

```
pip install -r requirements.txt
```

4. Now run with

```
python main.py
```
