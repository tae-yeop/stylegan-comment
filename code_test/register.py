_metric_dict = dict() # name => fn

def register_metric(fn):
    assert callable(fn)
    _metric_dict[fn.__name__] = fn
    return fn
  
  
def do_func(func_name, a):
  print(_metric_dict[func_name](a))
   
   
@register_metric
def func1(a):
  return a


@register_metric
def func2(a):
  return a

