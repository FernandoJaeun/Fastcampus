# 파이썬 모듈과 패키지
# 패키지 예제
# 상대 경로
# .. : 부모 경로
# . : 현재 경로
# 모듈의 파일 이름이 중요, 파일 이름을 보고 가져옴!

# 사용1(클래스)

from pkg.fibonacci import Fibonacci

Fibonacci.fib(300)

print("ex1 : ", Fibonacci.fib2(200))
print("ex1 : ", Fibonacci().title)

# 사용 2(클래스)
from pkg.fibonacci import Fibonacci as fb   # alias

fb.fib(1300)

print("ex2 : ", fb.fib2(2200))
print("ex2 : ", fb().title)

# 사용 3(함수)
import pkg.calculations as cal

print("ex 3 : ", cal.add(10,100))
print("ex 3 : ", cal.mul(10,100))

# 사용 4(함수)
from pkg.calculations import div
print("ex 4 : ", div(100,10))
print("ex 4 : ", int(div(100,10)))

# 사용 5
import pkg.prints as p
import builtins
p.prt1()
p.prt2()
# print(dir(builtins))
