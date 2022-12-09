class SinhVien:
    def __init__(self,fullname,age,score):
        self.hoten = fullname
        self.namsinh = age
        self.dtb = score
    def __str__(self):
        message = '[hoten: '+ self.hoten +'; namsinh: '+ str(self.namsinh)+'; dtb: '+ str(self.dtb) +']'
        return message
def main():
    #Nhập thông tin 
    sv1 = SinhVien('Lê Quý Minh Quang',2004,10)
    sv2 = SinhVien('Lê Hoàng Minh Quý',2004,9)
    print(sv1)
    print(sv2)
if __name__ == '__main__':
    main()