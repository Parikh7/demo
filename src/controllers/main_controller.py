from flask import Blueprint, render_template
from src.services.mater_service import materService

main_controller = Blueprint('main_controller', __name__)


@main_controller.route('/')
def index():
    data = materService.get_data()
    return render_template('index.html', data=data)


@main_controller.route("/ping")
def index_ping():
    return "Hello"
