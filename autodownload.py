import pyautogui
import time
# import cv2

button_slowDL = 'slowDL.jpg'
ogMousePos = pyautogui.position()

def returnMouse():
    # Move the mouse cursor back to the original position
    pyautogui.moveTo(ogMousePos)
 
def goforit():
    total_buttons = 338
    buttons_found = 0
    start_time = time.time()

    while buttons_found < total_buttons:
        print(f"Looking for button ({buttons_found + 1}/{total_buttons}): SLOW DL...")
        location_SLOWDL = None
        while not location_SLOWDL:
            try:
                location_SLOWDL = pyautogui.locateCenterOnScreen(button_slowDL, confidence=0.88)
            except:
                pass
            print('.')
            time.sleep(0.1)

        buttons_found += 1
        elapsed_time = time.time() - start_time
        #print(f"Found button! (SLOW DL) - Time taken: {elapsed_time:.2f} seconds")
        print(location_SLOWDL)

        pyautogui.moveTo(location_SLOWDL)
        pyautogui.doubleClick()
        current_x, current_y = location_SLOWDL
        pyautogui.moveTo(current_x + 420, current_y)
        time.sleep(0.1)

    returnMouse()

def main():
    goforit()

if __name__ == "__main__":
    main()
