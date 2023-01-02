class Singleton:
    _instances = {}

    def __call__(cls, *args, **kargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(
                SingletonMeta, cls).__call__(*args, **kargs)
        return cls._instances[cls]


class Popo(Singleton):
    i = 10

    def __init__(self):
        self.i += 10

        print(self.i)




a = Popo()
b = Popo()