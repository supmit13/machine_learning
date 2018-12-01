import os, sys, re, time

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler

# Get current directory
curdir = os.getcwd()

# We will have the training_nifty.csv file to read
training_file = curdir + os.path.sep + "training_nifty.csv"

# We also have the test data that we will need to verify our prediction results.
test_file = curdir + os.path.sep + "test_nifty.csv"

if __name__ == "__main__":
    training_df = pd.read_csv(training_file)
    label = training_df['Volume']
    features = training_df.drop(["Date", "Volume"], axis=1)
    training_df.fillna(0.0, inplace=True) # Fill NaN values with 0
    features.fillna(0.0, inplace=True)
    #print "##############\n",features,"\n###############\n"
    # First, we do some feature scaling so that the data lies between 0 and 1
    #training_array = training_df.values
    #trg_X = training_array[:6,1:len(training_df)]
    #trg_Y = training_array[:,:len(training_df)]
    #scaler = MinMaxScaler(feature_range=(0, 1))
    #rescaledX = scaler.fit_transform(trg_X)
    # summarize transformed data
    np.set_printoptions(precision=2)
    #print(rescaledX[0:len(training_df),:])

    # Next, we do some standardization
    #training_scaler = StandardScaler().fit(trg_X)
    #rescaledX = training_scaler.transform(trg_X)
    training_regr = linear_model.LinearRegression()
    #print rescaledX.shape

    #print training_df,"$$$$$$$$$$$$$$$$$$$$$$$$"
    try:
        training_regr.fit(features, label)
    except:
        print "LABEL: ", label, "Error: %s"%sys.exc_info()[1].__str__()
        sys.exit()
    # summarize transformed data
    np.set_printoptions(precision=2)
    #print(rescaledX[0:len(training_df),:])

    # Get the test data in which we will predict the 'Volume' attribute
    test_df = pd.read_csv(test_file)
    test_features = test_df.drop(["Date", "Volume"], axis=1)
    test_features.fillna(0.0, inplace=True)
    print training_regr.predict(test_features)

    
    """
    # Define our regression - for sake of simplicity, I am considering a linear regression
    training_regr = linear_model.LinearRegression()
    training_regr.fit(features, label)
    print features
    """
