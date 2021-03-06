import os, sys, re, time

import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from datetime import datetime
import matplotlib.pyplot as plt


# We will have the Diabetes training file to read
training_file = "/home/supriyo/work/machine_learning/machinelearning/datasets/Diabetes-Data/training_data.csv"

# We also have the test data that we will need to verify our prediction results.
test_file = "/home/supriyo/work/machine_learning/machinelearning/datasets/Diabetes-Data/final_data_test.csv"

column_to_determine = "Pre-lunch blood glucose measurement"
#column_predictor = "NPH insulin dose"
column_predictor = "Post-lunch blood glucose measurement"

if __name__ == "__main__":
    training_df = pd.read_csv(training_file)
    print training_df.keys(), "\n\n&&&&&&&&&&&&&&&&&&&&&&&&&&&\n\n"
    label = training_df[column_to_determine] # Take label of the feature that needs to be predicted.
    features = training_df.drop([column_predictor, column_to_determine], axis=1) # Take feature(s) values from training dataframe that need to be predicted.
    #print column_to_determine, "$$$$$$$$$$$$$$$$$$$$$$$\n"
    training_df.fillna(0.0, inplace=True) # Fill NaN values with 0
    features.fillna(0.0, inplace=True)
    # ****** Important - Need to sanitize data before going for the next step.
    # Using linear regression now. Will try penalized linear regression and/or logistic linear regression. May try ensemble methods later.
    training_regr = linear_model.LinearRegression()
    try:
        training_regr.fit(features, label)
    except:
        print "LABEL: ", label, "Error: %s"%sys.exc_info()[1].__str__()
        #sys.exit()
    np.set_printoptions(precision=2)
    print "\n############################################################\n"
    # Get the test data in which we will predict the column_to_determine attribute variable ("More-than-usual exercise activity")
    test_df = pd.read_csv(test_file)
    test_features = test_df.drop([column_predictor, column_to_determine], axis=1)
    test_features.fillna(0.0, inplace=True)
    predvals = training_regr.predict(test_features)
    predlist = predvals.tolist()
    for pred in predlist:
        print str(pred)

    # Plot graphs for the 2 selected features:
    prelunchfile = open("/home/supriyo/work/machine_learning/machinelearning/datasets/Diabetes-Data/csv_data_diabetes/Pre-lunch_blood_glucose_measurement.csv", "r")
    prelunchdatalines = prelunchfile.readlines()
    prelunchfile.close()
    prelunchdata = {}
    startrow = 1
    for line in prelunchdatalines:
        if startrow:
            startrow = 0
            continue
        datarows = line.split(",")
        datarowsparts = datarows[0].split("-")
        datarows[0] = datarowsparts[2] + datarowsparts[0] + datarowsparts[1]
        datarowsparts = datarows[1].split(":")
        datarows[1] = datarowsparts[0] + datarowsparts[1]
        """
        datetimestr = datarows[0] + " " + datarows[1]
        print datetimestr, "###############################"
        try:
            datetimeobj = datetime.strptime(datetimestr, "%m-%d-%Y %H:%M")
        except:
            continue
        """
        prelunchdata[datarows[0] + datarows[1]] = datarows[2]
        #print datarows[0] + datarows[1], "##################################"
        #prelunchdata[datetimeobj] = datarows[2]
    postlunchbasefile = open("/home/supriyo/work/machine_learning/machinelearning/datasets/Diabetes-Data/csv_data_diabetes/Post-lunch_blood_glucose_measurement.csv", "r")
    postlunchbaselines = postlunchbasefile.readlines()
    postlunchbasefile.close()
    postlunchdata = {}
    startrow = 1
    for line2 in postlunchbaselines:
        if startrow:
            startrow = 0
            continue
        datarows2 = line2.split(",")
        datarows2parts = datarows2[0].split("-")
        datarows2[0] = datarows2parts[2] + datarows2parts[0] + datarows2parts[1]
        datarows2parts = datarows2[1].split(":")
        datarows2[1] = datarows2parts[0] + datarows2parts[1]
        """
        datetimestr = datarows2[0] + " " + datarows2[1]
        datetimeobj = datetime.strptime(datetimestr, "%m-%d-%Y %H:%M")
        try:
            datetimeobj = datetime.strptime(datetimestr, "%m-%d-%Y %H:%M")
        except:
            continue
        """
        postlunchdata[datarows2[0] + datarows2[1]] = datarows2[2]
        #postlunchdata[datetimeobj] = datarows2[2]
        #print datarows2[0] + datarows2[1], "##################################"

    prelunchxticks = prelunchdata.keys()
    prelunchyticks = []
    for pltick in prelunchxticks:
        plval = prelunchdata[pltick]
        plval = plval.rstrip("\n")
        try:
            plval = float(plval)
        except:
            plval = 0.0
        prelunchyticks.append(plval)
    #### EXPERIMENTAL SEGMENT DATA ####
    prelunchxticks = prelunchxticks[:100]
    prelunchyticks = prelunchyticks[:100]
    #### EXPERIMENTAL DATA ENDS ####
    #print prelunchxticks, "HHHHHHHHHHHHHHHHHHHHHHHHH\n"
    plt.plot(prelunchxticks, prelunchyticks, label="Pre lunch blood glucose", color="red")
    
    postlunchxticks = postlunchdata.keys()
    postlunchyticks = []
    for nphtick in  postlunchxticks:
        nphval = postlunchdata[nphtick]
        nphval = nphval.rstrip("\n")
        try:
            nphval = float(nphval)
        except:
            nphval = 0.0
        postlunchyticks.append(nphval)
    #### EXPERIMENTAL SEGMENT DATA ####
    postlunchxticks = postlunchxticks[:100]
    postlunchyticks = postlunchyticks[:100]
    #### EXPERIMENTAL DATA ENDS ####
    #print postlunchxticks, "GGGGGGGGGGGGGGGGGG\n"
    plt.plot(postlunchxticks, postlunchyticks, label="Post lunch blood glucose measurement", color="blue")
    
    plt.xlabel('time') 
    plt.ylabel('values') 

    plt.legend()
    
    plt.show()
    
#####################
## TO DO: ##
## 1. The date values in X-axis are stored in form of strings. They should be in the form of valid datetime values.
## 2. Need to test more than 100 data sets. With 1000 data sets, the computer at this time freezes and the plots do not appear.

## Author: Supriyo Mitra.


        




   
