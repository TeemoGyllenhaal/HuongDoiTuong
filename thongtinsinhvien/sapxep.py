from student import SinhVien

x = [-1,-5,-9,8,3,4,2]
x = sorted(x)
print(x)
x = sorted(x, reverse = True)
print(x)
def main():
    sv = [SinhVien('Lê Quý Minh Quang',2004,10),SinhVien('Lê Hoàng Minh Quý',2004,9),SinhVien('Lê Văn Đạt',1999,100),SinhVien('Lê Văn Thân',1999,150),SinhVien('Lê Văn Nghĩa',1989,200)]
    sv = sorted (sv)
    for item in sv:
        print(item)
if __name__ == '__main__':
    main()