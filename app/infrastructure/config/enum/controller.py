from frozendict import frozendict


fd = frozendict({
        'AccountController': 1,
        'TransactionController': 2,
        'SeedController':3
    })

def get_controller_enum(key):
    return fd[key]