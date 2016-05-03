# understand *args and **kwargs

def pass_args(*args):
    return args
# ok so args is a tuple of the passed in position arguments

def pass_kwargs(**kwargs):
    return kwargs
# kwargs is a dict

def pass_all(*args,**kwargs):
    return args,kwargs
# must be in correct oder position, then key word arguments

