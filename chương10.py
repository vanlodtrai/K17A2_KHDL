10.1
print(max(40,20,100))
print(min(10,999,3900))

10.2
x=int(input("Nhập vào đây một số: "))
print(abs(x))

10.3
x=int(input("nhập x:"))
n=int(input("nhập n:"))
print("S=",pow(x,2)+1*n)

10.4
x=int(input("nhập x:"))
n=int(input("nhập n:"))
print("s=",pow(pow(x,2)+x+1,n)+pow(pow(x,2)-x+1,n))

10.5

10.6
from math import sqrt
a=float(input("Nhập một số tuỳ í: "))
b=float(input("Nhập một số tuỳ í thứ 2: "))
c=float(input("Nhập một số tuỳ í thứ 3: "))
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình vô số nghiệm!")
        else:
            print("Phương trình vô nghiệm!")
    else:
        if c == 0:
            print("Phương trình có 1 nghiệm x = 0")
        else:
            print("Phương trình có 1 nghiệm x = ", -c / b)
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm!")
    elif delta == 0:
        print("Phương trình có 1 nghiệm x = ", -b / (2 * a))
    else:
        print("Phương trình có 2 nghiệm phân biệt!")
        print("x1 = ", float((-b - sqrt(delta)) / (2 * a)))
        print("x2 = ", float((-b + sqrt(delta)) / (2 * a)))

10.7
str1 = " a b c d e f duck "
str2 = "duck"
print("Nhập chuỗi S:",str1)
print("Nhập chuỗi tìm S_find:",str1.find(str2))
print("Số lần S_sub xuất hiện trong S:",str1.count("d"))
print("Chuỗi S sau khi loại bỏ khoảng trắng ở đầu và cuối chuỗi:",str1.strip())
print("Chuỗi S sau khi thay thế:",str1.replace("duck","dog"))

10.8
import datetime
ngay=int(input("Nhập ngày:"))
thang=int(input("Nhập tháng:"))
nam=int(input("Nhập năm:"))
ngay_hop_le=True
if ngay_hop_le:
    ngay_thang_nam=datetime.datetime(nam,thang,ngay)
    ngay_formatted=ngay_thang_nam.strftime("%d-%m-%Y")
    print("Ngày:",ngay_formatted)
    if nam%4==0 and (nam % 100!=0 or nam %400==0):
        print("Là năm nhuận")
    else:
        print("Không phải năm nhuận")
    thu=ngay_thang_nam.strftime("%A")
    print("Ngày/tháng/năm đó là thứ:",thu)
    so_ngay=(datetime.datetime(nam,thang+1,1)-datetime.datetime(nam,thang,1)).days
    print("Tháng",thang,"có",so_ngay,"ngày.")
else:
    print("Ngày tháng năm không hợp lệ!!!")

10.9





