# class User(db.Model):
#     __tablename__ = 'user'

#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=True, unique=True)
#     password = db.Column(db.String(100), nullable=True)
#     idUserType = db.Column(db.Integer, ForeignKey('userType.id'))
#     fCarga = db.Column(db.TIMESTAMP, nullable=True)
#     idPerson = db.Column(db.Integer, ForeignKey('person.id'))
