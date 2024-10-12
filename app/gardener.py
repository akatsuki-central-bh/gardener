import time
from datetime import datetime

import click

from app.models.routine import Routine

@click.command('init-routines')
def init_routines_command():
  """Initialize routines."""
  click.echo('Initialized routines.')
  while True:
    routines = Routine.all()

    for routine in routines:
      if datetime.now() > routine.next_watering_date():
        routine.execute_watering()

def init_app(app):
  app.cli.add_command(init_routines_command)
