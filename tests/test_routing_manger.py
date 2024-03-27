import os
import pytest
from Module.DB import RoutingManager as RM, TagManager as TM, PhoneNumberManager as PNM, NewDB

@pytest.fixture
def manager():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    # Initialize PhoneNumberManager with the created database
    routing_manager = RM(db_name)
    phone_manager = PNM(db_name)
    tag_manager = TM(db_name)

    yield tag_manager, phone_manager, routing_manager

    # Clean up resources after testin
    routing_manager = None
    phone_manager = None
    tag_manager = None
    os.remove(db_name)

def test_Insert_Routing(manager):

    tag_manager = manager[0]
    phone_manager = manager[1]
    routing_manager = manager[2]

    # Test inserting a Tag
    result = tag_manager.insert_tag("TagAvaya", "Avaya")
    print(f"{result}")
    assert result =="Success: TagAvaya added"

    # Test inserting a phone number
    result = phone_manager.insert_phonenumber("+123456789")
    print(result)
    assert result == "Success: +123456789 added"

    # Test inserting a routing_manager
    result = routing_manager.insert_routing(1,1)
    print(result)
    assert result == "Success: 1 - 1 added"

# def test_select_routing(manager):

#     tag_manager = manager[0]
#     phone_manager = manager[1]
#     routing_manager = manager[2]

#     # Test inserting a Tag
#     tag_manager.insert_tag("TagAvaya", "Avaya")
#     phone_manager.insert_phonenumber("+123456789")

#     # Test inserting a routing_manager
#     result = routing_manager.select_routing(1,1)
#     print(result)
#     assert result == "[(1, 1, 1)]"

# def test_select_Tag(tag_manager):
#     # Test selecting a tag that exists
#     tag_manager.insert_tag("TagAC", "AC")
#     result = tag_manager.select_tag("TagAC")
#     print(result)
#     assert len(result) == 1
#     assert result[0][1] == "TagAC"

# def test_del_Tag(tag_manager):
#     # Test deleting a tag
#     result = tag_manager.insert_tag("TagAC", "AC")
#     result = tag_manager.select_tag("TagAC")

#     result = tag_manager.delete_tag(result[0][0])
#     print(result)
#     assert result == "Success: 1 deleted"

#     routing_id
#     Phonenumber_id