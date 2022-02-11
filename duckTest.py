class Duck(object):

    def walk(self):
        print("waddle, waddle, waddle")

    def swim(self):
        print("Come on in, the water's fine")
    
    def quack(self):
        print("Quack quack")


class Penguin(object):

    def walk(self):
        print("Waddle, waddle, I waddle too")

    def swim(self):
        print("Come on in, but it's a bit chilly")

    def quack(self):
        print("Are you having fun?  I'm a penguin!")


def test_duck(duck):
    duck.walk()
    duck.swim()
    duck.quack()

if __name__ == '__main__':
    donald = Duck()
    test_duck(donald)

    percy = Penguin()
    test_duck(percy)
