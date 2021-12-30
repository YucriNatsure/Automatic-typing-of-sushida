import time
import pyautogui as pa
import moji

start = time.time()
nowtime =time.time()
pa.press("enter")

while True:
    if time.time() - nowtime > 1.5:
        break

i=0

while True:
    if time.time()  - nowtime > 300:
        break
    img  = pa.screenshot(
        imageFilename = "sushidashot"+str(i)+".png",
        region=(300,534,400,35)
    )
    string = moji.moji("sushidashot"+str(i))
    pa.typewrite(string,interval=0.0)
    print(string)
    nowtime1 = time.time()
    while True:
        if time.time() - nowtime1 > 0.25:
            break
    i =+ 1