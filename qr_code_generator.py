import qrcode
import generator


def create_qrcode():
    # used previous project to get data
    data = generator.rand_psw()
    print(data)
    # create qr code
    filename = 'qr_code_psw.png'
    img = qrcode.make(data)
    img.save(filename)


if __name__ == '__main__':
    create_qrcode()
    