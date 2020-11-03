import json
import pandas as pd
import numpy as np
from datetime import datetime
import requests
from tqdm import tqdm

raw_data = pd.read_csv('data.csv')
raw_data = raw_data.replace({np.nan: None})

for i, row in tqdm(raw_data.iterrows()):
    json_obj = json.loads(row.to_json())
    url = "http://127.0.0.1:8000/api/add-booking/"
    x = requests.post(url, data = json_obj)

    if x.status_code == 500 or (i > 30):
        print(row["id"])
        break

