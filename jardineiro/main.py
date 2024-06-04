import time
import sqlite3
from datetime import datetime

conn = sqlite3.connect('instance/flaskr.sqlite')
cursor = conn.cursor()
cursor.execute('SELECT * FROM rotinas')

rows = cursor.fetchall()

# rows[0][0] -> id
# rows[0][1] -> planta_id
# rows[0][2] -> nutriente_id
# rows[0][3] -> frequencia_por_hora
# rows[0][4] -> quantidade_ppm
# rows[0][5] -> ultima_rega

while True:
  for row in rows:
    frequencia_por_hora = row[3]
    regar_tempo = row[3]
    ultima_rega = row[5]

    ultima_rega = time.mktime(datetime.strptime(ultima_rega, "%Y-%m-%d %H:%M:%S").timetuple())

    if (time.time() - ultima_rega) >= frequencia_por_hora * 3600:
      print("Regar")

      print(time.time())
      print(ultima_rega)

      ultima_rega = time.time()
      # cursor.execute('UPDATE rotinas SET ultima_rega = ? WHERE id = ?', (
      #   datetime.datetime.fromtimestamp(ultima_rega), row[0])
      # )

  # if(frequencia_por_hora - regar_tempo) >= regar_tempo:
  #   print("Regar")
  #   frequencia_por_hora = regar_tempo
