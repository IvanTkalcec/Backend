from flask import Flask, Response, jsonify, request
from domain import Profesori, Ankete,Kolegiji
from  flask_cors import CORS

app = Flask(__name__)
CORS(app)



@app.route('/kolegiji', methods=['GET','POST'])
def handle_kolegiji():
    if request.method == 'GET':
        kolegiji = Kolegiji.listaj()
        return jsonify({"kolegiji": kolegiji })
    elif request.method == 'POST':
        status, greske = Kolegiji.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

    
   

@app.route('/ankete', methods=['GET', 'POST'])
def handle_ankete():
    if request.method == 'GET':
        ankete = Ankete.listaj()
        return jsonify({"ankete": ankete})
    elif request.method == 'POST':
        status, greske = Ankete.dodaj(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r


@app.route('/profesori', methods=['GET', 'PUT','POST'])
def handle_profesori():
    if request.method == 'GET':
        profesori = Profesori.listaj()
        return jsonify({"profesori": profesori})
    elif request.method == 'POST':
        status, greske = Profesori.dodaj(request.get_json())
    elif request.method == 'PUT':
        status, greske = Profesori.update(request.get_json())
        if status:
            return Response(status=201)
        else:
            r = Response(status=500)
            r.set_data(greske)
            return r

if __name__ == '__main__':
    app.debug = True
    app.run()