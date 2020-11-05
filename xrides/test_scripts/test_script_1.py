import json
import pandas as pd
import numpy as np
from datetime import datetime
import requests
from tqdm import tqdm

url = "http://127.0.0.1:8000/api/bookings/"
x = requests.get(url)
x = x.json()
print(len(x))