from ..app import *

class Alert(db.Model):

    #__bind_key__ = 'alerts'
    __tablename__ = 'alerts'

    id = db.Column(db.Integer, primary_key=True, nullable=False, index=True) # Unique ID for each alert
    type = db.Column(db.String(50), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False) # Owner's ID from users database
    enable = db.Column(db.Boolean, nullable=False) # If the alert is enabled or not
    name = db.Column(db.String(50), nullable=False) # Alert name (for user control)
    asset = db.Column(db.String(50), nullable=False) # Asset name in yfinance, for example AAPL, GOOG, ITUB4.SA...
    interval = db.Column(db.String(50), nullable=False) # Sampling interval,  this means the alert will be check (run) every X interval, this can also be the candle time
    last = db.Column(db.DateTime()) # Last time the alert was triggered

    __mapper_args__ = {
        'polymorphic_identity':'alerts',
        'polymorphic_on':type
    }