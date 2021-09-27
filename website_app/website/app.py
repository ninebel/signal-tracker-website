from . import * # Import from __init__.py all (*) the necesary imports!

# APIs
from .config import *
def api_call(api_name, endpoint, **data):

    url = ''

    if api_name == 'users':
        url = users_url
    elif api_name == 'alerts':
        url = alerts_url
    
    if endpoint == 'query' or endpoint == 'get' or endpoint == 'verify':
        r = requests.get(url + endpoint, json=data)
        return json.loads(r.text)['result']
    else:
        r = requests.post(url + endpoint, json=data)
        return json.loads(r.text)['status']

app = Flask(__name__) # Creates the Flask application
app.config.from_pyfile('config.py') # App Configuration

# Blueprints
from .blueprint.general.general import general_bp # Homepage, about, page_not_found...
app.register_blueprint(general_bp)

from .blueprint.auth.auth import auth_bp # Login, register...
app.register_blueprint(auth_bp)

from .blueprint.panel.panel import panel_bp # Edit account, create alert, manage alerts...
app.register_blueprint(panel_bp)

@app.context_processor
def send_func():
  return {"api_call": api_call}


# View - Page not found (404)
@app.errorhandler(404)
def page_not_found(error):
    
    return "Página não encontrada!", 404

# View - Internal error (500)
@app.errorhandler(500)
def internal_error(error):
    
    return "Erro interno!", 500







