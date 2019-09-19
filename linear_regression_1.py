### Tools for linear regression ###

import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm


def simulate_data():
    X1 = np.random.exponential(scale=1/9000, size=5000)

    X2 = np.random.poisson(lam=15, size=5000)

    B1 = 0.75
    B2 = -0.25

    epsilon = np.random.normal(0,1, size=5000)

    y= B1*X1+ B2*X2 +epsilon

    # model = smf.OLS ('Y~np.log(X)', data=df1).fit()
   pass


def compare_models():

        X = np.array([X1],[X2])
        y = array([Y])

    """
    Compares output from different implementations of OLS.
    INPUT
        X (ndarray) the independent variables in matrix form
        y (array) the response variables vector
    RETURNS
        results (pandas.DataFrame) of estimated beta coefficients
    """
    pass


def load_hospital_data():
    """
    Loads the hospital charges data set found at data.gov.
    INPUT
        path_to_data (str) indicates the filepath to the hospital charge data (csv)
    RETURNS
        clean_df (pandas.DataFrame) containing the cleaned and formatted dataset for regression
    """
    pass


def prepare_data():
    """
    Prepares hospital data for regression (basically turns df into X and y).
    INPUT
        df (pandas.DataFrame) the hospital dataset
    RETURNS
        data (dict) containing X design matrix and y response variable
    """
    pass


def run_hospital_regression():
    """
    Loads hospital charge data and runs OLS on it.
    INPUT
        path_to_data (str) filepath of the csv file
    RETURNS
        results (str) the statsmodels regression output
    """
    pass
 

### END ###