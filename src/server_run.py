# -*- coding: utf-8 -*-
 
from flask import Flask, render_template
from flask import request
from flask import Response
import json
import run_script
 
app = Flask(__name__)
 
def Response_headers(content):
    resp = Response(content)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp
 
@app.route('/')
def hello_world():
    return render_template('index.html')
 
@app.route('/run',methods=['POST'])
def run():
    if request.method == 'POST' and request.json['code']:
        code = request.json['code']
        print(code)
        jsondata = run_script.run_main(code)
        return Response_headers(str(jsondata['output']))
 
if __name__ == '__main__':
    app.run(debug=True)