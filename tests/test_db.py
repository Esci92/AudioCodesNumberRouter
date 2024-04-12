import os
import pytest
from Module.DB import RoutingManager as RM, TagManager as TM, PhoneNumberManager as PNM, NewDB

@pytest.fixture

# Phonenumber Table
def db_phone_manager():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    # Initialize PhoneNumberManager with the created database
    db_phone_manager = PNM(db_name)

    yield db_phone_manager

    # Clean up resources after testing
    db_phone_manager = None
    os.remove(db_name)

def test_db_insert_phonenumber(db_phone_manager):
    # Test inserting a phone number
    result = db_phone_manager.insert_phonenumber("+123456789")
    print(result)
    assert result == "Success: +123456789 added"

def test_db_select_phonenumber(db_phone_manager):
    # Test selecting a phone number that exists
    db_phone_manager.insert_phonenumber("+1234567891")
    result = db_phone_manager.select_phonenumber("+1234567891")
    print(result)
    assert len(result) == 1
    assert result[0][1] == "+1234567891"

def test_db_delete_phonenumber(db_phone_manager):
    # Test deleting a phone number that doesn't exist
    result = db_phone_manager.delete_phonenumber("+123456789")
    assert result == "Success: +123456789 deleted"

# Tag Table
@pytest.fixture
def db_tag_manager():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    # Initialize PhoneNumberManager with the created database
    db_tag_manager = TM(db_name)

    yield db_tag_manager

    # Clean up resources after testing
    db_tag_manager = None
    os.remove(db_name)

    # Test inserting a phone number
def test_db_Insert_Tag(db_tag_manager):
    result = db_tag_manager.insert_tag("TagAvaya", "Avaya")
    print(f"{result}")
    assert result =="Success: TagAvaya added"

def test_db_select_Tag(db_tag_manager):
    # Test selecting a tag that exists
    db_tag_manager.insert_tag("TagAC", "AC")
    result = db_tag_manager.select_tag("TagAC")
    print(result)
    assert len(result) == 1
    assert result[0][1] == "TagAC"

def test_db_del_Tag(db_tag_manager):

    # Test deleting a tag
    result = db_tag_manager.insert_tag("TagAC", "AC")
    result = db_tag_manager.select_tag("TagAC")

    result = db_tag_manager.delete_tag(result[0][0])
    print(result)
    assert result == "Success: 1 deleted"

# Routing
@pytest.fixture
def manager():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    # Initialize PhoneNumberManager with the created database
    routing_manager = RM(db_name)
    db_phone_manager = PNM(db_name)
    db_tag_manager = TM(db_name)

    yield db_tag_manager, db_phone_manager, routing_manager

    # Clean up resources after testin
    routing_manager = None
    db_phone_manager = None
    db_tag_manager = None
    os.remove(db_name)

def test_db_Insert_Routing(manager):
    db_tag_manager = manager[0]
    db_phone_manager = manager[1]
    routing_manager = manager[2]

    # Test inserting a Tag
    result = db_tag_manager.insert_tag("TagAvaya", "Avaya")
    print(f"{result}")
    assert result =="Success: TagAvaya added"

    # Test inserting a phone number
    result = db_phone_manager.insert_phonenumber("+123456789")
    print(result)
    assert result == "Success: +123456789 added"

    # Test inserting a routing_manager
    result = routing_manager.insert_routing(1,"+123456789")
    print(result)
    assert result == "Success: 1 - +123456789 added"

    # Test inserting a routing_manager
    result = routing_manager.select_routing("+123456789")
    print(result)
    assert f"{result[0]}" == "(1, '+123456789', 'TagAvaya', 'Avaya')"

def test_db_delete_Routing(manager):
    db_tag_manager = manager[0]
    db_phone_manager = manager[1]
    routing_manager = manager[2]

    # Test inserting a Tag
    result = db_tag_manager.insert_tag("TagAvaya", "Avaya")
    print(f"{result}")
    assert result =="Success: TagAvaya added"

    # Test inserting a phone number
    result = db_phone_manager.insert_phonenumber("+123456789")
    print(result)
    assert result == "Success: +123456789 added"

    # Test inserting a routing_manager
    result = routing_manager.insert_routing("","+123456789")
    print(result)
    assert result == "Success:  - +123456789 added"

    # Test inserting a routing_manager
    result = routing_manager.select_routing("+123456789")
    print(result)
    assert f"{result[0]}" == "(1, '+123456789', None, None)"
