"""Ordinary same-currency arrival-order prototype, not the target system."""
class ReceivableWarehouse:
    def __init__(self):
        self.events = {}

    def receive(self, events):
        for event in events:
            self.events[event['event_id']] = dict(event)

    def report(self):
        invoices = {e['invoice_id']: dict(e) for e in self.events.values() if e['kind'] == 'invoice'}
        remaining = {key: row['amount'] for key, row in invoices.items()}
        for event in self.events.values():
            if event['kind'] == 'payment':
                for allocation in event['allocations']:
                    invoice = invoices[allocation['invoice_id']]
                    if event['currency'] == invoice['currency']:
                        remaining[invoice['invoice_id']] -= allocation['amount']
        return remaining
