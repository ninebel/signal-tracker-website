from . import * # Import from the __init__.py all (*) the necesary imports!

# Login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'id' in session:
            return f(*args, **kwargs)
        else:
            flash('Entre na sua conta!')
            return redirect(url_for('auth_bp.login'))
    return wrap


# For pages where the user MUST NOT BE LOGGED-IN
def guest_required(f): 
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'id' in session:
            return redirect(url_for('panel_bp.panel'))
        else:
            return f(*args, **kwargs)
    return wrap