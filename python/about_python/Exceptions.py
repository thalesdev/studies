

# Exemplo do assert
def sqrt_real(x):
    assert x >= 0, "Voce deve informar um valor maior-igual a 0"
    return x ** 0.5


# Exemplo do raise from
def sqrt_real_2(x):
    try:
        x ** 0.5
    except Exception as e:
        raise ValueError from e


############ context manager/ with ############

class MyContext:
    def __enter__(self):
        self.msg = "Vai ti toma no cu"
        return self
    def __exit__(self, value, type, traceback):
        print(value)
        print(type)
        print(traceback)


with MyContext() as m:
    print(m.msg)
    raise Exception 

#print(sqrt_real_2('-1'))
