import keyboard
import time

i = 1
text = input("Enter the text you want to spam: ")
x = int(input("Now specify how many times your text should be sent: "))
print("You now have 5 seconds to click into the text box where the text is to be entered.")

time.sleep(5)
while i <= x:
 keyboard.write(text)
 keyboard.press_and_release('enter')
 i += 1
 print("ok")