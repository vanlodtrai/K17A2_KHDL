#9.1
def sign(x:int):
    if x > 0:
        return 1
    elif x < 0:
        return -1
    else:
        return 0
print(sign(8))
print(sign(-8))
print(sign(0))

#9.2
def am_lich(nam_duong: int) -> str:
    if nam_duong%10:
      can = ["Canh", "Tân", "Nhâm", "Quý", "Giáp", "Ất", "Bính", "Đinh", "Mậu", "Kỷ"]
    if nam_duong%12:
        chi = ["Thân", "Dậu", "Tuất", "Hợi", "Tý", "Sửu", "Dần", "Mão", "Thìn", "Tỵ", "Ngọ", "Mùi"]
    return can[nam_duong % 10] + " " + chi[nam_duong % 12]
nam_duong = 2017
print("Năm âm lịch tương ứng với năm dương lịch", nam_duong, "là", am_lich(nam_duong))

#9.3
def bmi(chiều_cao: float, cân_nặng: float) -> float:
    return cân_nặng / (chiều_cao *chiều_cao)
chiều_cao= float(input("Nhập chiều cao của bạn (m): "))
cân_nặng = float(input("Nhập cân nặng của bạn (kg): "))
bmi_value = bmi(chiều_cao, cân_nặng)
print(f"Chỉ số BMI của bạn là {bmi_value:.2f}")
if bmi_value < 18.5:
    print("Bạn bị gầy!")
elif bmi_value < 25:
    print("Bạn đang bình thường!")
elif bmi_value < 30:
    print("Bạn bị thừa cân")


#9.4
n=float(input("Nhập vào một số n:"))
x=int(input("Nhập vào một số x:"))
S=(x**2+1)**n
print("Kết quả trả về =",S)

#9.5
n=float(input("Nhập vào một số n:"))
x=int(input("Nhập vào một số x:"))
A=(x**2+x+1)**n+(x**2-x+1)**n
print("Kết quả trả về =", S)

#9.6
def so_nguyen_to(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True
x = int(input("Nhập một số: "))
if so_nguyen_to(x):
    print(x,"là số ngueyen tố")
else:
    print(x, "không phải là số nguyên tố.")

#9.7
def phần_nguyên(a,b)->int:
    return a//b
a=int(input("nhập vào một số a :"))
b=int(input("Nhập vào một số b :"))
print("phần nguyên của hai số",a ,b ,"là ")


