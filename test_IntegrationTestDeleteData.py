import unittest
from DatabaseManager import DatabaseManager
from Database import Database
from Table import Table

class IntegrationTestDeleteData(unittest.TestCase):
    def setUp(self):
        self.table = Table(["name", "year"])
        self.database = Database()
        self.database.add_table(self.table, "students")

        self.manager = DatabaseManager()
        self.manager.add_database(self.database, "school") 
        self.manager.use_database("school")

        self.manager.current_database.tables["students"].insert(["Alice", 1])
        self.manager.current_database.tables["students"].insert(["Bob", 4])

    def test_delete_data(self):
        condition = lambda data, i: data['year'][i] < 3
        self.manager.current_database.tables["students"].delete(condition)
        upperClassmen = self.manager.current_database.tables["students"].select()

        self.assertEqual(len(upperClassmen), 1) 
        self.assertListEqual(upperClassmen, [("Bob", 4)])

if __name__ == "__main__":
    unittest.main()


