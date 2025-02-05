class MyClass:

    def func1(self):
        try:
            1 / 0
        except ZeroDivisionError:
            print("На ноль делить нельзя")
        print("Работает метод func1")

    def func2(self):
        self.func1()
        try:
            print(a)
        except NameError:
            print("Несуществующая переменная")
        print("Работает метод func2")

    def func3(self):
        self.func2()
        print("Работает метод func3")


if __name__ =="__main__":
    my_obj = MyClass()
    my_obj.func3()
