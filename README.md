# SqlPy
Data Sci Database Work

I. Establishing the absolute fitting ideal function

Begin by choosing the most appropriate ideal training function amongst 50 values provided in .CSV file (with x- and y- values). In our case, one with the lowest/mean squared error which is the average set of errors in relation to the training function.
Every ideal function to be discovered requires 4 different training functions.
This in essence is a variation of the “Mean squared deviation ” and is a popular loss function towards models are optimised.
Squared Error is when the deviation is squared (which eliminates negative values for differences and ensure positive results) and summed up. One quality includes a strong influence on huge deviations.
Each training function is examined point by point and the deviation of the y- value per ideal function value calculated. 
This is applied on every value function, such that the function with the lowest Squared Error becomes the ideal function, hence four ideal functions.

II: Data storage using SQLite
 
Data should be computed, enlisted into a SQLite database and three databases have to be created, one that reflects the training data set, 
another that simulates the ideal functions candidate data set and lastly, one that stocks the classifications and the deviation on to the ideal functions. Furthermore, if no classification is determined and the deviation cannot be catered for. 
On the occurrence of no classification, the program documents (-) within the “No of ideal function” column and (-1) inside the “Delta Y (test function)” column.

III. Alternative requirements

We are also expected to visualize the data using Panda packages, Bokeh and SQL alchemy to display an object-oriented design with an inheritance.
Furthermore, a standard and user-defined exception handling as well as "docstrings" should be applied as well, before unit tests are written for the elements. The implementation itself is explained in chapter 5 and 6.

# Unit 5 explains how to run the code

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
