def testEqual(x,y):
    """Testa l’uguaglianza fra due valori (int, str)"""
    if x == y:
        print("Pass")
    else:
        print("Not passing")

def testEqualF(x, y, e):
    if abs(x - y) < e:
        print("Pass Float")
    else:
        print("Expected" + str(x) + "got" + str(y))