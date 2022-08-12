import pyautogui
import time
import socket

host_name = socket.gethostname()
ip_addr = socket.gethostbyname(host_name)
ip_addr_list = ip_addr.split(".")

for i in range(0, len(ip_addr_list)):
    ip_addr_list[i] = int(ip_addr_list[i])

print(ip_addr_list)
print(type(ip_addr_list))

pyautogui.click(pyautogui.locateCenterOnScreen('.\images\ivms-client.png', confidence=.5), clicks=2)
time.sleep(0.8)

pyautogui.moveTo(pyautogui.locateOnScreen(r'.\images\server-ip.png', confidence=.5))
pyautogui.moveRel(0, 40)

for i in range(0, len(ip_addr_list)):
    pyautogui.click(clicks=2)
    x = ip_addr_list[i]
    print(x)
    pyautogui.write(str(x))
    # time.sleep(1)
    pyautogui.moveRel(80, 0)


pyautogui.moveTo(pyautogui.locateOnScreen(r'.\images\username.png', confidence=.5))
# time.sleep(1)
pyautogui.moveRel(0, 40)
pyautogui.click()
pyautogui.write('admin')

pyautogui.moveTo(pyautogui.locateOnScreen(r'.\images\password.png', confidence=.5))
#time.sleep(1)
pyautogui.moveRel(0, 40)
pyautogui.click()
pyautogui.write('Admin@123')

# time.sleep(1.2)
pyautogui.click(pyautogui.locateCenterOnScreen(r'.\images\login.png', confidence=.5), clicks=2)
# pyautogui.click(ivmsWidth, ivmsHeight)