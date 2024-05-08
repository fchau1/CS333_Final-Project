import unittest
from DatabaseManager import DatabaseManager
from Database import Database
from Table import Table

class test_IntegrationTestInsertData(unittest.TestCase):
    def setUp(self):
        self.table = Table(["name", "year"])
        self.database = Database()
        self.database.add_table(self.table, "Students") 

        self.manager = DatabaseManager()
        self.manager.add_database(self.database, "School")  
        self.manager.use_database("School")

    def test_insert_data(self):
        self.manager.current_database.tables["Students"].insert(["Anna", 1])
        names = self.manager.current_database.tables["Students"].data["name"]
        years = self.manager.current_database.tables["Students"].data["year"]

        self.assertEqual(self.table.data["name"], ["Anna"])
        self.assertEqual(self.table.data["year"], [1])

if __name__ == "__main__":
    unittest.main()

