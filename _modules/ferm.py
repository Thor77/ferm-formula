'''
ferm execution module
'''
__virtualname__ = 'ferm'


def __virtual__():
    '''
    Check requirements for this module
    '''
    return __virtualname__


def _render_kv(key, value):
    value = '({})'.format(' '.join(map(str, value))) if type(value) == list else value
    return '{} {}'.format(key, value)


def build_rule(rule, rule_defaults={}, comment=None):
    '''
    Build config line from rule
    '''
    r = __salt__['slsutil.merge'](rule_defaults, rule, 'replace')
    key_values = [
        _render_kv('domain', r.pop('domain')),
        _render_kv('table', r.pop('table')),
        _render_kv('chain', r.pop('chain'))
    ]
    if 'policy' not in r and comment:
        # don't add comment for policy, because that's not allowed
        key_values.append(
            'mod comment comment "{}"'.format(comment)
        )
    action = r.pop('action', None)
    key_values.extend(
        map(lambda kv: _render_kv(kv[0], kv[1]), r.items())
    )
    if action:
        key_values.append(action)
    return ' '.join(key_values)
