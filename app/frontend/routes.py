from flask import render_template, url_for, request, redirect, flash
from app.frontend import frontendbp

@frontendbp.route('/')
@frontendbp.route('/index')
def index():
    header= "Hello, Welcome to <span id='main-title'>WebARPES</span>"
    return render_template('index.html', title='Home-WebARPES', header=header)

@frontendbp.route('/setparams', methods=["GET", "POST"])
def setparams():
    if request.method == "POST":
        selected_lattice = request.form['lattices']
        return redirect(url_for('frontend.orbitals', lattice=selected_lattice))

    lattices = [
        {
            "type": "lieb",
            "label": "Lieb",
            "image": "LiebLattice.png",
            "apc": 3 # atoms per cell
        },
        {
            "type": "triangular",
            "label": "Triangular",
            "image": "TriangularLattice.png",
            "apc": 1 # atom per cell
        },
        {
            "type": "hexagonal",
            "label": "Hexagonal",
            "image": "HexagonalLattice.png",
            "apc": 2 # atoms per cell
        },
        {
            "type": "kagome",
            "label": "Kagome",
            "image": "KagomeLattice.png",
            "apc": 3 # atoms per cell
        }
    ]
    return render_template('setparams.html', title='Set Parameters-WebARPES', lattices=lattices)

@frontendbp.route('/orbitals/<lattice>', methods=["GET", "POST"])
def orbitals(lattice):
    if request.method == "POST":
        form_data = request.form.items()
        for k,v in form_data:
            print("key:", k)
            print("value:", v)

    if lattice == "lieb": 
        return render_template('orbitalConfig/lieb.html', title="Lieb Lattice")
    elif lattice == "triangular":
        return render_template('orbitalConfig/triangular.html', title="Triangular Lattice")
    elif lattice == "hexagonal":
        return render_template('orbitalConfig/hexagonal.html', title="Hexagonal Lattice")
    elif lattice == "kagome":
        return render_template('orbitalConfig/kagome.html', title="Kagome Lattice")
    return lattice

@frontendbp.route('/upload')
def upload():
    return render_template('upload.html', title='Upload-WebARPES')

@frontendbp.route('/345t3r_3gg')
def easter_egg():
    return "<h1>Hi, I'm Evan!</h1>"