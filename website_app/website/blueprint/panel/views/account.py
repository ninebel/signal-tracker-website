from .. import * # Import from the __init__.py all (*) the necesary imports!

class ChangeUserEmailForm(FlaskForm):
    email = StringField('email', validators=[Email(message='Preencher com um email válido'), DataRequired(message='Favor preencher o email')])

class ChangeUserPasswordForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired(message='Favor preencher a senha'), Length(min=4 ,max=50, message='A senha precisa ter entre 4 e 50 carácteres!') ,EqualTo('repeat_password', message='As duas senhas devem ser iguais!')])
    repeat_password = PasswordField('repeat password', validators=[DataRequired(message='Favor repetir a senha')])


def view(request):

    formEmail = ChangeUserEmailForm(email=api_call('users', 'get', id=session['id'], field='email'))
    formPassword = ChangeUserPasswordForm()

    if request.method == 'POST':

        # Checking formEmail.validate() and formEmail.__class__.__name__ is necessary when there is multiple fields in one page
        # Each submit button will send its name, which is the class name of the form
        if formEmail.__class__.__name__ in request.form.keys():

            if formEmail.validate():


                if api_call('users', 'query', email=formEmail.email.data): # In case the email is already taken

                    flash('Email já em uso, escolha outro!')

                else:

                    api_call('users', 'set', id=session['id'], field='email', value=formEmail.email.data)
                    flash('Email alterado com sucesso!')

            # Flash the errors with the form
            for field, errors in formEmail.errors.items():
                for error in errors:
                    flash(error)

        if formPassword.__class__.__name__ in request.form.keys():

            if formPassword.validate():

                api_call('users', 'set', id=session['id'], field='password_hash', value=formPassword.password.data)
                flash('Senha alterada com sucesso!')

            for field, errors in formPassword.errors.items():
                for error in errors:
                    flash(error)
    
    return render_template('panel/account.html', page='account', id=session['id'], formEmail=formEmail, formPassword=formPassword)
