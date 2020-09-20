# 상속, 다중상속(interface)

# 상속기본
# 슈퍼클래스(부모), 서브클래스(변수) --> 모든 속성 메소드 사용가능

# 라면 -> 속성(종류, 회사, 맛, 면 정류, 이름) : 부모
# 신라면 : 자식
# 진라면 : 자식
# 불닭 : 자식 중복되는 부분은 상속처리해서 코드량을 줄인다!

class Car:
    """parent class"""
    def __init__(self, tp, color):
        self.type = tp
        self.color = color

    def show(self):
        return 'Car Class "Show Method!"'

class BMWCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> str :
        return "Your Car Name : %s" % self.car_name 

class BenzCar(Car):
    """Sub Class"""
    def __init__(self, car_name, tp, color):
        super().__init__(tp, color)
        self.car_name = car_name

    def show_model(self) -> str :
        return "Your Car Name : %s" % self.car_name 

    def show(self) -> str :
        print(super().show())
        return 'Car Info : %s %s %s' % (self.car_name, self.color, self.type)


bmw = BMWCar("BMW", "SUV", "레드")
print(bmw.show_model())
print(bmw.type)
print(bmw.color)
print(bmw.__dict__)
for v in bmw.__dict__.items():
    print(v)

benz = BenzCar("S530", "cedan", "White")
print(benz.show())


print(BMWCar.mro())
print(BenzCar.mro())

class X():
    pass

class Y():
    pass

class Z():
    pass

class A(X,Y):
    pass

class B(Y,Z):
    pass

class M(B,A,Z):
    pass
