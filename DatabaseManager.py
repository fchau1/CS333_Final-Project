from Database import Database

class DatabaseManager:

    def __init__(self):
        self.databases = {}
        self.current_database = None

    def add_database(self, database, name):
        if name in self.databases:
            return False
        else:
            self.databases[name] = database

    def drop_database(self, name):
        if name in self.databases:
            del self.databases[name]
        else:
            return False

    def use_database(self, name):
        if name in self.databases:
            self.current_database = self.databases[name]
        else:
            return False
