from . import * # Import all (*) the imports from __init__.py 

app = Flask(__name__) # Creates the Flask application
app.config.from_pyfile('config.py') # App Configuration
db = SQLAlchemy(app)

from .models.user import User
db.create_all(bind='__all__')

# ---------------------------------------------------------------
# API AUTHENTICATION
# ---------------------------------------------------------------

@app.before_request # This function is executed when an endpoint is called
def init(): 

    # API authentication
    pass


# ---------------------------------------------------------------
# API ENDPOINTS
# ---------------------------------------------------------------

# Example usage: requests.get('http://link:port/api/users/query', json={'first_name':'Bob'}) -> Returns a list the IDs of all the users named 'Bob'
@app.route('/api/users/query', methods=['GET'])
def query(**filter):

    if filter: # If parameter (filter) were given, so its not a request

        return db.session.query(User).filter_by(**filter).all() # Returns an object

    else: # In case it is a request

        try:

            users = db.session.query(User).filter_by(**request.json).all()
            
            users_id = []
            for user in users:
                users_id.append(user.id)

            return jsonify({'result': users_id})

        except Exception as e:
            return jsonify({'status':str(e)})



# Example usage: requests.post('http://link:port/api/users/create', json=data) -> Creates a new user
@app.route('/api/users/create', methods=['POST'])
def create(): 

    try:

        request.json['password_hash'] = generate_password_hash(request.json['password_hash']) # Generate a hash password
        new_user = User(**request.json)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'status':'OK'})

    except Exception as e:
        return jsonify({'status':str(e)})


# Example usage: requests.post('http://link:port/api/users/delete', json={'id':1}) -> Deletes user with ID 1
@app.route('/api/users/delete', methods=['POST'])
def delete():

    user = query(**request.json)[0] # [0] for getting the first result (specific user)
    db.session.delete(user)
    db.session.commit()
    return jsonify({'status':'OK'})

    try:

        user = query(**request.json)[0] # [0] for getting the first result (specific user)
        db.session.delete(user)
        db.session.commit()
        return jsonify({'status':'OK'})

    except Exception as e:
        print(e)
        return jsonify({'status':str(e)})


# Example usage: requests.post('http://link:port/api/users/set', json={'id':1, 'field':'name', 'value':'Bill'}) -> Changes the first_name of user with ID 1 to 'Bill'
@app.route('/api/users/set', methods=['POST'])
def set_attr():

    try:

        field = request.json['field']
        value = request.json['value']

        if field == 'password_hash':
            value = generate_password_hash(value)

        del request.json['field']
        del request.json['value']
        user = query(**request.json)[0]
        setattr(user, field, value)
        db.session.commit()
        return jsonify({'status':'OK'})

    except Exception as e:
        return jsonify({'status':str(e)})


# Example usage: requests.get('http://link:port/api/users/get', json={'id':1, 'field':'first_name'}) -> Gets the first_name of user with ID 1
@app.route('/api/users/get', methods=['GET'])
def get_attr():

    try:

        field = request.json['field']

        if field == 'password_hash':
            return jsonify({'status':'access denied'})

        del request.json['field']
        user = query(**request.json)[0]
        return jsonify({'status':'OK', 'result':getattr(user, field)})

    except Exception as e:
        return jsonify({'status':str(e)})
    

# Example usage: requests.get('http://link:port/api/users/verify', json={'id':1, 'password':'1234'}) ->  Returns true if the user password is 1234
@app.route('/api/users/verify', methods=['GET'])
def verify_password():

    password = request.json['password']
    del request.json['password']
    user = query(**request.json)[0]
    return jsonify({'result': check_password_hash(user.password_hash, password)})
