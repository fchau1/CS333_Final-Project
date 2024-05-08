import unittest
from DatabaseManager import DatabaseManager
from Database import Database
from Table import Table

class IntegrationTestSwitchDB(unittest.TestCase):
    def setUp(self):
        self.manager = DatabaseManager()
        self.db1 = Database()
        self.db2 = Database()

        students1 = Table(["name", "year"])
        students2 = Table(["name", "year"])

        self.db1.add_table(students1, "students")
        self.db2.add_table(students2, "students")

        self.manager.add_database(self.db1, "DB1")
        self.manager.add_database(self.db2, "DB2")

    def test_switching_databases(self):
        self.manager.use_database("DB1")
        self.manager.current_database.tables["students"].insert(["Anna", 1])

        self.manager.use_database("DB2")
        self.assertEqual(self.manager.current_database.tables["students"].select(), [])

        self.manager.current_database.tables["students"].insert(["Elena", 2])
        studentData = self.manager.current_database.tables["students"].select()
        self.assertEqual(studentData[0],("Elena", 2))

        self.manager.use_database("DB1")
        studentData = self.manager.current_database.tables["students"].select()
        self.assertEqual(studentData[0],("Anna", 1))

if __name__ == "__main__":
    unittest.main()