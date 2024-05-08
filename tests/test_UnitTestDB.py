import unittest
from Database import Database
from Table import Table

class UnitTestDB(unittest.TestCase):
    def setUp(self):
        self.database = Database()

    def test_add_table(self):
        students = Table(["name", "year"])
        self.database.add_table(students, "students")
        self.assertIn("students", self.database.tables)
    
    def test_add_taken_table(self):
        students = Table(["name", "year"])
        self.database.add_table(students, "students")
        self.assertFalse(self.database.add_table(students, "students"))

    def test_drop_existing_table(self):
        students = Table(["name", "year"])
        self.database.add_table(students, "students")

        self.database.drop_table("students")
        self.assertNotIn("students", self.database.tables)
    
    def test_drop_nonExistent_table(self):
        self.assertFalse(self.database.drop_table("teachers"))

if __name__ == "__main__":
    unittest.main()