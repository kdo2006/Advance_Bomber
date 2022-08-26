import pyautogui
import time
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Advance Bomber by K.D.O")
print(ascii_banner)


msg = input("Message: ")
n = input("Amount: ")

print("Bombing starts in 5 second")
count = 5
while(count != 0):
	print(count)
	time.sleep(1)
	count -= 1

print("Started")

for i in range(0,int(n)):
	pyautogui.typewrite(msg + '\n')

