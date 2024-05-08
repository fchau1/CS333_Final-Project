import unittest
from Table import Table

class UnitTestTable(unittest.TestCase):
    def setUp(self):
        self.table = Table(["name", "year"])

    def test_insert(self):
        self.table.insert(["Anna", 1])
        self.assertEqual(self.table.data["name"], ["Anna"])
        self.assertEqual(self.table.data["year"], [1])
    
    def test_delete(self):
        self.table.insert(["Anna", 1])
        self.table.insert(["Elena", 2])

        condition = lambda data, i: data['year'][i] < 2
        self.table.delete(condition)

        students = self.table.select()
        self.assertEqual(len(students), 1)
        self.assertIn(("Elena", 2), students)

        self.assertNotIn(("Anna", 1), students)

    def test_select(self):
        self.table.insert([1, "Alice"])
        students = self.table.select()
        self.assertEqual(len(students), 1)

if __name__ == "__main__":
    unittest.main()