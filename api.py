from datetime import timedelta
from flask import Flask
from flask_jwt import JWT, jwt_required, current_identity
from gslothutils.safe_str_cmp import safe_str_cmp
from gslothutils.log import log
from gslothutils.pprint import pprint




class Client(object):
	def __init__(self, id, username, password):
		self.id = id
		self.username = username
		self.password = password

	def __str__(self):
		return "Client(id={})".format(self.id)

clients = [
	Client(1, "user1", "password1"),
	Client(2, "user2", "password2"),
]

#pprint(clients)

username_table = {u.username: u for u in clients}
userid_table = {u.id: u for u in clients}

def authenticate(username, password):
	user = username_table.get(username, None)
	if user and safe_str_cmp(user.password.encode("utf-8"), password.encode("utf-8")):
		return user

def identity(payload):
	user_id = payload["identity"]
	return userid_table.get(user_id, None)

app = Flask(__name__)
app.debug = True
app.config["SECRET_KEY"] = "secret"
app.config["JWT_AUTH_URL_RULE"] = "/auth"
app.config["JWT_AUTH_ENDPOINT"] = "jwt"
app.config["JWT_AUTH_USERNAME_KEY"] = "username"
app.config["JWT_AUTH_PASSWORD_KEY"] = "password"
app.config["JWT_ALGORITHM"] = "HS256"
app.config["JWT_LEEWAY"] = timedelta(seconds=10)
app.config["JWT_AUTH_HEADER_PREFIX"] = "JWT"
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds=300)
app.config["JWT_NOT_BEFORE_DELTA"] = timedelta(seconds=0)
app.config["JWT_VERIFY_CLAIMS"] = ['signature', 'exp', 'nbf', 'iat']
app.config["JWT_REQUIRED_CLAIMS"] = ['exp', 'iat', 'nbf']

jwt = JWT(app, authenticate, identity)

@app.route("/hi",methods = ["POST", "GET"])
@jwt_required()
def hi():
	log.debug(username_table)
	log.debug(userid_table)
	return "Hi, %s" % current_identity
	

if __name__ == "__main__":
	app.run(host="0.0.0.0", port=5005)