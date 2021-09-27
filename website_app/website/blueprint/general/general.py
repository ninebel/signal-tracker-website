from . import * # Import from __init__.py all (*) the necesary imports!

general_bp = Blueprint('general_bp', __name__, template_folder='templates', static_folder='static') # Creates the blueprint

# ---------------------------------------------------------------
# BLUEPRINT SETUP
# ---------------------------------------------------------------
@general_bp.before_app_request # This function is executed when the bueprint is registered in the application
def init(): 

    pass


# ---------------------------------------------------------------
# VIEWS (ROUTES)
# ---------------------------------------------------------------

# INDEX (HOMEPAGE)
@general_bp.route('/')
@general_bp.route('/home')
def home():
    
    return render_template('general/home.html', page='home')


# ABOUT
@general_bp.route('/about')
def about():

    return render_template('general/about.html', page='about')




            
