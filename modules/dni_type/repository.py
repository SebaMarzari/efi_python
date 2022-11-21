"""Module for create repository for the dni type table."""
from config.database import db
from modules.dni_type.model import DniType
from modules.country.schema import CountrySchema


def find_dni_types():
    """Function to find all dni types."""
    query = db.session.query(DniType).all()
    schema = CountrySchema().dump(query, many=True)
    return schema


def find_dni_type(id: str) -> dict:
    """Function to find all countries."""
    query = db.session.query(DniType).filter(DniType.id == id).all()
    schema = CountrySchema().dump(query, many=True)
    return schema


def find_exists_dni_type(id: str) -> dict:
    """Function to find all countries."""
    query = db.session.query(DniType).filter(DniType.id == id).count()
    return query
