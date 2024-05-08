import unittest
from DatabaseManager import DatabaseManager
from Database import Database
from Table import Table

class IntegrationTestSelectData(unittest.TestCase):
    def setUp(self):
        self.table = Table(["name", "year"])
        self.database = Database()
        self.database.add_table(self.table, "students")  

        self.manager = DatabaseManager()
        self.manager.add_database(self.database, "school") 
        self.manager.use_database("school")

    def test_select_data(self):
        self.manager.current_database.tables["students"].insert(["Anna", 1])
        studentData = self.manager.current_database.tables["students"].select()

        self.assertEqual(len(studentData), 1)
        self.assertEqual(studentData[0], ("Anna", 1))

if __name__ == "__main__":
    unittest.main()