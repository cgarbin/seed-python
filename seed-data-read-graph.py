"""
A seed for data loading, parsing, graphing in Python, using pandas

Covers:

* Read data from files
* Manipulate the data
* Filter data
* Visualize data in graphs

Sources:

* https://towardsdatascience.com/exploratory-data-analysis-with-pandas-and-jupyter-notebooks-36008090d813
* https://jeffdelaney.me/blog/useful-snippets-in-pandas/
* https://pandas.pydata.org/pandas-docs/stable/tutorials.html
* https://pandas.pydata.org/pandas-docs/stable/cookbook.html

"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def main():
    df = pd.read_csv('./employees.csv',
                     parse_dates=['hire date'], skipinitialspace=True)

    # Add a new column based on the value of another column
    # numpy version
    df['high salary'] = np.where(df['salary'] >= 7000, 'yes', 'no')
    print(df)

    # Add a new column based on the value of another column
    # List comprehension version
    # See https://stackoverflow.com/q/50375985/336802 for comparison of methods
    df['high salary'] = ['yes' if x >= 7000 else 'no' for x in df['salary']]
    print(df)

    # Add a column using vectorized operation with isin()
    high_salary = df['salary'] >= 7000
    low_salary = df['salary'] < 7000
    df.loc[high_salary, 'high salary'] = 'yes'
    df.loc[low_salary, 'high salary'] = 'no'

    # What option to use?
    # See https://stackoverflow.com/q/50375985/336802 for comparison of methods
    # and https://realpython.com/fast-flexible-pandas/ for a detailed, step-by-
    # step case study of performance improvement.

    # Add a column using a function - for more involved cases
    def vacation_days(hire_date):
        today = pd.to_datetime('today')
        service_years = (today - hire_date) / np.timedelta64(1, 'Y')
        if service_years >= 20:
            return 25
        if service_years >= 15:
            return 20
        return 10
    df['vacation days'] = df['hire date'].apply(vacation_days)
    print(df[['first name', 'vacation days']])

    # Filter data based on column value
    # Why use .loc here: https://stackoverflow.com/a/48411543, and the details
    # in https://pandas.pydata.org/pandas-docs/stable/indexing.html#selection-by-label
    df_high = df.loc[df['high salary'] == 'yes']
    print(df_high)

    # Simple graph, using specific columns
    df.plot(x='first name', y='salary', kind='barh', legend=False)
    # Note: the graph won't display at this point
    # See call to plt.show() below

    # Choosing colors for the bars, based on another column
    df.plot(x='first name', y='salary', kind='barh', legend=False,
            color=np.where(df['high salary'] == 'yes', 'r', 'b'))

    # Same as above, using list comprehension
    df.plot(x='first name', y='salary', kind='barh', legend=False, color=[
            'r' if x == 'yes' else 'b' for x in df['high salary']])

    # Using categorical data for colors
    # While possible in pandas/matlibplot, this is easier with seaborn
    import seaborn as sns
    sns.pairplot(x_vars=['hire date'], y_vars=['salary'],
                 data=df, hue='education level', height=5)
    # Use matlibplot to control the legend (seaborn is based on matlibplot)
    # Without this line the legend is cut off (displayed to the right, not visible)
    plt.legend(loc=0)

    # Display all graphs at once
    # If we call this after each .plot, it will show the graph and interrupt
    # the program until that graph is window is closed
    # Note that in some cases the graph windows may be displayed right on top
    # of each other - move them around to see all graphs
    plt.show()


if __name__ == '__main__':
    main()
