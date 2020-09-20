class UserInfo:
    def __init__(self, name):
        self.name = name
        
    def user_info_p(self):
        print("Name :", self.name)

user1 = UserInfo("이재윤")
user1.user_info_p()

user2 = UserInfo("박재윤")
user2.user_info_p()

print(id(user1))
print(id(user2))

print(user1.__dict__)
print(user2.__dict__)

class SelfTset:
    def self_test():    # 객체 함수
        print("im here")

    def self_test2(self):   # 인스턴스 함수
        print("im here")

SelfTset.self_test()
im = SelfTset()
im.self_test2()


class WareHouse:
    # 클래스 변수(전역 변수)-> 모든 인스턴스들이 공유하는 변수
    stock_num = 0
    def __init__(self, name): # 인스턴수 함수
        self.name = name    # 로컬 변수 -> 각 인스턴스의 고유한 변수
        WareHouse.stock_num += 1
    def __del__(self):
        WareHouse.stock_num -= 1
