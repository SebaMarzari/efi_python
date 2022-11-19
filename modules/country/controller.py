from config.database import db
from flask import Blueprint, jsonify, request
from modules.country.model import Country
from modules.country.repository import (
    find_countries,
    find_country,
    find_exists_country,
)
from sqlalchemy import insert, update


country_bp = Blueprint("country", __name__)


@country_bp.route("/register", methods=["POST"])
def add_countrie():
    """Function to add a country."""
    data = request.json
    name = data["name"]
    countries = find_countries()
    for country in countries:
        if name == country["name"]:
            return (
                jsonify({"Mensaje": "Ya existe un pais con ese nombre"}),
                404,
            )
    insert_db = insert(Country).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"Mensaje": "El pais se creo correctamente"},
            {"Pais": name},
        ),
        201,
    )


@country_bp.route("/list", methods=["GET"])
def get_all_countries():
    """Function to add a country."""
    countries = find_countries()
    return jsonify({"Paises": countries}), 201


@country_bp.route("/<id>", methods=["GET"])
def get_country(id):
    """Function to add a country."""
    countries = find_country(id)
    return jsonify({"Paises": countries}), 201


@country_bp.route("/update", methods=["PUT"])
def update_country():
    """Function to add a country."""
    data = request.json
    id = data["id"]
    exists = find_exists_country(id)
    if exists:
        update_db = (
            update(Country).where(Country.id == data["id"]).values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify({"Message": "El pais se actualizo correctamente"})
    return jsonify({"Message": "El pais no existe"})
