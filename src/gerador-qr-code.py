import qrcode
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw


def gerar_qr_code(word, uri, logo_uri='img/Logo-Brazucabet.png'):
    

    #capiturar a imagem e colocar ao centro do QR Code
    logo_img = Image.open(logo_uri)

    # taking base width
    basewidth = 300
    
    # adjust image size
    wpercent = (basewidth/float(logo_img.size[0]))
    hsize = int((float(logo_img.size[1])*float(wpercent)))
    logo = logo_img.resize((basewidth, hsize), Image.ANTIALIAS)
    QRcode = qrcode.QRCode(
        error_correction=qrcode.constants.ERROR_CORRECT_H
    )

    # addingg URL or text to QRcode
    QRcode.add_data(uri)
    
    # generating QR code
    QRcode.make()
    
    # Escolher a cor do QR Code
    QRcolor = 'Blue'
    
    # adding color to QR code
    QRimg = QRcode.make_image(
        fill_color=QRcolor, back_color="white").convert('RGB')
    
    # set size of QR code
    pos = ((QRimg.size[0] - logo.size[0]) // 2,
        (QRimg.size[1] - logo.size[1]) // 2)
    QRimg.paste(logo, pos)

    # Abrir para sobreposição
    draw = ImageDraw.Draw(QRimg)

    # Setar Fonte que quero usar
    fonte  = ImageFont.truetype('fonts/COOLVETICAHV-ITALIC.TTF', 25)

    #sobrepor da imagem algum texto
    draw.text((160, 455), word, (0,0,0), font=fonte)

    #salvar a imagem
    QRimg.save(f'qrcode_{word.replace(" ", "_")}.png')




if __name__ == '__main__':
    gerar_qr_code('Venha jogar!', 'https://brazucabet.online/hub/signup?affiliate=')