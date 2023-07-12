from flask import render_template, url_for
from app.frontend import frontendbp

@frontendbp.route('/')
@frontendbp.route('/index')
def index():
    return render_template('index.html', title='Home')

@frontendbp.route('/setparams')
def setparams():
    lattices = [
        {
            "type": "lieb",
            "label": "Lieb Lattice",
            "imagePath": "static/images/LiebLattice.png",
            "apc": 3 # atoms per cell
        },
        {
            "type": "triangular",
            "label": "Triangular Lattice",
            "imagePath": "static/images/TriangularLattice.png",
            "apc": 1 # atom per cell
        },
    ]
    return render_template('setparams.html', title='Set Parameters', lattices=lattices)