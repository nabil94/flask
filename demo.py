# Issue 30

class A:
    def foo(self):
        buzz()
        print('inside class A')


class B(A):
    def foo(self):
        print('inside class B')


class C(B):
    def foo(self):
        print('inside class C')

    def bar(self):
        self.foo()
        print('inside bar')


def buzz():
    ...


def driver():
    a = A()
    a.foo()
