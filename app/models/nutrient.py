from app.database.database import get_db

class Nutrient():
  def __init__(self, id, name, port):
    self.id = id
    self.name = name
    self.port = port

  @classmethod
  def all(cls):
    db = get_db()
    nutrients = db.execute('SELECT * FROM nutrients').fetchall()

    return map(lambda nutrient: Nutrient(
      id=nutrient['id'],
      name=nutrient['name'],
      port=nutrient['port']
    ), nutrients)

  @classmethod
  def find(cls, id):
    db = get_db()
    nutrient = db.execute('SELECT * FROM nutrients WHERE id = ?', (id,)).fetchone()

    return Nutrient(
      id=nutrient['id'],
      name=nutrient['name'],
      port=nutrient['port']
    )

  @classmethod
  def create(cls, name, port):
    db = get_db()
    db.execute('INSERT INTO nutrients (name, port) VALUES (?, ?)', (name, port))
    db.commit()

    return Nutrient(
      id=db.execute('SELECT last_insert_rowid()').fetchone()['last_insert_rowid()'],
      name=name,
      port=port
    )

  def update(self, name, port):
    db = get_db()
    db.execute('UPDATE nutrients SET name = ?, port = ? WHERE id = ?', (name, port, self.id))
    db.commit()

    self.name = name
    self.port = port

    return self

  def destroy(self):
    db = get_db()
    db.execute('DELETE FROM nutrients WHERE id = ?', (self.id,))
    db.commit()
