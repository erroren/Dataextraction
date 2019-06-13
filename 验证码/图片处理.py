import pytesseract
from PIL import Image
import time

image = Image.open('./z.png')
# text = pytesseract.image_to_string(image, lang='chi_sim')
# print(text)
image.show()

gray = image.convert('L')
gray.show()

bw = gray.point(lambda x: 0 if x< 155 else 255, '1')
bw.show()
strcode = pytesseract.image_to_string(bw)
print(strcode,type(strcode))