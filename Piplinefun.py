import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
import plotly.express as px
import datetime
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

class Student_Performance:

    def __init__(self):
        pass

    def Data_Clean(self,df):

        df.drop_duplicates(inplace=True)

        df.columns = [i.lower() for i in df.columns]

        for i in df.columns:
            if df[i].dtype == 'object':
                df[i] = df[i].str.lower()
        
        df.attendance_rate = df.attendance_rate.astype('int64')

        return df
