from flask import (
  Blueprint, flash, g, redirect, render_template, request, url_for
)

from app.models.nutrient import Nutrient
from app.models.plant import Plant
from app.models.routine import Routine

bp = Blueprint('routines', __name__)

@bp.route('/routines')
def index():
  routines = Routine.all()

  return render_template('routines/index.html', routines=routines)

@bp.route('/routines/create', methods=['GET'])
def new():
  return render_template('routines/create.html')

@bp.route('/routines/create', methods=['POST'])
def create():
  plant_id = request.form['plant_id']
  nutrient_id = request.form['nutrient_id']
  frequency_per_hour = request.form['frequency_per_hour']
  ppm_quantity = request.form['ppm_quantity']
  last_watering = request.form['last_watering']

  Routine.create(plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering)

  return redirect(url_for('routines.index'))

@bp.route('/routines/<int:id>', methods=['GET'])
def show(id):
  routine = Routine.find(id)
  plant = Plant.find(routine.plant_id)
  nutrient = Nutrient.find(routine.nutrient_id)

  return render_template('routines/show.html', routine=routine, plant=plant, nutrient=nutrient)

@bp.route('/routines/<int:id>/edit', methods=['GET'])
def edit(id):
  routine = Routine.find(id)
  plant = Plant.find(routine.plant_id)
  nutrient = Nutrient.find(routine.nutrient_id)

  return render_template('routines/edit.html', routine=routine, plant=plant, nutrient=nutrient)

@bp.route('/routines/<int:id>/edit', methods=['POST'])
def update(id):
  routine = Routine.find(id)

  plant_id = request.form['plant_id']
  nutrient_id = request.form['nutrient_id']
  frequency_per_hour = request.form['frequency_per_hour']
  ppm_quantity = request.form['ppm_quantity']
  last_watering = request.form['last_watering']

  routine.update(plant_id, nutrient_id, frequency_per_hour, ppm_quantity, last_watering)

  return redirect(url_for('routines.index'))

@bp.route('/routines/<int:id>/destroy', methods=['POST'])
def delete(id):
  routine = Routine.find(id)

  routine.destroy()

  return redirect(url_for('routines.index'))
