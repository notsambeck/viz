import ast


code = """
C = 10


def mfunc(x):
    y = x ** 2 + 15
    return y


y = mfunc(c)
print(f'myfunc({C}) = y')
"""


if __name__ == "__main__":
    p = ast.parse(code)
    print(p)
    print(p.body[0].__dict__)
