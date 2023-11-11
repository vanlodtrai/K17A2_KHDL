def e_mu_x(x, sai_so, n=0, ket_qua=1):
    # Nếu sai số đã đạt được, hoặc n vượt quá một ngưỡng cố định (để tránh lặp vô hạn)
    if abs(x**n / factorial(n)) < sai_so or n > 100:
        return ket_qua
    else:
        n += 1
        ket_qua += x**n / factorial(n)
        return e_mu_x(x, sai_so, n, ket_qua)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

x = float(input("Nhập giá trị của x: "))
sai_so = 1e-4
ket_qua = e_mu_x(x, sai_so)
print(f"e^{x} gần đúng với sai số {sai_so} là: {ket_qua}")