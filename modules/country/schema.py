"""Module for create schema for the Appliances Availability table."""
from marshmallow import fields
from config.schema import ma


class CountrySchema(ma.Schema):
    """Schema for table country without id."""
    id = fields.Integer(dump_only=True)
    name = fields.String()
