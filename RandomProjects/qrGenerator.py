import cv2
import qrcode

qr = qrcode.QRCode(version = 1, error_correction= qrcode.constants.ERROR_CORRECT_L,
                    box_size = 30,
                    border=3)

qr.add_data("whats your question?")
qr.make(fit=True)

img = qr.make_image(fill_color = "white", back_color = "red")
img.save("qrcode1.png")


# d = cv2.QRCodeDetector()
# val, points, straight_qrcode = d.detectAndDecode(cv2.imread("qr.png"))
# print(val)


