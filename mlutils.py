import os, sys, re, time

import pandas as pd
import numpy as np
from sklearn import linear_model
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

DEBUG = 1


def gnb_classification(training_file="UCI_training.csv", test_file="UCI_test.csv", category_fieldname="stabf"):
    curdir = os.getcwd()
    training_file = curdir + os.path.sep + training_file
    test_file = curdir + os.path.sep + test_file

    training_df = pd.read_csv(training_file)
    label = training_df[category_fieldname]
    training_features = training_df.drop("stabf", axis=1)
    training_df.fillna(0.0, inplace=True) # Fill NaN values with 0

    gnb = GaussianNB() # Using Gaussian Naive Bayes. Will try other algorithms later.
    model = gnb.fit(training_features, label)
    test_df = pd.read_csv(test_file)
    test_features = test_df.drop("stabf", axis=1)
    #print "\n@@@@@@@@@@@@@@@@@@@@@@@\n", test_features, "\n@@@@@@@@@@@@@@@@@@@@@@@\n\n"
    preds = gnb.predict(test_features)
    test_data_id = 2 # That is the line from where the test data starts. The first line is headers.
    if DEBUG:
        for p in preds:
            print "Entity #%s: %s"%(test_data_id, p)
            test_data_id += 1
    else:
        pass
    return preds



def trainer_regression(training_file="training_nifty.csv", test_file="test_nifty.csv", category_fieldnames=["Date", "Volume"]):
    # Get current directory
    curdir = os.getcwd()
    training_file = curdir + os.path.sep + training_file
    test_file = curdir + os.path.sep + test_file

    training_df = pd.read_csv(training_file)
    label = training_df['Volume']
    features = training_df.drop(category_fieldnames, axis=1)
    training_df.fillna(0.0, inplace=True) # Fill NaN values with 0
    features.fillna(0.0, inplace=True)
    
    training_regr = linear_model.LinearRegression()
    try:
        training_regr.fit(features, label)
    except:
        print "LABEL: ", label, "Error: %s"%sys.exc_info()[1].__str__()
        sys.exit()
    np.set_printoptions(precision=2)

    # Get the test data in which we will predict the 'Volume' attribute
    test_df = pd.read_csv(test_file)
    test_features = test_df.drop(category_fieldnames, axis=1)
    test_features.fillna(0.0, inplace=True)
    if DEBUG:
        print training_regr.predict(test_features)
    return test_features


if __name__ == "__main__":
    if DEBUG:
        tf = trainer_regression()
        preds = gnb_classification()
    else:
        print "DEBUG mode is off. You cannot run the script from command line. Kindly import the functions and call them from your program\n"


