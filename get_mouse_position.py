import pyautogui
import time

def get_mouse_position():
    # Aguardar 3 segundos para o usuário posicionar o cursor
    time.sleep(6)
    x, y = pyautogui.position()
    print(f"Cursor position: ({x}, {y})")

def main():
    for i in range(11):
        get_mouse_position()

    


main()

"""
619, 624
81, 549
631, 342
174, 815
187, 928
527, 865
667, 725
1059, 759
"""


"""
institution = input("What is the institution of the course: ")
    path = input("Insert the path where you want to store the videos: ")
    url = input("Please insert the URL of the lesson that you want to download: ")
    print("Be sure that you are logged in on the webpage and on the URL of the lesson.")

    pyautogui.click(659, 643)
    time.sleep(1)
    pyautogui.click(659, 643)
"""