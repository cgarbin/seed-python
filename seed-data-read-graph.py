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


if __name__ == '__main__':
    main()
