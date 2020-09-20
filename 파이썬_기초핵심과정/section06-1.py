# 파이썬 함수식 및 람다(lambda)
# 함수 정의 방법
# def 함수명(parameter):
#   code


def args_func(*asd):
    # print(asd)
    for index, value in enumerate(asd):
        print(index, value )

args_func(1)
args_func(1,2)
args_func(1,3,4)
args_func(1,2,3,4,5)



def kwargs_func(**asd):
    # print(asd)
    for i, v in asd.items():
        print(i, v)

kwargs_func(name1= "asd", name2="qwe")
kwargs_func(name1= "asd")


def example_mul(a1, a2, *a3, **a4):
    print(a1,a2,a3,a4)

example_mul(10,20, a3=["asd","asd","asd"] ,name1= "123",name2="123")


# 중첩함수(클로저) closer!
# 함수안에 함수
def nested_func(num : int) -> int:
    def func_in_func(num):
        print(">>>", num)
    print("in func")
    func_in_func(num+10000)
nested_func(100)


# 람다식 예제
# 람다식 : 메모리절약, 가독성 향상, 간결한 코드
# 함수는 객체 생성 -> 리소스 할당
# 람다는 즉시 실행(Heap 초기화) -> 메모리 초기화


lambda_mul_10 = lambda num: num * 100
print(lambda_mul_10(10))

def func_final(x,y,func):
    print(x * y * func(10))

func_final(10,10, lambda x : x * 1000)

  
