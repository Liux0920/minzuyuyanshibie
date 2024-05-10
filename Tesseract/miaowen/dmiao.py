import pytesseract
from PIL import Image
# 指定tesseract-OCR.安装目录
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 加载图像
img=Image.open('dmiao.png')
# 执行ocr
text=pytesseract.image_to_string(img,lang='eng')
# 打印识别文字
with open ('dmiao.txt', 'w', encoding='utf-8')as file:
    file.write(text)
# 将识别的文字保存在文档
print("本文已保存在 dmiao.txt 文件中")

img=Image.open('smiao.png')
# 执行ocr
text=pytesseract.image_to_string(img,lang='eng+chi_sim')
# 打印识别文字
with open ('smiao.txt', 'w', encoding='utf-8')as file:
    file.write(text)
# 将识别的文字保存在文档
print("本文已保存在 smiao.txt 文件中")