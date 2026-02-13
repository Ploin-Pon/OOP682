
class App:
   def __init__(self):
      self.database = MySQLDatabase()
   def save_data(self, data):
      self.database.save(data)

class MySQLDatabase:
   def save(self, data):
      print(f"Saving data to MySQL: {data}")

app = App()
app.save_data("Sample Data")