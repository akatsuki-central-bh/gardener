from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from app.models.nutrient import Nutrient

bp = Blueprint('nutrients', __name__)

@bp.route('/nutrients')
def index():
  nutrients = Nutrient.all()

  return render_template('nutrients/index.html', nutrients=nutrients)

@bp.route('/nutrients/create', methods=['GET'])
def new():
  return render_template('nutrients/create.html')

@bp.route('/nutrients/create', methods=['POST'])
def create():
  name = request.form['name']
  port = request.form['port']

  Nutrient.create(name, port)

  return redirect(url_for('nutrients.index'))

@bp.route('/nutrients/<int:id>', methods=['GET'])
def show(id):
  nutrient = Nutrient.find(id)

  return render_template('nutrients/show.html', nutrient=nutrient)

@bp.route('/nutrients/<int:id>/edit', methods=['GET'])
def edit(id):
  nutrient = Nutrient.find(id)

  return render_template('nutrients/edit.html', nutrient=nutrient)

@bp.route('/nutrients/<int:id>/edit', methods=['POST'])
def update(id):
  nutrient = Nutrient.find(id)

  name = request.form['name']
  port = request.form['port']

  nutrient.update(name, port)

  return redirect(url_for('nutrients.index'))

@bp.route('/nutrients/<int:id>/delete', methods=['POST'])
def delete(id):
  nutrient = Nutrient.find(id)

  nutrient.delete()

  return redirect(url_for('nutrients.index'))
