import os
import pytest
from Module.DB import TagManager as TM, NewDB

@pytest.fixture
def tag_manager():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    # Initialize PhoneNumberManager with the created database
    tag_manager = TM(db_name)

    yield tag_manager

    # Clean up resources after testing
    tag_manager = None
    os.remove(db_name)

def test_Insert_Tag(tag_manager):
    # Test inserting a phone number
    result = tag_manager.insert_tag("TagAvaya", "Avaya")
    print(f"{result}")
    assert result =="Success: TagAvaya added"

def test_select_Tag(tag_manager):
    # Test selecting a tag that exists
    tag_manager.insert_tag("TagAC", "AC")
    result = tag_manager.select_tag("TagAC")
    print(result)
    assert len(result) == 1
    assert result[0][1] == "TagAC"

def test_del_Tag(tag_manager):
    # Test deleting a tag
    result = tag_manager.insert_tag("TagAC", "AC")
    result = tag_manager.select_tag("TagAC")

    result = tag_manager.delete_tag(result[0][0])
    print(result)
    assert result == "Success: 1 deleted"