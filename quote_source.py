"""Small existing prototype. Missing behavior is part of the task."""
from decimal import Decimal

class QuoteSource:
    def __init__(self, pair, bid, ask, ttl=10):
        self.pair, self.bid, self.ask, self.ttl = pair, Decimal(bid), Decimal(ask), ttl
        self.firms, self.executions = {}, []

    def quote(self, request_id, sell, buy, amount, now):
        base, counter = self.pair
        rate = self.bid if (sell, buy) == (base, counter) else 1 / self.bid
        value = int(Decimal(amount) * rate)
        firm = {'firm_quote_id': request_id, 'sell': sell, 'buy': buy,
                'sell_amount': amount, 'buy_amount': value, 'requested_at': now,
                'expires_at': now + self.ttl}
        self.firms[request_id] = firm
        return dict(firm)

    def accept(self, firm_id, accept_id, now):
        firm = self.firms[firm_id]
        if now > firm['expires_at']:
            raise ValueError('expired')
        execution = {**firm, 'conversion_id': accept_id, 'accepted_at': now,
                     'seq': len(self.executions) + 1}
        self.executions.append(execution)
        return dict(execution)
