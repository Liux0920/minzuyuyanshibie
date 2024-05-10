import pytesseract
from PIL import Image
# 指定tesseract-OCR.安装目录
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'
# 加载图像
img=Image.open('dchao.png')
# 执行ocr
text=pytesseract.image_to_string(img,lang='kor')
# 打印识别文字
with open ('dchao.txt', 'w', encoding='utf-8')as file:
    file.write(text)
# 将识别的文字保存在文档
print("本文已保存在 dchao.txt 文件中")
img=Image.open('schao.png')
# 执行ocr
text=pytesseract.image_to_string(img,lang='kor+chi_sim')
# 打印识别文字
with open ('schao.txt', 'w', encoding='utf-8')as file:
    file.write(text)
# 将识别的文字保存在文档
print("本文已保存在 schao.txt 文件中")

