# Decoradores de metodos:


def override(cls):
    def wrapper(method):
        error = "Metodo \"{}\" não existe na classe pai \"{}\".".format(
            method.__name__, cls.__name__)
        _assert = method.__name__ in cls.__dict__
        assert _assert, error
        return method
    return wrapper


class Father:
    def walk(self):
        print("Walking")


class Son(Father):
    def __init__(self):
        super(Son, self).__init__()

    @override(Father)
    def walk(self):
        print("Walking from son..")


s = Son()
s.walk()


# Decoradores de classes

_instances = {}


def singleton(cls):
    def wrapper(*args, **kargs):
        if cls not in _instances:
            _instances[cls] = cls.__call__(*args, **kargs)
        return _instances[cls]
    return wrapper


@singleton
class Timer:
    time = 0

    def __init__(self):
        self.time += 1


t = Timer()
t1 = Timer()
assert t == t1, "Classes diferentes, singleton não funcionou"

######## Classes decoradoras ############


class Tracer:
    _log = {}

    def __init__(self, cls):
        if cls not in Tracer._log:
            Tracer._log[cls] = {}
        self.__cls__ = cls

    def __call__(self, *args, **kargs):
        self.__t_instance__ = self.__cls__(*args, **kargs)
        self.__t_logger__ = []
        Tracer._log[self.__cls__][self.__t_instance__] = self.__t_logger__
        self.__t_logger__.append("Instanced class...")
        return self

    def __getattr__(self, attr):
        self.__t_logger__.append("get:{}".format(attr))
        return getattr(self.__t_instance__, attr)

    def __setattr__(self, attr, value):
        if attr not in ['__t_logger__', '__cls__', '__t_instance__']:
            self.__t_logger__.append("set:{}({})".format(attr, value))
            setattr(self.__t_instance__, attr, value)
        else:
            super().__setattr__(attr, value)

    def log(self):
        instance = self.__t_instance__
        if instance.__class__ in Tracer._log:
            return Tracer._log[instance.__class__][instance]
        return []


@Tracer
class People(Son):
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    @property
    def name(self):
        return "{} {}".format(self.fname, self.lname)

    @name.setter
    def name(self, names):
        if isinstance(names, list) or isinstance(names, tuple):
            if len(names) == 2:
                self.fname, self.lname = names
            elif len(names) == 1:
                self.fname = names[0]
            else:
                raise ValueError
        else:
            self.fname = names

    @name.deleter
    def name(self):
        del self.fname
        del self.lname


marcos = People("Marcos", "Antonio")
# print(marcos.name)
marcos.name = "Batman", "Darkneldo"
print(marcos.name)
print(marcos.log())
