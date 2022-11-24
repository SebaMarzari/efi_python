from flask import Flask
from flask_migrate import Migrate

from config import database, schema
from modules.country.controller import country_bp
from modules.dni_type.controller import dni_type_bp
from modules.gender.controller import gender_bp
from modules.province.controller import province_bp
from modules.userType.controller import user_type_bp
from modules.locations.controller import locations_bp

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://BD2021:BD2021itec@143.198.156.171/python_efi_mar_pal_sch"
app.config["SECRET_KEY"] = "acalepongoloquequiera"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["pydev_do_not_trace"] = True

database.init_app(app)
schema.init_app(app)

migrate = Migrate(app, database.db)
from modules.country.model import CountryModel
from modules.dni_type.model import DniTypeModel
from modules.gender.model import GenderModel
from modules.province.model import ProvinceModel
from modules.userType.model import UserTypeModel
from modules.locations.model import LocationsModel

# Register blueprints
app.register_blueprint(country_bp, url_prefix="/countries")
app.register_blueprint(dni_type_bp, url_prefix="/dni_type")
app.register_blueprint(gender_bp, url_prefix="/gender")
app.register_blueprint(province_bp, url_prefix="/province")
app.register_blueprint(user_type_bp, url_prefix="/user_type")
app.register_blueprint(locations_bp, url_prefix="/locations")


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


if __name__ == "__main":
    app.run(debug=True)
