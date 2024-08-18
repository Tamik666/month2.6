class Hello:
    def __init__(self, str):
        self.str = str


class Bonjour(Hello):
    def __init__(self, str):
        Hello.__init__(self, str)

    def __str__(self):
        return self.str


a = Bonjour("Hello")
print(a)
