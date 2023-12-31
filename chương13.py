#1
ten_tap_tin=input("nhập tên tập tin:")
with open('HumptyDumpty.txt','w', encoding='utf-8') as f:
    print("nội dung tập tin:")
    f.write("Humpty Dumpty sat on a wall, \n")
    f.write("Humpty Dumpty had a great fall. \n")
    f.write("All the king's horses and all the king's men \n")
    f.write("Couldn't put Humpty together again. \n")
f=open("HumptyDumpty.txt",'r')
content=f.read()
print(content)
f.close

#2
ten_noi_dung=input("nhập tên nội dung:")
print("Content of file:")
f=open("HumptyDumpty.txt",'r')
noi_dung=f.read()
print(noi_dung)
so_dong=len(noi_dung.splitlines())
so_tu=len(noi_dung.split())
so_ki_tu=len(noi_dung)
print('-----Report:Lines/ Words/ Chars-----')
print('lines:',so_dong,'words:',so_tu,'chars:',so_ki_tu)
f.close

#3
ten_tap_tin=input("nhập tên tập tin:")
with open("Rain.txt",'w',encoding='utf-8') as f:
    print("nhập nội dung")
    f.write("Rain rain, go away; Come again another day...\n")
f=open("Rain.txt",'r')
noi_dung=f.read()
print(noi_dung)
print("đã ghi nội dung vào tập tin Rain.txt")
print("Rain rain, go away; Come again another day...")
f.close 

#4
n=input("Nhập tên tập tin:")
def doc_file():
    while True:
        nd=input('Nhập nội dung:')
        with open('JohnnyJohnny.txt','a') as file:
                file.write(nd+'\n')
        x=int(input('Bạn có muốn tiếp tục ghi nội dung vào file? 1: Có,0: Không   '))
        if x == 1:
            continue
        elif x == 0:
            with open('JohnnyJohnny.txt','r') as file:
                doc=file.read()
                print("Đã ghi nội dung vào tập tin JohnnyJohnny.txt")
                print(doc)
            break
doc_file()

#5
a=input("Nhập tên tập tin:")
from csv import reader
with open('Menu.csv','r') as read_obj:
    csv_reader = reader(read_obj)
    for row in csv_reader:
        print(row)

#6
a=input("nhập tên tập tin:")
from csv import reader
with open('dienthoai.csv','r') as read_obj:
    read_obj=open('dienthoai.csv','r')
    row=read_obj.read()
    print(row)



