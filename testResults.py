import numpy as np
import pandas as pd

"""
These functions are used to test the results of the predictions of any model we use
"""


# These functions expect dataframes as an input type ( datafram of Prediction, dataframe of Actual results )


"""
Mean Squared Error
"""
def MSE(predict, actual):
    n = len(predict)
    result = sum((actual - predict)^2)
    return result / n
"""
Root Mean Squared Error
"""
def RMSE(predict, actual):
    return np.sqrt(MSE(predict,actual))

"""
Missclassification Rate
"""
def MisclassificationRate(predict, actual):
    n = len(predict)
    result = sum(predict != actual)
    return result / n

"""
Matthews Correlation Coefficient
"""
def MCC(predict, actual):
    n = len(predict)
    TP, TN, FP, FN = 0

    if predict == 0 and actual == 0 :
        TP+=1
    elif predict == 0 and actual == 1:
        FP+=1
    elif predict == 1 and actual == 0:
        FN+=1
    else:
        TN+=1

    top = (TP*TN) - (FP*FN)
    bottom = np.sqrt( (TP+FP)*(TP+FN)*(TN+FP)*(TN+FN) )

    if bottom == 0:
        return -1
    
    return top / bottom
