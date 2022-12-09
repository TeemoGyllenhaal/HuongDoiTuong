from Student import SinhVien
def main():
    sv = [SinhVien('Lê Quý Minh Quang',2004,10),SinhVien('Lê Hoàng Minh Quý',2004,9),SinhVien('Lê Văn Đạt',1999,100)]
    for item in sv:
        print(item)
if __name__ == '__main__':
    main()