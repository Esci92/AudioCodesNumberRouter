from flask import request, jsonify
from Module.DB import RoutingManager as RM, TagManager as TM, PhoneNumberManager as PNM


def get_phonenumber(db):

    if 'id' in request.json is not None:
        try:
            return jsonify(PNM.select_phonenumber_id(db, request.json['id'])) 
        except:
            return jsonify({'error': 'General Error'}), 404
        
    if 'number' in request.json is not None:
        try:
            return jsonify(PNM.select_phonenumber(db, request.json['number'])) 
        except:
            return jsonify({'error': 'General Error'}), 404

    try:
        return jsonify(PNM.select_phonenumber(db)) 
    except:
        return jsonify({'error': 'General Error'}), 404

def add_phonenumber(db):
    try:
        dbresponse = PNM.insert_phonenumber(db, request.json['number'])
        return jsonify({'message': f'{dbresponse}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def del_phonenumber(db):

    if 'number' in request.json is not None:
        try:
            dbresponse = PNM.delete_phonenumber(db, request.json['number'])
            return jsonify({'message': f'{dbresponse}'})
        except:
            return jsonify({'error': 'General Error'}), 404

    return jsonify({'error': 'No Number provided'}), 406

        
def get_routingTag(db):
    
    if 'id' in request.json is not None:
        try:
            return jsonify(TM.select_tag_id(db, request.json['id'])) 
        except:
            return jsonify({'error': 'General Error'}), 404
        
    if 'routingtag' in request.json is not None:
        try:
            return jsonify(TM.select_tag(db, request.json['routingtag'])) 
        except:
            return jsonify({'error': 'General Error'}), 404    
        
    try:
        return jsonify(TM.select_tag(db))
    except:
        return jsonify({'error': 'General Error'}), 404
    
def add_routingtag(db):
    try:
        dbresponse = TM.insert_tag(db, request.json['routingtag'], request.json['name'])
        return jsonify({'message': f'{dbresponse}'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

def del_routingtag(db):

    if 'id' in request.json is not None:
        try:
            dbresponse = TM.delete_tag(db, request.json['id'])
            return jsonify({'message': f'{dbresponse}'})
        except:
            return jsonify({'error': 'General Error'}), 404

    return jsonify({'error': 'Wrongdata provided'}), 400

def get_ac_routing(db):
    
    if 'number' in request.json is not None:
        try:
            return jsonify(RM.select_routing(db, request.json['number'])) 
        except:
            return jsonify({'error': 'General Error'}), 404    
        
    try:
        return jsonify(RM.select_routing(db))
    except:
        return jsonify({'error': 'General Error'}), 404