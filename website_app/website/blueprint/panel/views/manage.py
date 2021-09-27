from .. import * # Import from the __init__.py all (*) the necesary imports!

class ChangeAlertEnableForm(FlaskForm):
    enable = BooleanField('enable')

class ChangeAlertNameForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='Favor preencher com um nome'), Length(max=50, message='O nome do alerta deve ter no máximo 50 carácteres')])

class ChangeAlertPriceTarget(FlaskForm):
    target = FloatField('target', validators=[DataRequired(message='Favor preencher com um número')])

class DeleteAlertForm(FlaskForm):
    delete = SubmitField('Deletar')

def view(request, id):

    if api_call('alerts', 'query', id=id): # If the alert was found and exists

        if api_call('alerts', 'get', id=id, field='owner_id') == session['id']: # If the alert belongs to the user

            formEnable = ChangeAlertEnableForm(enable=api_call('alerts', 'get', id=id, field='enable'))
            formName = ChangeAlertNameForm(name=api_call('alerts', 'get', id=id, field='name'))
            formAlert = object()
            formDelete = DeleteAlertForm()

            # For each alert...
            if api_call('alerts', 'get', id=id, field='type') == 'price_target':

                formAlert = ChangeAlertPriceTarget(target=api_call('alerts', 'get', id=id, field='target'))
            # ----

            if request.method == 'POST':

                # Checking formEmail.validate() and formEmail.__class__.__name__ is necessary when there is multiple fields in one page
                # Each submit button will send its name, which is the class name of the form          
                if formEnable.validate_on_submit() and formEnable.__class__.__name__ in request.form.keys():

                    api_call('alerts', 'set', id=id, field='enable', value=formEnable.enable.data) # Set the enable state

                    if api_call('alerts', 'get', id=id, field='enable'):
                        #print(get_alert_attr('enable', id=id))
                        #print(type(get_alert_attr('enable', id=id)))
                        flash('Alerta ativado!')
                    else:
                        flash('Alerta desativado!')

                if formName.validate_on_submit() and formName.__class__.__name__ in request.form.keys():

                    api_call('alerts', 'set', id=id, field='name', value=formName.name.data) # Set name
                    flash('Nome do alerta alterado com sucesso!')

                if formAlert.validate_on_submit() and formAlert.__class__.__name__ in request.form.keys():

                    # For each alert...
                    if api_call('alerts', 'get', id=id, field='type') == 'price_target':

                        api_call('alerts', 'set', id=id, field='target', value=formAlert.target.data)
                        flash('Alerta alterado com sucesso!')
                    # ----

                if formDelete.validate_on_submit() and formDelete.delete.name in request.form.keys():

                    api_call('users', 'get', id=session['id'], field='claimed_alerts')
                    claimed_alerts = api_call('users', 'get', id=session['id'], field='claimed_alerts')
                    api_call('users', 'set', id=session['id'], field='claimed_alerts', value=claimed_alerts-1)
                    api_call('alerts', 'delete', id=id)
                    flash('Alerta deletado com sucesso!')

                    return redirect(url_for('panel_bp.panel'))


                # Flash the errors with the form
                for field, errors in formName.errors.items():
                    for error in errors:
                        flash(error)
                for field, errors in formAlert.errors.items():
                    for error in errors:
                        flash(error)

            return render_template('panel/manage.html', page='panel', id=id, formEnable=formEnable, formName=formName, formAlert=formAlert, formDelete=formDelete)

        else:
            return "Esse alerta não te pertence!", 200
    else:

        return "Alerta não encontrado!", 404