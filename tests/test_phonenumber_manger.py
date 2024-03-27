import os
import pytest
from Module.DB import PhoneNumberManager as PNM, NewDB

@pytest.fixture
def phone_manager():
    # Create a temporary SQLite database for testing
    db_name = "test.db"

    # Initialize the database and create necessary tables
    new_db = NewDB(db_name)
    new_db.create_tables_if_not_exist()

    # Initialize PhoneNumberManager with the created database
    phone_manager = PNM(db_name)

    yield phone_manager

    # Clean up resources after testing
    phone_manager = None
    os.remove(db_name)

def test_insert_phonenumber(phone_manager):
    # Test inserting a phone number
    result = phone_manager.insert_phonenumber("+123456789")
    print(result)
    assert result == "Success: +123456789 added"

def test_select_phonenumber(phone_manager):
    # Test selecting a phone number that exists
    phone_manager.insert_phonenumber("+1234567891")
    result = phone_manager.select_phonenumber("+1234567891")
    print(result)
    assert len(result) == 1
    assert result[0][1] == "+1234567891"

# def test_select_phonenumber_all(phone_manager):
#     result = phone_manager.select_phonenumber()
#     print(result)
#     assert len(result) == 2

def test_delete_phonenumber(phone_manager):
    # Test deleting a phone number that doesn't exist
    result = phone_manager.delete_phonenumber("+123456789")
    assert result == "Success: +123456789 deleted"
