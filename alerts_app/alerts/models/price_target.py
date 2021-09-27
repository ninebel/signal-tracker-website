from ..app import *
from ..models.alert import Alert

class PriceTarget(Alert):

    #__bind_key__ = 'alerts'
    __tablename__ = 'price_target'

    id = db.Column(db.Integer, db.ForeignKey('alerts.id'), primary_key=True)
    target = db.Column(db.Float(), nullable=False) # Target values that must hit in order to trigger the alert
    #length = db.Column(db.Integer(), nullable=False) # The time length used to calculate the EMA

    __mapper_args__ = {
        'polymorphic_identity':'price_target',
    }

    def run(self, prices, lows, highs, volume):

        # The line below will check if the target value was crossed by comparing 2 points (if the target is between them)
        if (self.target > prices[len(prices)-2] and prices[len(prices)-1] > self.target) or (self.target < prices[len(prices)-2] and prices[len(prices)-1] < self.target):

            # In this case the alert was activated
            self.contact()
            return True

        else:

            return False

    def contact(self):

        pass