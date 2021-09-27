from ..app import *

class User(db.Model):

    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True, nullable=False, index=True)
    created_at = db.Column(db.DateTime) # year-month-day hour format

    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password_hash = db.Column(db.String(256), nullable=False)
    cell_number = db.Column(db.Integer)
    gender = db.Column(db.String(50)) # 'male' or 'female'
    age = db.Column(db.Integer)

    max_alerts = db.Column(db.Integer, nullable=False)
    claimed_alerts = db.Column(db.Integer, nullable=False)
    role = db.Column(db.String(50), nullable=False) # 'free', 'premium'...

    # Custom constructor
    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)
        self.created_at = datetime.datetime.now()
        self.claimed_alerts = 0
        
        if self.role == 'premium':
            pass
        else:
            from ..config import free_max_alerts
            self.max_alerts = free_max_alerts

    def __repr__(self):
        return self.email # Must return a string or it will raise an error



