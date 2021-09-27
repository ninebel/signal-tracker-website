from .. import * # Import from the __init__.py all (*) the necesary imports!

class LoginForm(FlaskForm):

    email = StringField('email', validators=[DataRequired(message='Favor preencher o eemail')])
    password = PasswordField('password', validators=[DataRequired(message='Favor preencher a senha')])

def view(request):

    form = LoginForm()

    if request.method == 'POST' and form.validate():

        email = form.email.data
        
        if api_call('users', 'query', email=email): # If the user email exists, so he's registered    

            if api_call('users', 'verify', email=email, password=form.password.data):
                                
                # Log-in the user and open a session
                session.pop('_flashes', None) # Clear flash messages
                session['id'] = api_call('users', 'get', email=email, field='id')
                session.permanent = False
                app.permanent_session_lifetime = datetime.timedelta(minutes=15)
                # ---------------------
                return redirect(url_for('panel_bp.panel'))

            else:
                flash('A senha está incorreta!')
        else:
            flash('Esse email não está cadastrado!')
            email = ''

    # Flash the errors with the form
    for field, errors in form.errors.items():
        for error in errors:
            flash(error)

    return render_template('auth/login.html', page='login', form=form)
