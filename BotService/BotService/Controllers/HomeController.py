
from flask import Blueprint

HomeController = Blueprint('HomeController', __name__)

@HomeController.route('/')
@HomeController.route('/index')
def Home_Index():
    return 'This is Home Index For HomeController'
