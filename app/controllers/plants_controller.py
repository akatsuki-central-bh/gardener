from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.models.plant import Plant

bp = Blueprint('plants', __name__)

@bp.route('/plants')
def index():
  plants = Plant.all()

  return render_template('plants/index.html', plants=plants)

@bp.route('/plants/create', methods=['GET'])
def new():
  return render_template('plants/create.html')

@bp.route('/plants/create', methods=['POST'])
def create():
  plant_name = request.form['name']
  plant_port = request.form['port']

  Plant.create(plant_name, plant_port)

  return redirect(url_for('plants.index'))

@bp.route('/plants/<int:id>', methods=['GET'])
def show(id):
  plant = Plant.find(id)
  routines = plant.routines()

  return render_template('plants/show.html', plant=plant, routines=routines)

@bp.route('/plants/<int:id>/edit', methods=['GET'])
def edit(id):
  plant = Plant.find(id)

  return render_template('plants/edit.html', plant=plant)

@bp.route('/plants/<int:id>/edit', methods=['POST'])
def update(id):
  plant = Plant.find(id)

  plant_name = request.form['name']
  plant_port = request.form['port']

  plant.update(plant_name, plant_port)

  return redirect(url_for('plants.index'))

@bp.route('/plants/<int:id>/delete', methods=['POST'])
def delete(id):
  plant = Plant.find(id)

  plant.delete()

  return redirect(url_for('plants.index'))
