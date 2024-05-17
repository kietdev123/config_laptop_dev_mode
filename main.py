import pyautogui
import time
import json

# Các thao tác thủ công
# https://www.thegioididong.com/hoi-dap/may-tinh-bi-cham-phai-lam-sao-day-la-cach-khac-phu-1066442

_maxPeformance = "max"
_minPeformance = "min"

def saveData(state):
    dictionary = {
        "statePerformace" : state
    }
    
    # Serializing json
    json_object = json.dumps(dictionary, indent=1)
    
    # Writing to sample.json
    with open("data.json", "w") as outfile:
        outfile.write(json_object)

def readData():
    with open('data.json', 'r') as openfile:
        # Reading from json file
        json_object = json.load(openfile)

    return json_object
      
def delete_unused_data():
    print('Staring...')
    # # Chờ một chút để đảm bảo mọi thứ đã sẵn sàng
    # time.sleep(2)

    # # Xóa tập tin rác

    # # Nhấn tổ hợp phím Windows + R để mở hộp thoại Run
    # pyautogui.hotkey('win', 'r')
    # # Chờ một chút để hộp thoại Run mở ra
    # time.sleep(1)
    # # Điền vào thông tin cần thiết (ví dụ: notepad)
    # pyautogui.write('%temp%')
    # # Nhấn Enter để chạy lệnh
    # pyautogui.press('enter')
    # time.sleep(1)
    # pyautogui.hotkey('ctrl', 'a')
    # time.sleep(1)
    # pyautogui.press('delete')


    # Chờ một chút để đảm bảo mọi thứ đã sẵn sàng
    time.sleep(2)

    # Bước 1: Mở thanh tìm kiếm Windows (Windows + S)
    pyautogui.hotkey('win', 's')
    time.sleep(1)

    # Nhập từ khóa "Advanced"
    pyautogui.write('View advanced system settings')
    time.sleep(1)

    # Chọn "View advanced system settings" (Giả sử nó là mục đầu tiên trong danh sách)
    # pyautogui.press('down')  # di chuyển đến kết quả tìm kiếm đầu tiên
    pyautogui.press('enter')  # mở mục đó

    # Chờ để cửa sổ mở ra
    # time.sleep(2)
    # currentMouseX, currentMouseY = pyautogui.position()
    # print(currentMouseX, currentMouseY)

    # screenWidth, screenHeight = pyautogui.size()
    # print(screenWidth, screenHeight)
    # time.sleep(3)
    # while True:
        # time.sleep(2)
        # pyautogui.press('tab')
    # pyautogui.press('enter')
    time.sleep(3)
    # pyautogui.press('\n', presses=3)
    # pyautogui.typewrite(["enter"])
    # time.sleep(1)
    # pyautogui.click(446, 265, 1) # Move the mouse to XY coordinates.
    # time.sleep(1)
    # pyautogui.doubleClick()



    print('Done')       
    # pyautogui.alert('Done delete unused data')

def configSystemPerformance(type, data):
    # Chờ một chút để đảm bảo mọi thứ đã sẵn sàng
    time.sleep(2)

    # Bước 1: Mở thanh tìm kiếm Windows (Windows + S)
    pyautogui.hotkey('win', 's')
    time.sleep(1)

    # Nhập từ khóa "Advanced"
    pyautogui.write('View advanced system settings')
    time.sleep(1)
    pyautogui.press('enter')

    if (type == 'max'):
        if (data["statePerformace"] == _minPeformance):
            # Chọn "View advanced system settings" (Giả sử nó là mục đầu tiên trong danh sách)
            time.sleep(1)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('down')  
            time.sleep(1)
            pyautogui.press('down')  
            time.sleep(1)
            pyautogui.press('enter') 
           

    if (type == 'min'):
        if (data["statePerformace"] == _maxPeformance):
            # Chọn "View advanced system settings" (Giả sử nó là mục đầu tiên trong danh sách)
            time.sleep(2)
            pyautogui.press('enter')
            time.sleep(1)
            pyautogui.press('up', presses=2)   
            time.sleep(1)
            pyautogui.press('enter')  
            

    #close
    time.sleep(3)
    pyautogui.press('tab', presses=4)
    pyautogui.press('enter') 

def configPowerPerformance(type, data):
    # Chờ một chút để đảm bảo mọi thứ đã sẵn sàng
    time.sleep(2)

    # Bước 1: Mở thanh tìm kiếm Windows (Windows + S)
    pyautogui.hotkey('win', 'i')
    time.sleep(1)

    time.sleep(1)
    pyautogui.press('tab')
    time.sleep(1)
    pyautogui.press('enter')

    time.sleep(1)
    pyautogui.click(123, 418, 1)
    time.sleep(3)
    pyautogui.moveTo(1146, 137, 0)
    time.sleep(1)
    pyautogui.click()

    # pyautogui.press('tab', presses=5)  
    # time.sleep(1)
    # pyautogui.press('enter')  

    time.sleep(1)
    pyautogui.press('right')
    pyautogui.press('tab')
    pyautogui.press('down')

    if (type == 'max'):
        if (data["statePerformace"] == _minPeformance):
            time.sleep(2)
            pyautogui.press('down')
           
    if (type == 'min'):
        if (data["statePerformace"] == _maxPeformance):
            time.sleep(2)
            pyautogui.press('up')

def maxPeformance(data):
    configSystemPerformance('max',data)
    configPowerPerformance('max', data)
    saveData(_maxPeformance) 

    print('Done')       
    pyautogui.alert('Done set up maxPeformace')
   
def normalPeformace(data):
    configSystemPerformance('min', data)
    configPowerPerformance('min', data)
    saveData(_minPeformance)

    print('Done')   
    pyautogui.alert('Done set up normalPeformace')

def getMouseLocation():
    print('Press Ctrl-C to quit.')
    try:
        while True:
            x, y = pyautogui.position()
            positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
            print(positionStr, end='')
            print('\b' * len(positionStr), end='', flush=True)
    except KeyboardInterrupt:
        print('\n')

def show_menu(data):
    print("Welcome to config console Python application")
    print("=> Current config performance " + data["statePerformace"])
    print("1. Config max performance")
    print("2. Config min performance")
    print("3. Get mouse position")
    print("4. Exit")

def main():
    oldData = readData()

    # delete_unused_data()

    show_menu(oldData)
    choice = input("Input number (1,2,3,4): ")
        
    if choice == '1':
        maxPeformance(oldData)
    elif choice == '2':
        normalPeformace(oldData)
    elif choice == '3':
        getMouseLocation()
    elif choice == '4':
        print("Exit, bye")
    else:
        print("Try again")
        
main()