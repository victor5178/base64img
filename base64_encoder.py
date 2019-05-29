import base64
chqno = input("Input Cheque Number : ")
imgbwb64 = input("Input imgbwb : ")
imgbwf64 = input("Input imgbwf : ")


decoded_string_b = base64.b64decode(imgbwb64)
with open(chqno+"_B.jpg", "wb") as image_file2:
 image_file2.write(decoded_string_b);

decoded_string_f = base64.b64decode(imgbwf64)
with open(chqno+"_F.jpg", "wb") as image_file3:
 image_file3.write(decoded_string_f);

print("Completed...")

