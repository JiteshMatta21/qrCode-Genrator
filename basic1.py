#importing qrcode library to generate QR codes
import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=2)

var1=input("Add data to this:\n")

features.add_data(var1)
features.make(fit=True)

generate_img=features.make_image(fill_coor="black",back_color="white")

save_name=input("Give name to save file:\n")

#provide save location to file
generate_img.save('D:\projects\python\qrCodeGen\img\qr'+save_name+'.png')