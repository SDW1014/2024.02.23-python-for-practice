# 숫자 리스트 출력하기
def practiceFor1():
    numbers = [1,2,3,4,5]
    for number in numbers:
        print(number)

# 문자열 리스트에서 문자열 길이 출력하기        
def practiceFor2():
    words = ["apple", "banana", "cherry"]
    for word in words:
        print(f"{word} is {len(word)} characters long. ");
        
# 딕셔너리의 키와 값 순회하기
def practiceFor3():
    person = {"name" : "John", "age" : 30, "city" : "New York"}
    for key, value in person.items():
        print(f"{key} : {value}")
        
# range() 함수 사용하기
def practiceFor4():
    for i in range(10):
        print(i)
        
# 리스트의 인덱스와 값을 함께 출력하기
def practiceFor5():
    fruits = ["apple", "banana", "cherry"]
    for index, fruit in enumerate(fruits):
        print(f"Index {index} : {fruit}")
        
#리스트 컴프리헨션 사용하기
def practiceFor6():
    even_numbers = [i for i in range(10) if i%2 == 0]
    print(even_numbers)
    
#중첩된 for 반복문 사용하기
def practiceFor7():
    for i in range(1,6):
        for j in range(1,10):
            print(f"{i} * {j} == {i*j}")
        print("------------")