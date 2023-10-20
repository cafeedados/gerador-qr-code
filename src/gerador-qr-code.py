import qrcode
from PIL import Image


#capiturar a imagem e colocar ao centro do QR Code
logo_img = Image.open('img/Logo-Brazucabet.png')


# pegar o tam

# taking base width
basewidth = 300
  
# adjust image size
wpercent = (basewidth/float(logo_img.size[0]))
hsize = int((float(logo_img.size[1])*float(wpercent)))
logo = logo_img.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H
)
  
# taking url or text
url = 'https://brazucabet.online/hub/signup?affiliate='
  
# addingg URL or text to QRcode
QRcode.add_data(url)
  
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
  
# save the QR code generated
QRimg.save('gfg_QR.png')
  
print('QR code generated!')