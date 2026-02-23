from abc import ABC , abstractmethod

class Database(ABC):
    @abstractmethod
    def save(self, data):
        pass

class MySQLDatabase(Database):
    def save(self, data):
        print(f"Saving data to MySQL: {data}")

class PostgreSQLDatabase(Database):
    def save(self, data):
        print(f"Saving data to PostgreSQL: {data}")

class App:
    def __init__(self, database: Database):
         self.database = database
    def save_data(self, data):
         self.database.save(data)

x = App(MySQLDatabase())
x.save_data("Sample Data")
y = App(PostgreSQLDatabase())
y.save_data("Sample Data")