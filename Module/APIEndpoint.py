from flask import Flask
import Module.API as api

app = Flask(__name__)

# Number Endpoints
@app.route('/api/v1/phonenumber', methods=['GET'])
def endpoint_get_phonenumber():
    return api.get_phonenumber(db)

@app.route('/api/v1/phonenumber', methods=['PUT'])
def endpoint_add_phonenumber():
    return api.add_phonenumber(db)

@app.route('/api/v1/phonenumber', methods=['DELETE'])
def endpoint_del_phonenumber():
    return api.del_phonenumber(db)
    
# Number routingtag Endpoints
@app.route('/api/v1/routingtag', methods=['GET'])
def endpoint_get_routingTag():
    return api.get_routingTag(db)
    
@app.route('/api/v1/routingtag', methods=['PUT'])
def endpoint_add_routingTag():
    return api.add_routingtag(db)

@app.route('/api/v1/routingtag', methods=['DELETE'])
def endpoint_del_routingTag():
    return api.del_routingtag(db)

# Audiocodes Endpoints
@app.route('/api/v1/audiocodes', methods=['GET'])
def endpoint_get_ac_routing():
    return api.get_ac_routing(db)

def start(DBdata):
    global db
    db = DBdata
    
    app.run(debug=True, port=5000)