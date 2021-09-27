from .. import * # Import from the __init__.py all (*) the necesary imports!
print(api_call)

class SignupForm(FlaskForm):

    first_name = StringField('first name', validators=[Regexp(r'^\w+$', message='Formato inválido'), DataRequired(message='Favor preencher o nome'), Length(max=50, message='O nome deve ter no máximo 50 carácteres')])
    last_name = StringField('last name', validators=[Regexp(r'^\w+$', message='Formato inválido'), DataRequired(message='Favor preencher o sobrenome'), Length(max=50, message='O sobrenome deve ter no máximo 50 carácteres')])
    email = StringField('email', validators=[Email(message='Preencher com um email válido'), DataRequired(message='Favor preencher o email')])
    password = PasswordField('password', validators=[DataRequired(message='Favor preencher a senha'), Length(min=4 ,max=50, message='A senha precisa ter entre 4 e 50 carácteres!') ,EqualTo('repeat_password', message='As duas senhas devem ser iguais!')])
    repeat_password = PasswordField('repeat password', validators=[DataRequired(message='Favor repetir a senha')])
    #accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])

def view(request):

    form = SignupForm()

    # For POST request (receive data information for example)
    if request.method == 'POST' and form.validate():

        first_name = form.first_name.data
        last_name = form.last_name.data
        email = form.email.data
        password = form.password.data

        if api_call('users', 'query', email=email): # Checks if a email already exists for a given ID

            flash('Email já em uso, escolha outro!')
            email = ''

        #elif recaptcha.verify() == False:

            #flash("Erro no captcha!")
                
        else:

            # Creates an user by sending the request and then checks if it was succesful
            if api_call('users', 'create', first_name=first_name, last_name=last_name, email=email, password_hash=password, role='free') == 'OK':
                    
                # Log-in the user by opening a session
                session.pop('_flashes', None) # Clear flash messages
                session['id'] = api_call('users', 'get', email=email, field='id')
                session.permanent = False
                app.permanent_session_lifetime = datetime.timedelta(minutes=15)
                # ---------------------

                return redirect(url_for('panel_bp.panel'))

    # Flash the errors with the form
    for field, errors in form.errors.items():
        for error in errors:
            flash(error)

    return render_template('auth/signup.html', page='signup', form=form)