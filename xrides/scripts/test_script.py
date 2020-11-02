import json
import pandas as pd
import numpy as np
from datetime import datetime
import requests

raw_data = pd.read_csv('data.csv')
raw_data = raw_data.replace({np.nan: None})

for i, row in raw_data.iterrows():

    # Parse the row data
    row["uuid"] = row["id"]
    del row["id"]
    json_obj = json.loads(row.to_json())

    # Make api request
    url = "http://127.0.0.1:8000/api/add-booking/"
    x = requests.post(url, data = json_obj)
    print(x)
    break

