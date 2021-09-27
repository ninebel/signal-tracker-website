from .app import app, db

celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'], backend=app.config['CELERY_RESULT_BACKEND'])
celery.conf.timezone = 'UTC' # Redundant, because default is UTC

from .config import ativos
celery.conf.beat_schedule = {
    'run_alerts-1m': {
        'task': 'run_alerts',
        'schedule': 60.0, # 1x60 = 60
        'args': (ativos, '5m', '2d')
    },
    'run_alerts-5m': {
        'task': 'run_alerts',
        'schedule': 300.0, # 5x60 = 300
        'args': (ativos, '5m', '2d')
    },
    'run_alerts-15m': {
        'task': 'run_alerts',
        'schedule': 900.0, # 15x60 = 900
        'args': (ativos, '15m', '1wk')
    },
    'run_alerts-60m': {
        'task': 'run_alerts',
        'schedule': 3600.0, # 60x60 = 900
        'args': (ativos, '60m', '1mo')
    },
    'run_alerts-1d': {
        'task': 'run_alerts',
        'schedule': 3600.0, # 60x60 = 900
        'args': (ativos, '1d', '6mo')
    },
    'run_alerts-1wk': {
        'task': 'run_alerts',
        'schedule': 3600.0, # 60x60 = 900
        'args': (ativos, '1wk', '2y')
    },
}


# ---------------------------------------------------------------
# SCHEDULED TASKS
# ---------------------------------------------------------------

@celery.task
def run_alerts(assets, interval, period):

    data = yf.download(assets, interval=interval, period=period) # Download yahoo finance data

    if interval == '1m':

        print('5 MIN')
        from alerts.app import db
        from alerts.models.alert import Alert
        alerts = Alert.query.filter_by(interval=interval, enable=True)

        for alert in alerts:
            
            prices = data['Close']
            lows = data['Low']
            highs = data['High']
            volume = data['Volume']
            alert.run(prices, lows, highs, volume)

    elif interval == '5m':
        pass
    elif interval == '15m':
        pass
    elif interval == '60m':
        pass
    elif interval == '1d':
        pass
    elif interval == '1wk':
        pass

    return 'OK'