import os, threading, pytest, requests, json
import Module.APIEndpoint as aep
from Module.DB import NewDB


def ApiConnect(APIEndpoint, body, method):
    url = f"http://192.168.10.122:5000{APIEndpoint}"

    payload = json.dumps(body)

    headers = {
    'Content-Type': 'application/json'
    }

    APIResponse = requests.request(method, url, headers=headers, data=payload)

    return APIResponse

@pytest.fixture(scope='module')
def api():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    NewDB.create_tables_if_not_exist(new_db)

    server_thread = threading.Thread(target=aep.start, args=(new_db, True,))
    server_thread.daemon = True
    server_thread.start()

    yield
    
    server_thread.join(timeout=0)
        
    # Clean up resources after testin
    os.remove(db_name)
    exit()

# Phonenumber
def test_endpoint_get_phonenumber(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/phonenumber",{},"GET")
    assert response.status_code == 200
    assert response.text == '[]\n'

def test_endpoint_add_phonenumber(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/phonenumber",{"number": "+123456789"},"POST")
    assert response.status_code == 200
    assert response.text == '{"message":"Success: +123456789 added"}\n'
    
    # verify
    response = ApiConnect("/api/v1/phonenumber",{},"GET")
    assert response.status_code == 200
    assert response.text == '[{"id":1,"number":"+123456789","tag_id":null}]\n'

def test_endpoint_get_phonenumber_id(api):    
    # verify
    response = ApiConnect("/api/v1/phonenumber",{"id": "1"},"GET")
    assert response.status_code == 200
    assert response.text == '[{"id":1,"number":"+123456789","tag_id":null}]\n'

def test_endpoint_get_phonenumber_nummber(api):    
    # verify
    response = ApiConnect("/api/v1/phonenumber",{"number": "+123456789"},"GET")
    assert response.status_code == 200
    assert response.text == '[{"id":1,"number":"+123456789","tag_id":null}]\n'

def test_endpoint_del_phonenumber(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/phonenumber",{"number": "+123456789"},"DELETE")
    assert response.status_code == 200
    assert response.text == '{"message":"Success: +123456789 deleted"}\n'

    # verify
    response = ApiConnect("/api/v1/phonenumber",{},"GET")
    assert response.status_code == 200
    assert response.text == '[]\n'

# RoutingTag
def test_endpoint_get_routingtag(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/routingtag",{},"GET")
    assert response.status_code == 200
    assert response.text == '[]\n'

def test_endpoint_add_routingtag(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/routingtag",{"routingtag":"TagAvaya", "name":"Avaya"},"POST")
    assert response.status_code == 200
    assert response.text == '{"message":"Success: TagAvaya added"}\n'
    
    # verify
    response = ApiConnect("/api/v1/routingtag",{},"GET")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":"TagAvaya","id":1,"name":"Avaya"}]\n'

def test_endpoint_get_routingtag_id(api):    
    # verify
    response = ApiConnect("/api/v1/routingtag",{"id": "1"},"GET")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":"TagAvaya","id":1,"name":"Avaya"}]\n'

def test_endpoint_get_routingtag_tag(api):    
    # verify
    response = ApiConnect("/api/v1/routingtag",{"routingTag":"TagAvaya"},"GET")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":"TagAvaya","id":1,"name":"Avaya"}]\n'

def test_endpoint_del_routingtag(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/routingtag",{"id": "1"},"DELETE")
    assert response.status_code == 200
    assert response.text == '{"message":"Success: 1 deleted"}\n'

    # verify
    response = ApiConnect("/api/v1/routingtag",{},"GET")
    assert response.status_code == 200
    assert response.text == '[]\n'


def test_endpoint_update_routing(api):
    # Test inserting phonenumber
    response = ApiConnect("/api/v1/phonenumber",{"number": "+123456789"},"POST")
    assert response.status_code == 200
    assert response.text == '{"message":"Success: +123456789 added"}\n'
    
    # verify
    response = ApiConnect("/api/v1/phonenumber",{},"GET")
    assert response.status_code == 200
    assert response.text == '[{"id":2,"number":"+123456789","tag_id":null}]\n'

    # Test inserting a Tag
    response = ApiConnect("/api/v1/routingtag",{"routingtag":"TagAvaya", "name":"Avaya"},"POST")
    assert response.status_code == 200
    assert response.text == '{"message":"Success: TagAvaya added"}\n'
    
    # verify
    response = ApiConnect("/api/v1/routingtag",{},"GET")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":"TagAvaya","id":2,"name":"Avaya"}]\n'

    # Test get routingtag
    response = ApiConnect("/api/v1/phonenumber/+123456789",{"tagid": "2"},"PUT")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":"TagAvaya","id":2,"name":"Avaya","number":"+123456789"}]\n'

def test_endpoint_update_routing_del(api):
    # Test get routingtag
    response = ApiConnect("/api/v1/phonenumber/+123456789",{"tagid": ""},"PUT")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":null,"id":2,"name":null,"number":"+123456789"}]\n'

def test_endpoint_update_routing_add(api):
    # Test get routingtag
    response = ApiConnect("/api/v1/phonenumber/+123456789",{"tagid": "2"},"PUT")
    assert response.status_code == 200
    assert response.text == '[{"RoutingTag":"TagAvaya","id":2,"name":"Avaya","number":"+123456789"}]\n'


# Audiocodes
def test_endpoint_audiocodes_healthcheck(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/audiocodes",{},"GET")
    assert response.status_code == 200
    assert response.text == '{"OK":"Health Check"}\n'

def test_endpoint_audiocodes(api):
    # Test inserting a Tag
    response = ApiConnect("/api/v1/audiocodes/+123456789",{},"GET")
    assert response.status_code == 200
    assert response.text == 'TagAvaya'
