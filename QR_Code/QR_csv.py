import qrcode
from csv import DictReader
  
with open('my_plants.csv', 'r') as read_obj:
    csv_dict_reader = DictReader(read_obj, delimiter=',')
    for row in csv_dict_reader:
        #print(row)
        print(row['Name'], row['Details'])
        data = row['Details']
        qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=5,
    border=4)
        qr.add_data(data)
        qr.make(fit=True)
        img = qr.make_image(fill_color="green", back_color="pink")
        img.save(row['Name'] + '.png') 
