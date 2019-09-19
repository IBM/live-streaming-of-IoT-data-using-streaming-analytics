import json
import requests
from flask_cors import CORS
import pandas as pd
import os
from flask import Flask, jsonify, json, request

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False
CORS(app)

'''
Different application Ignore this method
'''
def realtime_simulation():
    df = pd.read_excel('Bank_Personal_Loan_Modelling.xlsx','Data')
    df.pop('Personal Loan')
    df.columns = ["ID","Age","Experience","Income","ZIPCode","Family","CCAvg","Education","Mortgage","SecuritiesAccount","CDAccount","Online","CreditCard"]
    df = df.sample()
    out = df.to_json(orient='records')[1:-1].replace('},{', '} {')
    return out

@app.route("/")
def main():
    return realtime_simulation()

port = os.getenv('VCAP_APP_PORT', '8080')
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=port)
