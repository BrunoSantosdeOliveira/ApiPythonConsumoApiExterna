from flask import Flask,Response
import requests

app = Flask(__name__)

viacep = "https://viacep.com.br/ws/13467275/json/"

@app.route('/test', methods= ['GET'])
def getsest():
    response= requests.get(viacep)
    return Response(response)

app.run()
