from .. import * # Import from the __init__.py all (*) the necesary imports!


class CreateAlertForm(FlaskForm):
    name = StringField('name', validators=[DataRequired(message='Favor preencher com um nome'), Length(max=50, message='O nome do alerta deve ter no máximo 50 carácteres')])
    asset = SelectField('asset', choices=[('BBDC4.SA', 'BBDC4'), ('ITUB4.SA', 'ITUB4')])
    interval = SelectField('interval', choices=[('5m', '5m'), ('15m', '15m'), ('60m', '60m'), ('1d', '1d'), ('1wk', '1wk')])

    type = SelectField('type', choices=[('price_target', 'Preço alvo')])

class TargetPriceForm(FlaskForm):
    target = FloatField('target', validators=[DataRequired(message='Favor preencher com um número')])


def view(request):

    #from website.config import alerts

    formAlert = CreateAlertForm()
    formPriceTarget = TargetPriceForm()

    if request.method == 'POST':

        if formAlert.validate_on_submit():

            max_alerts = api_call('users', 'get', id=session['id'], field='max_alerts')
            claimed_alerts = api_call('users', 'get', id=session['id'], field='claimed_alerts')

            if (max_alerts - claimed_alerts) > 0: # If the user still has unused alerts

                # For each alert...
                if formAlert.type.data == 'price_target':

                    api_call('alerts', 'create', type='price_target', owner_id=session['id'] , enable=True, name=formAlert.name.data, asset=formAlert.asset.data, interval=formAlert.interval.data, target=formPriceTarget.target.data)
                    api_call('users', 'set', id=session['id'], field='claimed_alerts', value=claimed_alerts+1)
                    flash('Alerta criado com sucesso!')
                    return redirect(url_for('panel_bp.panel'))

            else:
                flash('Você não tem mais alertas disponíveis!')


    return render_template('panel/create.html', page='panel', formAlert=formAlert, formPriceTarget=formPriceTarget)