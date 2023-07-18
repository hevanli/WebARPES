from flask import render_template, url_for, request, redirect, flash
from app.frontend import frontendbp

@frontendbp.route('/')
@frontendbp.route('/index')
def index():
    header= "Hello, Welcome to <span id='main-title'>WebARPES</span>"
    return render_template('index.html', title='Home', header=header)

@frontendbp.route('/setparams', methods=["GET", "POST"])
def setparams():
    if request.method == "POST":
        selected_lattice=request.form['lattices']
        return redirect(url_for('frontend.orbitals', lattice=selected_lattice))

    lattices = [
        {
            "type": "lieb",
            "label": "Lieb Lattice",
            "image": "LiebLattice.png",
            "apc": 3 # atoms per cell
        },
        {
            "type": "triangular",
            "label": "Triangular Lattice",
            "image": "TriangularLattice.png",
            "apc": 1 # atom per cell
        },
        {
            "type": "hexagonal",
            "label": "Hexagonal Lattice",
            "image": "HexagonalLattice.png",
            "apc": 2 # atoms per cell
        },
        {
            "type": "kagome",
            "label": "Kagome Lattice",
            "image": "KagomeLattice.png",
            "apc": 3 # atoms per cell
        }
    ]
    return render_template('setparams.html', title='Set Parameters', lattices=lattices)

@frontendbp.route('/orbitals/<lattice>')
def orbitals(lattice):
    if lattice == "lieb": 
        return render_template('orbitalConfig/lieb.html', title="Lieb Lattice")
    elif lattice == "triangular":
        return render_template('orbitalConfig/triangular.html', title="Triangular Lattice")
    elif lattice == "hexagonal":
        return render_template('orbitalConfig/hexagonal.html', title="Hexagonal Lattice")
    elif lattice == "kagome":
        return render_template('orbitalConfig/kagome.html', title="Kagome Lattice")
    return lattice