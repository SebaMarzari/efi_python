from flask import Flask
from flask_migrate import Migrate

from config import database, schema
from modules.country.controller import country_bp
from modules.dni_type.controller import dni_type_bp

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://BD2021:BD2021itec@143.198.156.171/python_efi_mar_pal_sch"
app.config["SECRET_KEY"] = "acalepongoloquequiera"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config["pydev_do_not_trace"] = True

database.init_app(app)
schema.init_app(app)

migrate = Migrate(app, database.db)
from modules.country.model import Country
from modules.dni_type.model import DniType


# Register blueprints
app.register_blueprint(country_bp, url_prefix="/countries")
app.register_blueprint(dni_type_bp, url_prefix="/dni_type")


# Serializadores
# class CountrySchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.String()


# class CountryWithoutIdSchema(ma.Schema):
#     name = fields.String()


# class ProvinceSchema(ma.Schema):
#     name = fields.String()
#     idCountry = fields.Integer()


# class PersonSchema(ma.Schema):
#     id = fields.Integer(dump_only=True)
#     name = fields.String()
#     idTypeDni = fields.Integer()
#     dni = fields.Integer()
#     address = fields.String()
#     idLocation = fields.Integer()
#     idCountry = fields.Integer()
#     countries = fields.Nested(CountrySchema, exclude=['id',])
#     born = fields.String()
#     idSex = fields.Integer()
#     phone = fields.Integer()
#     mail = fields.String()
#     uploadDate = fields.Date()
#     active = fields.Boolean()


# class UserSchema(ma.Schema):
#     id = fields.Integer()
#     name = fields.String()
#     idUserType = fields.Integer()


# SI NO LE DETERMINO EL METODO; SIEMPRE ES UN GET
# @app.route('/countries')
# def get_countries():
#     country = db.session.query(Country).all()
#     countrie_schema = CountrySchema().dump(country, many=True)
#     return jsonify(countrie_schema)


# # POST
# @app.route('/countries', methods=['POST'])
# def add_countrie():
#     if request.method == 'POST':
#         data = request.json
#         name = data['name']
#         countries = db.session.query(Country).all()
#         for country in countries:
#             if name == country.name:
#                 return jsonify({"Mensaje":"Ya existe un pais con ese nombre"}),404
#         new_countrie = Country(name=name)
#         db.session.add(new_countrie)
#         db.session.commit()
#         countrie_schema = CountryWithoutIdSchema().dump(
#            new_countrie
#         )
#         return jsonify(
#             {"Mensaje":"El pais se creo correctamente"},
#             {"Pais": countrie_schema}
#         ), 201


# @app.route('/countries_names')
# def get_country_names():

#     countrie_schema = CountryWithoutIdSchema().dump(
#         db.session.query(Country).all(), many=True
#     )
#     return jsonify(countrie_schema)


# @app.route('/persons')
# def get_persons():
#     """
#     Paginado recibe 2 parametros principales
#     PAGINA (pag) y CANTIDAD (can)
#     Y un tercer parametro obligatorio que es
#     error_out que se pude setear como vacio
#     """

#     try:
#         can = int(request.args.get('can'))
#         pag = int(request.args.get('pag'))
#         persons = Person.query.paginate(pag, can, error_out="No se obtienen valores").items
#     except:
#         persons = db.session.query(Person).all()
#         pag = 1
#         can = 'Todos'

#     persons_schema = PersonSchema().dump(persons, many=True)
#     return jsonify(dict(
#         pagina=pag,
#         cantidad=can,
#         result=persons_schema
#         )
#     )


# @app.route('/users')
# def get_users():
#     users = db.session.query(User).all()
#     if len(users) == 0:
#         return jsonify(dict(Mensaje='No existen usuario aun')), 400
#     users_schema = UserSchema().dump(users, many=True)
#     return jsonify(dict(Usuarios=users_schema)), 200


# @app.route('/users', methods=['POST'])
# def add_user():
#     if request.method == 'POST':
#         data = request.json
#         name = data['name']
#         password = data['password'].encode('utf-8')
#         idUserType = data['idUserType']
#         idPerson = data['idPerson']

#         pass_hash = hashlib.md5(password).hexdigest()

#         try:
#             new_user = User(
#                 name=name,
#                 password=pass_hash,
#                 idUserType=idUserType,
#                 idPerson=idPerson,
#                 fCarga=datetime.now()
#             )
#             db.session.add(new_user)
#             db.session.commit()

#             result = UserSchema().dump(new_user)

#             if result:
#                 return jsonify(dict(NuevoUsuario=result))

#         except:
#             return jsonify(dict(Error="Username en uso")), 201


# @app.route('/login', methods=['GET'])
# def login():
#     auth = request.authorization
#     username = auth['username']
#     password = auth['password'].encode('utf-8')

#     if not auth or not auth.username or not auth.password:
#         return make_response(
#             {"Error": "No se enviaron todos lo parametros auth"}, 401
#         )

#     hasheada = hashlib.md5(password).hexdigest()

#     user_login = db.session.query(User).filter_by(
#         name=username).filter_by(
#             password=hasheada
#         ).first()

#     if user_login:
#         token = jwt.encode(
#             {
#                 'usuario': username,
#                 'id_usuario': user_login.id,
#                 'exp': datetime.utcnow() + timedelta(minutes=5)
#             },
#             app.secret_key
#         )
#         session['api_session_token'] = token

#         return jsonify({"Token": token.decode("UTF-8")})

#     return make_response(
#             {"Error": "Algun dato no coincide"}, 401
#         )


# def token_required(f):
#     @wraps
#     def decorated(*args, **kwargs):
#         token = None
#         if 'x-access-token' in request.headers:
#             token = request.headers['x-access-token']

#         if not token:
#             return jsonify({"ERROR":"Token is missing"}),401

#         try:
#             datatoken = jwt.decode(token, app.secret_key)
#             print(datatoken)
#             userLogged = User.query.filter_by(id=datatoken['id_usuario']).first()
#         except:
#             return jsonify(
#                 {"ERROR": "Token is invalid or expired"}
#             ),401

#         return f(userLogged, *args, **kwargs)

#     return decorated

# @app.route('/provinces')
# @token_required
# def get_provinces(userLogged):
#     if userLogged.idUserType == 2:
#         provinces = db.session.query(Province).all()
#         provice_shemma = ProvinceSchema().dump(provinces, many=True)
#         return jsonify(provice_shemma)
#     else:
#         return jsonify({"Error":"Ud no tiene permiso"})

# @app.route('/provinces', methods=['post'])
# def add_province():
#     if request.method == 'POST':
#         data = request.json
#         name = data['name']
#         country_id = data['country_id']
#         try:
#             new_province = Province(idContry=country_id, name=name)
#             db.session.add(new_province)
#             db.session.commit()

#             provice_schema = ProvinceSchema().dump(new_province)

#             return jsonify(
#                 {"Mensaje" : "La Provincia se creo correctamente"},
#                 {"Pais": provice_schema}
#             ), 201

#         except:
#             return jsonify(
#                 {"Mensaje": "Algo salio mal, valide los datos"},
#             ), 404


if __name__ == "__main":
    app.run(debug=True)
