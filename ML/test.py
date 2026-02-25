import pandas as pd
from tensorflow.keras.models import load_model
import numpy as np
import joblib
def predict():
    ds=joblib.load("ML/ds1.joblib")
    df=pd.read_csv("media/input/test/test.csv")
    print(df)
    df1=df.iloc[:,1:-1]
    print(df1)
    pred=ds.predict(df1)
    print(pred[0])
    if pred[0]==0:
        result="Ready,"
    elif pred[0]==1:
        result="Denial of Service attacks"
    elif pred[0]==2:
        result='Fuzzy'
    elif pred[0]==3:
        result="Revolutions Per Minute"
    elif pred[0]==4:
        result='gear'    
     
    
    return result
#predict()