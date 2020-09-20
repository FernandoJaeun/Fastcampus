q1 = "dk2jd923i1jdk2jd93jfd92jd918943jfd8923" # 길이
print(len(q1))

#    apple;orange;banana;lemon
print("apple;orange;banana;lemon")


print("*" *100)

str1 = '30'
print(int(str1))
print(float(str1))
print(complex(str1))
print(str(str1))


str2 = "Niceman"
print(str2[4:])
print(str2[str2.index("man"):])
print(str2.index("man"))


str3 = "Strawberry"
print(list(reversed(str3))[0:],sep = "")
print(str3[::-1])


str4 = "010-8589-2763"
print(str4.replace("-",""))


str5 = "http://daum.net"
str5.index("http://")
print(str5.replace("http://",""))


str6 = "NiceMan"
print(str6.lower())
print(str6.upper())


str7 = "abcdefghijklmn"
print(str7[2:5])


list1 = ["Banana", "Apple", "Orange"]
print(list1)
list1.remove("Apple")
print(list1)


tuple1 = (1,2,3,4)
print(list(tuple1))


dict1 = {"성인": 100000, "청소년": 70000,"아동" : 30000}
print(dict1.keys())
dict1["소아"] = 0
print(dict1.keys())
print(dict1)
print(dict1.keys())
print(dict1.values())