from flask import request, jsonify
from Module.DB import RoutingManager as RM, TagManager as TM, PhoneNumberManager as PNM
import json

def format_by_indexes(input_list, first_value, secound_value, third_value, forth_value=None):
    json_list = []
    for row in input_list:

        if forth_value != None:
            # Extracting values from tuple
            first_row_value, secound_row_value, third_row_value, forth_row_value = row

            # Creating a dictionary with specified keys
            data = {first_value: first_row_value, secound_value: secound_row_value, third_value: third_row_value, forth_value: forth_row_value}
        else:
            # Extracting values from tuple
            first_row_value, secound_row_value, third_value = row

            # Creating a dictionary with specified keys
            data = {first_value: first_row_value, secound_value: secound_row_value, third_value: third_row_value}

        # Convert the dictionary to JSON and append to the json_list
        json_list.append(data)
    return json_list

def get_phonenumber(db):

    if 'id' in request.json is not None:
        try:
            raw_list = PNM.select_phonenumber_id(db, request.json['id'])
            formated_list = format_by_indexes(raw_list,"id","number","tag_id")
            return jsonify(formated_list) 
        except:
            return jsonify({'error': 'General Error'}), 404
        
    if 'number' in request.json is not None:
        try:
            raw_list = PNM.select_phonenumber(db, request.json['number'])
            formated_list = format_by_indexes(raw_list,"id","number","tag_id")
            return jsonify(formated_list) 
        except:
            return jsonify({'error': 'General Error'}), 404

    try:        
        raw_list = PNM.select_phonenumber(db)
        formated_list = format_by_indexes(raw_list,"id", "number", "tag_id")
        return jsonify(formated_list)
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
            raw_list = TM.select_tag_id(db, request.json['id']) 
            formated_list = format_by_indexes(raw_list,"id","RoutingTag","name")
            return jsonify(formated_list) 
        except:
            return jsonify({'error': 'General Error'}), 404
        
    if 'routingtag' in request.json is not None:
        try:
            raw_list = TM.select_tag(db, request.json['routingtag'])
            formated_list = format_by_indexes(raw_list,"id","RoutingTag","name")
            return jsonify(formated_list) 
        except:
            return jsonify({'error': 'General Error'}), 404    
        
    try:
        raw_list = TM.select_tag(db)
        formated_list = format_by_indexes(raw_list,"id","RoutingTag","name")
        return jsonify(formated_list) 
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

def get_ac_routing(db, number):

    try:
        raw_list = RM.select_routing(db, number)
        formated_list = format_by_indexes(raw_list,"id","number","RoutingTag","name")
        return jsonify(formated_list) 
    except:
        return jsonify({'error': 'General Error'}), 404    

def get_ac_routing_healht():
    return jsonify({'OK': 'Health Check'}), 200    


def get_routing_phone(db, number):
    try:
        raw_list = RM.select_routing(db, number)
        formated_list = format_by_indexes(raw_list,"id","number","RoutingTag","name")
        return jsonify(formated_list) 
    except:
        return jsonify({'error': 'General Error'}), 404
    
def update_routing(db, number):
    try:
        RM.insert_routing(db, request.json['tagid'], number)
        raw_list = RM.select_routing(db, number)
        formated_list = format_by_indexes(raw_list,"id","number","RoutingTag","name")
        return jsonify(formated_list) 
    except:
        return jsonify({'error': 'General Error'}), 404