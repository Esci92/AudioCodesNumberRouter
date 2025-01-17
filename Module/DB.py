import sqlite3

class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_value, traceback):
        self.connection.commit()
        self.connection.close()
        
    
class PhoneNumberManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def insert_phonenumber(self, phonenumber):
        with DatabaseManager(self.db_name) as cursor:
            try:
                cursor.execute("INSERT INTO Phonenumber (number) VALUES (?)", (phonenumber,))
                return f"Success: {phonenumber} added"
            except sqlite3.IntegrityError:
                return f"Error: The {phonenumber} number already exists in the database"

    def select_phonenumber(self, phonenumber=None):
        with DatabaseManager(self.db_name) as cursor:
            if phonenumber is None:
                cursor.execute("SELECT * FROM Phonenumber")
            else:
                cursor.execute("SELECT * FROM Phonenumber WHERE number=?", (phonenumber,))
            return cursor.fetchall()

    def select_phonenumber_id(self, id):
        with DatabaseManager(self.db_name) as cursor:

            cursor.execute("SELECT * FROM Phonenumber WHERE id=?", (id,))
            return cursor.fetchall()

    def delete_phonenumber(self, phonenumber):
        with DatabaseManager(self.db_name) as cursor:
            try:
                cursor.execute("DELETE FROM phonenumber WHERE number=?", (phonenumber,))
                return f"Success: {phonenumber} deleted"
            except sqlite3.IntegrityError:
                return f"Error: {phonenumber} not exists"
                
class TagManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def insert_tag(self, tag, name):
        with DatabaseManager(self.db_name) as cursor:
            try:
                cursor.execute("INSERT INTO Tag (routingtag, name) VALUES (?,?)", (tag,name,))
                return f"Success: {tag} added"
            except sqlite3.IntegrityError:
                return f"Error: The {tag} number already exists in the database"

    def select_tag(self, tag=None):
        with DatabaseManager(self.db_name) as cursor:
            if tag is None:
                cursor.execute("SELECT * FROM Tag")
            else:
                cursor.execute("SELECT * FROM Tag WHERE routingtag=?", (tag,))
            return cursor.fetchall()
        
    def select_tag_id(self, id=None):
        with DatabaseManager(self.db_name) as cursor:
            cursor.execute("SELECT * FROM Tag WHERE id=?", (id,))
            return cursor.fetchall()
        
    def delete_tag(self, id):
        with DatabaseManager(self.db_name) as cursor:
            try:
                cursor.execute("DELETE FROM Tag WHERE id=?", (id,))
                return f"Success: {id} deleted"
            except sqlite3.IntegrityError:
                return f"Error: {id} not exists"
                
class RoutingManager:
    def __init__(self, db_name):
        self.db_name = db_name

    def insert_routing(self, tag_id, number):
        with DatabaseManager(self.db_name) as cursor:
            try:
                cursor.execute("UPDATE Phonenumber SET tag_id = ? WHERE number = ?", (tag_id, number))
                return f"Success: {tag_id} - {number} added"
            except sqlite3.IntegrityError:
                return f"Error: The {tag_id} - {number} number already exists in the database"

    def select_routing(self, number=None):
        with DatabaseManager(self.db_name) as cursor:
            if number is None:
                cursor.execute("SELECT Phonenumber.id, number, routingtag, name FROM Phonenumber LEFT JOIN Tag on Phonenumber.tag_id = Tag.id;")
            else:
                cursor.execute("SELECT Phonenumber.id, number, routingtag, name FROM Phonenumber LEFT JOIN Tag on Phonenumber.tag_id = Tag.id WHERE number=?;", (number,))
            outvar = cursor.fetchall()
            return outvar


    def delete_routing(self, number):
        with DatabaseManager(self.db_name) as cursor:
            cursor.execute("UPDATE Phonenumber SET tag_id = null WHERE number = ?", (number,))
            return f"Success: {number} deleted"

class NewDB:
    def __init__(self, db_name):
        self.db_name = db_name

    def create_tables_if_not_exist(self):
        with DatabaseManager(self.db_name) as cursor:
            try:
                # Begin transaction
                cursor.execute("BEGIN TRANSACTION")
                
                # Create Tag table
                cursor.execute("""CREATE TABLE IF NOT EXISTS Tag(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    routingtag VARCHAR(50) NOT NULL UNIQUE, 
                                    name VARCHAR(25) NOT NULL
                                )""")
                
                # Create Phonenumber table
                cursor.execute("""CREATE TABLE IF NOT EXISTS Phonenumber(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                    number VARCHAR(25) NOT NULL UNIQUE,
                                    tag_id INT 
                                )""")
                
                # Commit transaction
                cursor.execute("COMMIT")
                
            except sqlite3.Error as e:
                # Rollback transaction if there's an error
                cursor.execute("ROLLBACK")
                print("Error:", e)