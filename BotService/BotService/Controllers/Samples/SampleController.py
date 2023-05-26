"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template # 渲染模板

from flask import Blueprint

SampleController = Blueprint('SampleController', __name__)

@SampleController.route('/')
@SampleController.route('/index')
def Sample_Index():
    return 'This is Home Index For SampleController'


#def home():
#    """Renders the home page."""
#    return render_template(
#        'index.html',
#        title='Home Page',
#        year=datetime.now().year,
#    )

#@SampleController.route('/contact')
#def contact():
#    """Renders the contact page."""
#    return render_template(
#        'contact.html',
#        title='Contact',
#        year=datetime.now().year,
#        message='Your contact page.'
#    )

#@SampleController.route('/about')
#def about():
#    """Renders the about page."""
#    return render_template(
#        'about.html',
#        title='About',
#        year=datetime.now().year,
#        message='Your application description page.'
#    )
