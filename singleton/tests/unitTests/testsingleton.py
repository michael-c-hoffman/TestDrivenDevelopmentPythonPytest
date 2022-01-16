import singleton

def testSingletonNewClass():
    @singleton.singletonDecorator
    class Foo:
        def __init__(self, x: int)->None:
            self.x = x

    assert id(Foo(15)) == id(Foo(20))
