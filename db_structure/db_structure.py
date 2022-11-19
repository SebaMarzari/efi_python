# """Module for the database structure."""

# from flask import Flask
# from flask_migrate import Migrate
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import ForeignKey



# db = SQLAlchemy(app)
# migrate = Migrate(app, db)


# class Country(db.Model):
#     __tablename__ = 'country'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)

#     def __str__(self):
#         return self.name

#     """ 
#     SI NO SE LE ESTABLECE UN INIT 
#     CADA VEZ QUE SE GENERE EL OBJETO DEBERAN
#     ESTABLECER QUE PARAMETRO ES CADA UNO
#     DE LO CONTRARIO EL PRIMER PARAMETRO SERA
#     CONSIDERADO COMO ID
#     """

#     def __init__(self, name):
#         self.name = name


# class Province(db.Model):
#     __tablename__ = 'province'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     idContry = db.Column(db.Integer, ForeignKey('country.id'))


# class Location(db.Model):
#     __tablename__ = 'location'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     idProvince = db.Column(db.Integer, ForeignKey('province.id'))


# class Sex(db.Model):
#     __tablename__ = 'sex'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(10), nullable=True)


# class DniType(db.Model):
#     __tablename__ = 'dniType'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(10), nullable=True)


# class Person(db.Model):
#     __tablename__ = 'person'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     idTypeDni = db.Column(db.Integer, ForeignKey('dniType.id'))
#     dni = db.Column(db.Integer, nullable=True)
#     address = db.Column(db.String(100), nullable=True)
#     idLocation = db.Column(db.Integer, ForeignKey('location.id'))
#     idCountry = db.Column(db.Integer, ForeignKey('country.id'))
#     born = db.Column(db.TIMESTAMP, nullable=True)
#     idSex = db.Column(db.Integer, ForeignKey('sex.id'))
#     phone = db.Column(db.Integer, nullable=False)
#     mail = db.Column(db.String(50), nullable=False)
#     uploadDate = db.Column(db.TIMESTAMP, nullable=True)
#     active = db.Column(db.Boolean, nullable=True, default=True)
#     countries = db.relationship('Country')


# class UserType(db.Model):
#     __tablename__ = 'userType'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(10), nullable=True)


# class User(db.Model):
#     __tablename__ = 'user'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=True, unique=True)
#     password = db.Column(db.String(100), nullable=True)
#     idUserType = db.Column(db.Integer, ForeignKey('userType.id'))
#     fCarga = db.Column(db.TIMESTAMP, nullable=True)
#     idPerson = db.Column(db.Integer, ForeignKey('person.id'))
