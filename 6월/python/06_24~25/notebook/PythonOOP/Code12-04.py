## 클래스 선언 부분 ##
class Car:
    # 인스턴스 변수
    color = ""
    speed = 0
    # 클래스 변수
    count = 0

    # 생성자
    def __init__(self):
        self.speed = 0
        Car.count += 1

## 변수 선언 부분 ##
myCar1, myCar2 = None, None

## 메인 코드 부분 ##
myCar1 = Car()
myCar1.speed = 30
print("자동차1의 현재 속도는 %d이며, 생상된 자동차는 총 %d대입니다." % (myCar1.speed, myCar1.count))

myCar2 = Car()
myCar2.speed = 60
print("자동차2의 현재 속도는 %d이며, 생상된 자동차는 총 %d대입니다." % (myCar2.speed, myCar2.count))