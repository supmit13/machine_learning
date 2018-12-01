import os, sys, re, time

import pandas as pd
import numpy as np
from sklearn import linear_model
#from sklearn.preprocessing import MinMaxScaler
#from sklearn.preprocessing import StandardScaler
from sklearn.naive_bayes import GaussianNB

# Get current directory
curdir = os.getcwd()

# We will have the UCI_training.csv file to read
training_file = curdir + os.path.sep + "UCI_training.csv"

# We also have the test data that we will need to verify our prediction results.
test_file = curdir + os.path.sep + "UCI_test.csv"

if __name__ == "__main__":
    training_df = pd.read_csv(training_file)
    label = training_df["stabf"]
    training_features = training_df.drop("stabf", axis=1)
    training_df.fillna(0.0, inplace=True) # Fill NaN values with 0

    gnb = GaussianNB() # Using Gaussian Naive Bayes. Will try other algorithms later.
    model = gnb.fit(training_features, label)
    test_df = pd.read_csv(test_file)
    test_features = test_df.drop("stabf", axis=1)
    #print "\n@@@@@@@@@@@@@@@@@@@@@@@\n", test_features, "\n@@@@@@@@@@@@@@@@@@@@@@@\n\n"
    preds = gnb.predict(test_features)
    test_data_id = 2 # That is the line from where the test data starts. The first line is headers.
    for p in preds:
        print "Entity #%s: %s"%(test_data_id, p)
        test_data_id += 1
    
