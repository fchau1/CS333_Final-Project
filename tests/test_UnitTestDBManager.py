import unittest
from DatabaseManager import DatabaseManager
from Database import Database

class UnitDB1Manager(unittest.TestCase):
    def setUp(self):
        self.manager = DatabaseManager()

        self.database = Database()
        self.manager.add_database(self.database, "DB1")
        self.manager.use_database("DB1")

    def test_add_database(self):
        self.assertIn("DB1", self.manager.databases)
    
    def test_add_taken_database(self):
        self.assertIn("DB1", self.manager.databases)
        self.assertFalse(self.assertIn("DB1", self.manager.databases))

    def test_drop_database(self):
        self.assertIn("DB1", self.manager.databases)

        self.manager.drop_database("DB1")
        self.assertNotIn("DB1", self.manager.databases)
    
    def test_drop_nonExistent_database(self):
        self.assertFalse(self.manager.drop_database("DB2"))

    def test_use_database(self):
        self.manager.use_database("DB1")
        self.assertEqual(self.manager.current_database, self.database)

    def test_use_nonExistent_database(self):
        self.assertFalse(self.manager.use_database("DB2"))

if __name__ == "__main__":
    unittest.main()