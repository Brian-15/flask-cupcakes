"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template
from models import Cupcake, connect_db, db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///cupcakes"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True
app.config["SECRET_KEY"] = "secret123"

connect_db(app)

def serialize_cupcake(cupcake):
    """Serialize cupcake SQLAlchemy object to dictionary"""

    return {
        "id": cupcake.id,
        "flavor": cupcake.flavor,
        "size": cupcake.size,
        "rating": cupcake.rating,
        "image": cupcake.image
    }

@app.route("/")
def home_page():
    """List cupcakes on page"""
    
    cupcakes = Cupcake.query.all()
    return render_template("index.html", cupcakes=cupcakes)

@app.route("/api/cupcakes", methods=["GET"])
def list_all_cupcakes():
    """gather all cupcakes from database"""

    cupcakes = Cupcake.query.all()
    serialized = [serialize_cupcake(c) for c in cupcakes]
    return jsonify(cupcakes=serialized)

@app.route("/api/cupcakes", methods=["POST"])
def create_cupcake():
    """post new cupcake to database"""

    cupcake = Cupcake(
        flavor=request.json.get("flavor", ""),
        size=request.json.get("size", ""),
        rating=request.json.get("rating", ""),
        image=request.json.get("image", "")
    )
    db.session.add(cupcake)
    db.session.commit()

    return jsonify(cupcake=serialize_cupcake(cupcake)), 201

@app.route("/api/cupcakes/<int:id>", methods=["GET"])
def get_cupcake(id):
    """Get cupcake from database"""

    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=serialize_cupcake(cupcake))