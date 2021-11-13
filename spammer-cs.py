import keyboard
import time

i = 1
text = input("Zadejte text, co chcete napsat: ")
x = int(input("Nyní zadejte, kolikrát se má váš text odeslat: "))
print("Nyní máte 5 sekund na překliknutí do textového pole, kam se má text zadávat.")

time.sleep(5)
while i <= x:
 keyboard.write(text)
 keyboard.press_and_release('enter')
 i += 1
 print("ok")