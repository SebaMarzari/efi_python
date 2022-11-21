"""Module for create schema for the type of dni table."""
from marshmallow import fields
from config.schema import ma


class DniTypeSchema(ma.Schema):
    """Schema for table country without id."""
    id = fields.Integer(dump_only=True)
    name = fields.String()
