import qrcode
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4,
)
data = 'https://www.fdp-pankow.de/wp-content/uploads/Bezirkswahlprogramm_final.pdf'
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")
img.save('Wahlprogram_Pankow.png')
