import qrcode

class Qr:
    def __init__(self , size:int , padding:int):
        self.qr = qrcode.QRCode(box_size=size , border=padding)

    def create_qr(self, filename:str ,fg:str,bg:str ):
        data :str = input("Enter some text: ")
        try:
            self.qr.add_data(data)
            self.qr.make()
            self.image =self.qr.make_image(fill_color = fg , back_color = bg)
            self.image.save(filename)
            print(f"Succesfully created {filename}")
        except Exception as e:
            print("Error {e} has accord")

def main():
    qr = Qr(size =30 ,padding = 2)
    qr.create_qr("Qr.png" , fg=(255, 80,50) , bg="White")

if __name__ =="__main__":
    main()