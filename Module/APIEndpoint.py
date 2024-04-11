from flask import Flask
import Module.API as api
from waitress import serve 

app = Flask(__name__)

# Number Endpoints
@app.route('/api/v1/phonenumber', methods=['GET'])
def endpoint_get_phonenumber():
    return api.get_phonenumber(db)

@app.route('/api/v1/phonenumber', methods=['POST'])
def endpoint_add_phonenumber():
    return api.add_phonenumber(db)

@app.route('/api/v1/phonenumber', methods=['DELETE'])
def endpoint_del_phonenumber():
    return api.del_phonenumber(db)
    
# Number routingtag Endpoints
@app.route('/api/v1/routingtag', methods=['GET'])
def endpoint_get_routingTag():
    return api.get_routingTag(db)
    
@app.route('/api/v1/routingtag', methods=['POST'])
def endpoint_add_routingTag():
    return api.add_routingtag(db)

@app.route('/api/v1/routingtag', methods=['DELETE'])
def endpoint_del_routingTag():
    return api.del_routingtag(db)

# Audiocodes Endpoints
@app.route('/api/v1/audiocodes', methods=['GET'])
def endpoint_get_ac_routing_healht():
    return api.get_ac_routing_healht()

@app.route('/api/v1/audiocodes/<number>', methods=['GET'])
def endpoint_get_ac_routing(number):
    json = api.get_ac_routing(db, number)
    return json.json[0]['RoutingTag']

# Routing Endpoints
@app.route('/api/v1/phonenumber/<number>', methods=['GET'])
def endpoint_get_routing_phone(number):
    return api.get_routing_phone(db, number)

@app.route('/api/v1/phonenumber/<number>', methods=['PUT'])
def endpoint_update_routing(number):
    return api.update_routing(db, number)

def start(DBdata):
    global db
    db = DBdata
    
    # Flask Debup
    # app.run(port=5000)
    serve(app, host='0.0.0.0', port=5000)
