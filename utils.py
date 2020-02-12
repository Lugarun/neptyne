
async def async_lambda(f):
    return f()

async def aseq(*futs):
    for fut in futs:
        await fut

class dotdict(dict):
    __getattr__ = dict.get
    __setattr__ = dict.__setitem__
    __delattr__ = dict.__delitem__

def id_stream(prevs=()):
    id = max([0] + [prev.id or 0 for prev in prevs])
    def bump():
        nonlocal id
        id += 1
        return id
    return bump


