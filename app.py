from marshmallow import pprint
user = User(name="bansh", email="bansh")
schema = UserSchema()
result = schema.dump(user)
pprint(result)