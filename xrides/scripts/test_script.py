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
    row["online_booking"] = bool(row["online_booking"])
    row["mobile_site_booking"] = bool(row["mobile_site_booking"])
    row["Car_Cancellation"]  = bool(row["Car_Cancellation"])
    del row["id"]
    row["from_date"] = datetime.strptime(row["from_date"], '%d/%m/%Y %H:%M')
    if(row["to_date"]!=None):
        row["to_date"] = datetime.strptime(row["to_date"], '%d/%m/%Y %H:%M')
    row["booking_created"] = datetime.strptime(row["booking_created"], '%d/%m/%Y %H:%M')

    json_obj = json.loads(row.to_json())

    # Make api request
    url = "http://127.0.0.1:8000/api/add-booking/"
    x = requests.post(url, data = json_obj)
    print(x)
    break

