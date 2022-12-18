import pymongo
import pandas as pd
import json


# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

Data_File_path="/config/workspace/aps_failure_training_set1.csv"
Data= 'aps'
Collection_Name= 'sensor'

if __name__=='__main__':
    df=pd.read_csv(Data_File_path)
    print(f"Rows and columns:{df.shape}")

    #Covert dataframe from csv to json to dump into MongoDb
    df.reset_index(drop=True, inplace= True)

    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record)

    client[Data][Collection_Name].insert_many(json_record)