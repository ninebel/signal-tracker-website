from . import * # Import from __init__.py all (*) the necesary imports!

panel_bp = Blueprint('panel_bp', __name__, template_folder='templates', static_folder='static', url_prefix='/panel') # Creates the blueprint

# ---------------------------------------------------------------
# BLUEPRINT SETUP
# ---------------------------------------------------------------
@panel_bp.before_app_first_request # This function is executed when the bueprint is registered in the application
def init(): 

    pass


# ---------------------------------------------------------------
# VIEWS (ROUTES)
# ---------------------------------------------------------------

# PANEL
@panel_bp.route('/')
@login_required
def panel():
    
    from .views.panel import view as panel_view # Panel view
    return panel_view(request)


# ACCOUNT
@panel_bp.route('/account', methods=['POST' , 'GET'])
@login_required
def account():

    from .views.account import view as account_view # Account view
    return account_view(request)

# ALERT (For managing an alert)
@panel_bp.route('/manage/<id>', methods=['POST', 'GET'])
@login_required
def manage(id):

    from .views.manage import view as manage_view # Account view
    return manage_view(request, id)

# CREATE (For creating an alert)
@panel_bp.route('/create', methods=['POST' , 'GET'])
@login_required
def create():

    from .views.create import view as create_view # Account view
    return create_view(request)


            
