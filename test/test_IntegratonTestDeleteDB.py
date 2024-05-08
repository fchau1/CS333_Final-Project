import unittest
from DatabaseManager import DatabaseManager
from Database import Database
from Table import Table

class IntegrationTestDeleteDatabase(unittest.TestCase):
    def setUp(self):
        self.manager = DatabaseManager()
        self.database = Database()
        
        self.table = Table(["name", "year"])

        self.database.add_table(self.table, "students")

        self.manager.add_database(self.database, "school")
        self.manager.use_database("school")

        self.manager.current_database.tables["students"].insert(["Anna", 1])
        self.manager.current_database.tables["students"].insert(["Elena", 3])

    def test_delete_database(self):
        self.assertIn("school", self.manager.databases)
        self.manager.drop_database("school")
        self.assertNotIn("school", self.manager.databases)

if __name__ == "__main__":
    unittest.main()
