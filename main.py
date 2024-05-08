from DatabaseManager import DatabaseManager
from Database import Database
from Table import Table

if __name__ == "__main__":
    print("Welcome to my CS333 Final Project")
    table = Table(["name", "year"])
    database = Database()
    database.add_table(table, "Students") 

    manager = DatabaseManager()
    manager.add_database(database, "School")  
    manager.use_database("School")

    manager.current_database.tables["Students"].insert(["Anna", 1])
    print(manager.current_database.tables["Students"].select())