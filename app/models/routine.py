from app.database.database import get_db

class Routine():
  def __init__(self, id, plant_id, nutrient_id, watering_interval_days, on_duration, last_watering):
    self.id = id
    self.plant_id = plant_id
    self.nutrient_id = nutrient_id
    self.watering_interval_days = watering_interval_days
    self.on_duration = on_duration
    self.last_watering = last_watering

  @classmethod
  def all(cls):
    db = get_db()
    routines = db.execute('SELECT * FROM routines').fetchall()

    return map(lambda routine: Routine(
      id=routine['id'],
      plant_id=routine['plant_id'],
      nutrient_id=routine['nutrient_id'],
      watering_interval_days=routine['watering_interval_days'],
      on_duration=routine['on_duration'],
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
      watering_interval_days=routine['watering_interval_days'],
      on_duration=routine['on_duration'],
      last_watering=routine['last_watering']
    )

  @classmethod
  def create(cls, plant_id, nutrient_id, watering_interval_days, on_duration, last_watering):
    db = get_db()
    db.execute('INSERT INTO routines (plant_id, nutrient_id, watering_interval_days, on_duration, last_watering) VALUES (?, ?, ?, ?, ?)', (
      plant_id, nutrient_id, watering_interval_days, on_duration, last_watering)
    )
    db.commit()

    return Routine(
      id=db.execute('SELECT last_insert_rowid()').fetchone()['last_insert_rowid()'],
      plant_id=plant_id,
      nutrient_id=nutrient_id,
      watering_interval_days=watering_interval_days,
      on_duration=on_duration,
      last_watering=last_watering
    )

  def update(self, plant_id, nutrient_id, watering_interval_days, on_duration, last_watering):
    db = get_db()
    db.execute('UPDATE routines SET plant_id = ?, nutrient_id = ?, watering_interval_days = ?, on_duration = ?, last_watering = ? WHERE id = ?', (
      plant_id, nutrient_id, watering_interval_days, on_duration, last_watering, self.id)
    )
    db.commit()

    self.plant_id = plant_id
    self.nutrient_id = nutrient_id
    self.watering_interval_days = watering_interval_days
    self.on_duration = on_duration
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
    db.execute('UPDATE routines SET plant_id = ?, nutrient_id = ?, watering_interval_days = ?, on_duration = ?, last_watering = ? WHERE id = ?', (
      self.plant_id, self.nutrient_id, self.watering_interval_days, self.on_duration, self.last_watering, self.id)
    )
    db.commit()

    return self
