from . import * # Import all (*) the imports from __init__.py 

app = Flask(__name__) # Creates the Flask application
app.config.from_pyfile('config.py') # App Configuration
db = SQLAlchemy(app)

from .models.alert import Alert
from .models.price_target import PriceTarget
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

# Example usage: requests.get('http://link:port/api/alerts/query', json={'owner_id':1}) -> Returns a list with the ID of all the alerts owned by user with ID 1
@app.route('/api/alerts/query', methods=['GET'])
def query(**filter):

    if filter: # If parameter (filter) were given, so its not a request

        return db.session.query(Alert).filter_by(**filter).all() # Returns an object

    else: # In case it is a request

        try:

            alerts = db.session.query(Alert).filter_by(**request.json).all()
            
            alerts_id = []
            for alert in alerts:
                alerts_id.append(alert.id)

            return jsonify({'result': alerts_id})

        except Exception as e:
            return jsonify({'status':str(e)})


# Example usage: requests.post('http://link:port/api/alerts/create', json=data) -> Creates a new alert
@app.route('/api/alerts/create', methods=['POST'])
def create():

    try:

        alerts = {'price_target': PriceTarget}

        alert_type = request.json['type']
        del request.json['type']
        alert = alerts[alert_type](**request.json)
        db.session.add(alert)
        db.session.commit()
        return jsonify({'status':'OK'})

    except Exception as e:
        return jsonify({'status':str(e)})


# Example usage: requests.post('http://link:port/api/alerts/delete', json={'id':1}) -> Deletes alert with ID 1
@app.route('/api/alerts/delete', methods=['POST'])
def delete():

    try:

        alert = query(**request.json)[0] # [0] for getting the first result (specific user)
        db.session.delete(alert)
        db.session.commit()
        return jsonify({'status':'OK'})

    except Exception as e:
        return jsonify({'status':str(e)})


# Example usage: requests.post('http://link:port/api/alerts/set', json={'id':1, 'field':'name', 'value':'Main alert'}) -> Changes the name of alert with ID 1 to 'Main alert'
@app.route('/api/alerts/set', methods=['POST'])
def set_attr():

    try:

        field = request.json['field']
        value = request.json['value']
        del request.json['field']
        del request.json['value']
        alert = query(**request.json)[0]
        setattr(alert, field, value)
        db.session.commit()
        return jsonify({'status':'OK'})

    except Exception as e:
        return jsonify({'status':str(e)})


# Example usage: requests.get('http://link:port/api/alerts/get', json={'id':1, 'field':'name'}) -> Gets the name of alert with ID 1
@app.route('/api/alerts/get', methods=['GET'])
def get_attr():

    try:

        field = request.json['field']
        del request.json['field']
        alert = query(**request.json)[0]
        return jsonify({'status':'OK', 'result':getattr(alert, field)})

    except Exception as e:
        return jsonify({'status':str(e)})



            
