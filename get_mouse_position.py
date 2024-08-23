import pyautogui
import time

def get_mouse_position():
    # Wait 6 seconds to get the mouse position
    time.sleep(6)
    x, y = pyautogui.position()
    print(f"Cursor position: ({x}, {y})")

def main():
    for i in range(11):
        get_mouse_position()

    
if __name__ == "__main__":
    main()
