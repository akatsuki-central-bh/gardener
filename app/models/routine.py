from app.database.database import get_db

class Routine():
  def __init__(self, id, plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering):
    self.id = id
    self.plant_id = plant_id
    self.nutrient_id = nutrient_id
    self.frequency_per_hour = frequency_per_hour
    self.ppm_quantity = ppm_quantity
    self.last_watering = last_watering

  @classmethod
  def all(cls):
    db = get_db()
    routines = db.execute('SELECT * FROM routines').fetchall()

    return map(lambda routine: Routine(
      id=routine['id'],
      plant_id=routine['plant_id'],
      nutrient_id=routine['nutrient_id'],
      frequency_per_hour=routine['frequency_per_hour'],
      ppm_quantity=routine['ppm_quantity'],
      last_watering=routine['last_watering']
    ), routines)

  @classmethod
  def find(cls, id):
    db = get_db()
    routine = db.execute('SELECT * FROM routines WHERE id = ?', (id,)).fetchone()

    return Routine(
      id=routine['id'],
      plant_id=routine['plant_id'],
      nutrient_id=routine['nutrient_id'],
      frequency_per_hour=routine['frequency_per_hour'],
      ppm_quantity=routine['ppm_quantity'],
      last_watering=routine['last_watering']
    )

  @classmethod
  def create(cls, plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering):
    db = get_db()
    db.execute('INSERT INTO routines (plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering) VALUES (?, ?, ?, ?, ?)', (plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering))
    db.commit()

    return Routine(
      id=db.execute('SELECT last_insert_rowid()').fetchone()['last_insert_rowid()'],
      plant_id=plant_id,
      nutrient_id=nutrient_id,
      frequency_per_hour=frequency_per_hour,
      ppm_quantity=ppm_quantity,
      last_watering=last_watering
    )

  def update(self, plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering):
    db = get_db()
    db.execute('UPDATE routines SET plant_id = ?, nutrient_id = ?, frequency_per_hour = ?, ppm_quantity = ?, last_watering = ? WHERE id = ?', (plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering, self.id))
    db.commit()

    self.plant_id = plant_id
    self.nutrient_id = nutrient_id
    self.frequency_per_hour = frequency_per_hour
    self.ppm_quantity = ppm_quantity
    self.last_watering = last_watering

    return self

  def destroy(self):
    db = get_db()
    db.execute('DELETE FROM routines WHERE id = ?', (self.id,))
    db.commit()

  def plant(self):
    from app.models.plant import Plant

    return Plant.find(self.plant_id)

  def nutrient(self):
    from app.models.nutrient import Nutrient

    return Nutrient.find(self.nutrient_id)

  def save(self):
    db = get_db()
    db.execute('UPDATE routines SET plant_id = ?, nutrient_id = ?, frequency_per_hour = ?, ppm_quantity = ?, last_watering = ? WHERE id = ?', (
      self.plant_id, self.nutrient_id, self.frequency_per_hour, self.ppm_quantity, self.last_watering, self.id)
    )
    db.commit()

    return self
