import time
from datetime import datetime

import click

from app.models.routine import Routine

def regar(routine):
  plant = routine.plant()
  nutrient = routine.nutrient()

  print(f"Regando planta {plant.name} com {nutrient.name} ({routine.ppm_quantity} ppm)")
  print(f"horario: {datetime.now()} Próxima rega em {routine.frequency_per_hour} horas")
  print("")

@click.command('init-routines')
def init_routines_command():
  """Initialize routines."""
  click.echo('Initialized routines.')
  while True:
    routines = Routine.all()

    for routine in routines:
      ultima_rega = routine.last_watering
      ultima_rega = time.mktime(ultima_rega.timetuple())

      frequencia_por_hora = routine.frequency_per_hour

      if (time.time() - ultima_rega) >= frequencia_por_hora * 3600:
        regar(routine)

        ultima_rega = time.time()

        routine.last_watering = datetime.fromtimestamp(ultima_rega)
        routine.save()

def init_app(app):
  app.cli.add_command(init_routines_command)
