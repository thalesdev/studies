def AssertType(tp):
    def assertTypeDecorator(func):
        def wrapper(val):
            assert isinstance(val, tp), "Tipo invalido"
            return func(val)
        return wrapper
    return assertTypeDecorator


def NoType(tp, raise_all=False):
    def domainDecorator(func):
        def wrapper(*args):
            mp = list(map(lambda e: not isinstance(e, tp), args))
            error = "Não é permitido {} do tipo {}.".format(
                "todos parametros serem" if raise_all else "mais de um parametro ser", tp.__name__)
            _assert = all(mp) if raise_all else any(mp)
            assert _assert, error
            return func(*args)
        return wrapper
    return domainDecorator


def AllowedParamTypes(*types):
    def paramTypesDecorator(func):
        def wrapper(*args):
            for arg in args:
                if arg.__class__ not in types:
                    _assert = False
                    error = "Tipo não permitido"
                    assert _assert, error
            return func(*args)
        return wrapper
    return paramTypesDecorator


@AllowedParamTypes(float, int)
def pow_square_int(*args):
    return [x**2 for x in args]


def pow_square_list(array):
    return [x**2 for x in array]


#assert False, 1
print("by params")
pow_square_int(*range(int(1e7)))
print("Gone")
print("by list")
pow_square_list(range(int(1e7)))
print("Gone")
#print(all([True, True , False]))
