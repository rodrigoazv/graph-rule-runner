from .models import Rule

def create_rule(tx, _):
    rule = Rule(name='Jim', value=3, code='VALUE').save()
    return rule