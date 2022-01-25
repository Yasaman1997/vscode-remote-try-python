#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

from flask import Flask
import json
import requests

API_URL = "https://api-inference.huggingface.co/models/gpt2"
headers = {"Authorization": "Bearer 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"}

app = Flask(__name__)

@app.route("/")



def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))

data = query("Can you please let us know more details about your ")
print(data)