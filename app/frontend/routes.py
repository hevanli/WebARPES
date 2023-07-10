from flask import render_template, url_for
from app.frontend import frontendbp

@frontendbp.route('/')
@frontendbp.route('/index')
def index():
    return render_template('index.html', title='Home')