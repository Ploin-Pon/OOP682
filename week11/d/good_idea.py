
class App:
  # พึ่งพา Abstraction
  def __init__(self, db: DataSource):
    self.db = db

# ส่งสิ่งที่ต้องใช้เข้าไป (Injection)
app = App(MySQLDatabase())
app = App(PostgresDatabase())