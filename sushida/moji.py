from PIL import Image
import sys
import pyocr
import pyocr.builders

def moji(a):
    tools = pyocr.get_available_tools()
    tool = tools[0]

    langs = tool.get_available_languages()
    lang = langs[0]
    #txtに変換した文字列を代入する
    txt = tool.image_to_string(
        Image.open(a + '.png'),
        lang="eng",
        builder=pyocr.builders.TextBuilder(tesseract_layout=6)
    )
    Text = list(txt)   #文字列を配列に変換
    count = len(Text)
    i = 0


    txt = str(''.join(Text))   #文字列に戻す
    return txt