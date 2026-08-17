import json
import os

FILE_NAME="vault.json"

def initialize():
    #check if file exist or not
    if not os.path.exists(FILE_NAME):
        #create a default structure
        data={
            "master_password":"",
            "data": {}
        }
        with open(FILE_NAME,"w") as f:                  #this use to open a file as file where w-write and r-read
            json.dump(data,f,indent=4)

def load_data():
    with open(FILE_NAME,"r") as f:
        return json.load(f)
    
def save_data(data):
    with open(FILE_NAME,"w") as f:
        json.dump(data,f,indent=4)

