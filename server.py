"""
To start server run the following command in the Server directory:

FLASK_APP=server.py flask run
"""

import re
import json
import random
import pandas as pd
from flask import Flask, url_for

# load CSV for use
csv_file = 'static/BookList.csv'
df = pd.read_csv(csv_file)
# remove extra spaces
df.columns = [re.sub(' +', ' ', x.strip()) for x in df.columns]
# generate unique ID for each book
df['ID'] = [random.randrange(10**8) for x in range(0, len(df))]

app = Flask(__name__, static_url_path='/static')

@app.route('/data')
def get_data():
	return json.dumps({
		'columns': list(df.columns),
		'data': json.loads(df.to_json(orient='records'))
	})