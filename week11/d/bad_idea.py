
class App:
  def __init__(self):
    # พึ่งพา MySQL โดยตรง!
    self.db = MySQLDatabase()

  def get_data(self):
    self.db.query()