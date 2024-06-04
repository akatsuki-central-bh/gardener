from app.database.database import get_db
from app.models.routine import Routine

class Plant():
  def __init__(self, id, name, port):
    self.id = id
    self.name = name
    self.port = port

  @classmethod
  def all(cls):
    db = get_db()
    plants = db.execute('SELECT * FROM plants').fetchall()

    return map(lambda plant: Plant(
      id=plant['id'],
      name=plant['name'],
      port=plant['port']
    ), plants)

  @classmethod
  def find(cls, id):
    db = get_db()
    plant = db.execute('SELECT * FROM plants WHERE id = ?', (id,)).fetchone()

    return Plant(
      id=plant['id'],
      name=plant['name'],
      port=plant['port']
    )

  @classmethod
  def create(cls, name, port):
    db = get_db()
    db.execute('INSERT INTO plants (name, port) VALUES (?, ?)', (name, port))
    db.commit()

    return Plant(
      id=db.execute('SELECT last_insert_rowid()').fetchone()['last_insert_rowid()'],
      name=name,
      port=port
    )

  def update(self, name, port):
    db = get_db()
    db.execute('UPDATE plants SET name = ?, port = ? WHERE id = ?', (name, port, self.id))
    db.commit()

    self.name = name
    self.port = port

    return self

  def destroy(self):
    db = get_db()
    db.execute('DELETE FROM plants WHERE id = ?', (self.id,))
    db.commit()

  def routines(self):
    db = get_db()
    routines = db.execute('SELECT * FROM routines WHERE plant_id = ?', (self.id,)).fetchall()

    return map(lambda routine: Routine(
      id=routine['id'],
      plant_id=routine['plant_id'],
      nutrient_id=routine['nutrient_id'],
      frequency_per_hour=routine['frequency_per_hour'],
      ppm_quantity=routine['ppm_quantity'],
      last_watering=routine['last_watering']
    ), routines)
