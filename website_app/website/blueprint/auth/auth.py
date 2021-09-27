from . import * # Import from __init__.py all (*) the necesary imports!

auth_bp = Blueprint('auth_bp', __name__, template_folder='templates', static_folder='static') # Creates the blueprint

# ---------------------------------------------------------------
# BLUEPRINT SETUP
# ---------------------------------------------------------------
@auth_bp.before_app_first_request # This function is executed when the bueprint is registered in the application
def init(): 

    pass

# ---------------------------------------------------------------
# VIEWS (ROUTES)
# ---------------------------------------------------------------

# SIGNUP
@auth_bp.route('/signup', methods=['POST' , 'GET'])
@guest_required
def signup():

    from .views import signup # Sign-up view
    return signup.view(request)


# LOGIN
@auth_bp.route('/login', methods=['POST' , 'GET'])
@guest_required
def login():

    from .views import login # Login view
    return login.view(request)


# LOGOUT
@auth_bp.route('/logout')
@login_required
def logout():
    
    session.pop('id', None)
    return redirect(url_for('general_bp.home'))

            
