import pickle

class Seriazable:
    def __init__(self, b):
        self.a = 30
        self.b = b

    def __eq__(self, other):
        return self.a == other.a and self.b == other.b


l = Seriazable(dict(n=30))
with open(".teste", "wb") as file:
    p = pickle.dump(l, file, pickle.HIGHEST_PROTOCOL)
    file.close()

with open(".teste", "rb") as file:
    l1 = pickle.load(file)
    assert (l1 == l)
    print("Seriazable:", l1.b.get("n"))
    file.close()