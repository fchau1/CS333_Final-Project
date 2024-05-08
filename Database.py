from Table import Table

class Database:
    def __init__(self):
        self.tables = {}

    def add_table(self, table, name):
        if name in self.tables:
            return False
        else:
            self.tables[name] = table

    def drop_table(self, name):
        if name in self.tables:
            del self.tables[name]
        else:
            return False
