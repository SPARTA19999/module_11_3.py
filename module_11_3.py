from inspect import getmodule

def introspection_info(obj):
    introspection = {"type": type(obj).__name__, "attribute": obj.__dict__, "metods": dir(obj), "module": getmodule(obj)}
    return introspection
class Laptop:
    pass
obj = Laptop()
print(introspection_info(obj))
