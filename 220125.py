# class Person:
#     def __init__(self):
#         print('응애')

#     def __del__(self):
#         print('꿱')
# p100 = Person() # 
# # del p100




# 매직메서드 활용

class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    def __str__(self):
        return f'{self.name}: {self.age}'
    def __gt__(self, other):
        print(f'{self.name}:{self.age}살/ {other.name}:{other.age}살')
        return self.age > other.age
    def __len__(self):
        return self.height

p1 = Person('지수', 100, 190)
p2 = Person('동구', 101, 183)
print(p1)
print(p1>p2)
print(len(p1))