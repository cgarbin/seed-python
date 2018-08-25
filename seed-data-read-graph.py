"""
A seed for data loading, parsing, graphing in Python, using pandas

Covers:

* Read data from files
* Manipulate the data
* Filter data
* Visualize data in graphs

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


if __name__ == '__main__':
    main()
