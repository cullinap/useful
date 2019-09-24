import numpy as np
import pandas as pd
import statsmodels.api as sm
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV
from sklearn.metrics import mean_absolute_error
from statsmodels.tools.eval_measures import mse, rmse
from sklearn.model_selection import train_test_split


def _split(X,Y):
	X_train, X_test, y_train, y_test = train_test_split(
										X, Y, 
										test_size = 0.2, 
										random_state = 465)

	return X_train, X_test, y_train, y_test


def split(X, Y):
	data = _split(X,Y)
	print("Training set # {}".format(data.X_train.shape[0]))
	print("Test set # {}".format(data.X_test.shape[0]))


def linear_regression():
	pass 
	#X_train = sm.add_constant(X_train)
