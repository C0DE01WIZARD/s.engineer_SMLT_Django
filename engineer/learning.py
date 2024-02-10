class Point:
    color = 'red'
    circle = 2


    def __init__(self, x=1, y=3):
        print("Вызов __init__")
        self.x = x
        self.y = y

    def __del__(self):
        print('Удаление объекта'+ str(self))

pt = Point()
print(pt.__dict__)
