import pymongo
import pandas as pd
import json
#provide te mongodb localost url to connect pyton to mangodb
client=pymongo.MongoClient("mongodb://localhost:27017")

DATA_FILE_PATH="C:/ineuron/fault detection/aps_failure_training_set1.csv"
DATABASE_NAME='aps'
COLLECTION_NAME='sensor'

if __name__=="__main__":
    df=pd.read_csv(DATA_FILE_PATH)
    print(f"row and column:{df.shape}")
    
    
    #convert dataframe to json format -we can dump our dataframe to mongodb
    df.reset_index(drop=True,inplace=True)
    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])
    
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)
    
    