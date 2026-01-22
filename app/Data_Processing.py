import pandas
from numpy import inf
from models import validate_df

def risk_level(df:pandas.DataFrame):
    df["risk_level"] = pandas.cut(df["range_km"],bins=[0,20,100,300,inf],labels=["low","medium","high","extreme"])
    return df

def manufacturer(df:pandas.DataFrame):
    df["manufacturer"] = df["manufacturer"].fillna(value="Unknown") 
    return df


def get_df(file):
    df =  pandas.read_csv(file)
    df = risk_level(df)
    df = manufacturer(df)
    df = validate_df(df)
    return df

