"""Module for create repository for the country table."""
from config.database import db
from modules.country.model import Country
from modules.country.schema import CountrySchema


def find_countries():
    """Function to find all countries."""
    query = db.session.query(Country).all()
    schema = CountrySchema().dump(query, many=True)
    return schema


def find_country(id: str) -> dict:
    """Function to find all countries."""
    query = db.session.query(Country).filter(Country.id == id).all()
    schema = CountrySchema().dump(query, many=True)
    return schema


def find_exists_country(id: str) -> dict:
    """Function to find all countries."""
    query = db.session.query(Country).filter(Country.id == id).count()
    return query
