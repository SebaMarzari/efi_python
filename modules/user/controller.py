from config.database import db
from flask import Blueprint, jsonify, request
from modules.user.model import UserModel
from modules.user.repository import (
    find_user,
    find_users,
    find_exists_user,
)
from sqlalchemy.sql import func
from sqlalchemy import insert, update
from sqlalchemy.dialects.postgresql import CHAR


user_bp = Blueprint("user", __name__)


@user_bp.route("/register", methods=["POST"])
def add_user():
    """Function to add a user type."""
    data = request.json
    id_person = data["idPerson"]
    users = find_users()
    for user in users:
        if id_person == user["idPerson"]:
            return (
                jsonify({"message": "Ya existe un usuario con esa persona"}),
                404,
            )
    insert_db = insert(UserModel).values(data)
    db.session.execute(insert_db)
    db.session.commit()
    return (
        jsonify(
            {"message": "El usuario se creo correctamente"},
            {"data": id_person},
        ),
        201,
    )


@user_bp.route("/list", methods=["GET"])
def get_all_users():
    """Function to list all user types."""
    users = find_users()
    return jsonify({"data": users})


@user_bp.route("/<id>", methods=["GET"])
def get_user(id):
    """Function to get a userType."""
    exists = find_exists_user(id)
    if not exists:
        return jsonify({"message": "El usuario no existe"})
    userType = find_user(id)
    return jsonify({"data": userType})


@user_bp.route("/update", methods=["PUT"])
def update_user():
    """Function to update a userType."""
    data = request.json
    id = data["id"]
    exists = find_exists_user(id)
    if exists:
        update_db = (
            update(UserModel)
            .where(UserModel.id == data["id"])
            .values(data)
        )
        db.session.execute(update_db)
        db.session.commit()
        return jsonify(
            {"message": "El usuario se actualizo correctamente"}
        )
    return jsonify({"message": "El usuario no existe"})
