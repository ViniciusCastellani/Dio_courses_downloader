import os
import yt_dlp
import time
import pyautogui
import pyperclip
from bs4 import BeautifulSoup


urls = []


def get_origin_path():
    if os.name == "nt":  # Windows
        disk = input(
            "Enter the drive letter where you want to save the videos (e.g., D): "
        )
        change_directory(disk + ":")
        root_path = input("Enter the path where you want to save the videos: ")
        change_directory(root_path)
        return root_path
    
    else:  # Linux
        root_path = input("Enter the path where you want to save the videos: ")
        return root_path


def create_folder(path):
    os.makedirs(path, exist_ok=True)


def change_directory(user_input):
    if os.path.isdir(user_input):
        try:
            os.chdir(user_input)
        except OSError as e:
            print(f"An error ocurried while changing directories: {e}")
    else:
        print("This directory does not exist")


def download_videos(urls, output_path):
    ydl_opts = {
        "format": "best",
        "outtmpl": os.path.join(output_path, "%(title)s.%(ext)s"),
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:
            try:
                ydl.download(url)
            except Exception as e:
                print(f"Error downloading the video: {e}")


def get_images_diretory():
    browser = input("\nWhat browser are you using? ").lower()
    base_dir = os.path.dirname(__file__)
    images_directory = os.path.join(base_dir, "images", browser)
    return images_directory, browser


def init_image_list(images_directory):
    images_path = {
        "html": [],
        "play_button": [],
        "outer_html": [],
        "copy": [],
        "change_video": [],
    }

    image_extension = ".png"

    for filename in os.listdir(images_directory):
        if os.path.splitext(filename)[1].lower() == image_extension:
            if str(filename).lower().startswith("html"):
                images_path["html"].append(os.path.join(images_directory, filename))

            elif str(filename).lower().startswith("copy"):
                images_path["copy"].append(os.path.join(images_directory, filename))

            elif str(filename).lower().startswith("outer"):
                images_path["outer_html"].append(
                    os.path.join(images_directory, filename)
                )

            elif str(filename).lower().startswith("next"):
                images_path["change_video"].append(
                    os.path.join(images_directory, filename)
                )

            elif str(filename).lower().startswith("play"):
                images_path["play_button"].append(os.path.join(images_directory, filename))

    return images_path


def locate_and_click(image_path, right_click, grayScale=True):
    try:
        location = pyautogui.locateCenterOnScreen(
            image_path, grayscale=grayScale, confidence=0.7
        )

        if location is not None:
            x, y = location
            if right_click:
                pyautogui.rightClick(location)
            else:
                pyautogui.click(location)
            return {"x": x, "y": y}
        else:
            return None
    except Exception as e:
        return None


def locate_and_click_multiple_files(images_paths, right_click, grayScale=True):
    location = None
    for image_path in images_paths:
        location = locate_and_click(image_path, right_click, grayScale)
        if location is not None:
            return location

    if location is None:
        print(f"image not found on screen")


def play_stop_video(images_path):
    # Play and stop the video to get the hidden video link
    # time.sleep(2)
    # pyautogui.click(580, 313)
    # time.sleep(4)
    # pyautogui.click(580, 313)
    location = locate_and_click_multiple_files(images_path["play_button"], False)
    time.sleep(5)
    if location:
        x, y = location["x"], location["y"]
        pyautogui.click(x, y)


def open_developer_tools():
    pyautogui.hotkey("ctrl", "shift", "i")


def get_html(images_path):
    # time.sleep(2)
    # pyautogui.rightClick(163, 693) # right clicks on the html code to copy the whole html
    # time.sleep(2)
    # pyautogui.click(276, 553) # clicks in copy
    # time.sleep(2)
    # pyautogui.click(566, 589) # clicks in "outter html"

    time.sleep(1)
    location = locate_and_click_multiple_files(images_path["html"], True)
    time.sleep(1)
    location = locate_and_click_multiple_files(images_path["copy"], False)
    time.sleep(1)
    location = locate_and_click_multiple_files(images_path["outer_html"], False)

    html = pyperclip.paste()
    return html


def get_subject_name(html):
    """
    The text is inside of an SPAN which has
    class="sc-cWSHoV jmOqli"
    """

    soup = BeautifulSoup(html, "lxml")
    span = soup.find("span", class_="sc-cWSHoV jmOqli")
    subject_name = span.text
    return subject_name


def get_video(html):
    """
    Ex: link = src="https://www.youtube.com/embed/..."
    """

    soup = BeautifulSoup(html, "lxml")
    iframe = soup.find(get_iframe_src)

    if iframe:
        video_link = iframe["src"]
        return video_link
    else:
        print("Youtube video not found")


# function that sets the iframe in the soup.find function that has 'src'
# and the content of src starts with the youtube link
def get_iframe_src(iframe):
    return iframe.has_attr("src") and iframe["src"].startswith(
        "https://www.youtube.com/embed/"
    )


def change_video(images_path):
    #   pyautogui.click(1236, 396) # clicks in the right arrow of the video
    location = locate_and_click_multiple_files(
        images_path["change_video"], False, False
    )


def menu():
    institution = input("Enter the name of the institution: ")
    root_path = get_origin_path()
    change_directory(root_path)

    create_folder(os.path.join(root_path, institution))
    current_path = os.path.join(root_path, institution)
    change_directory(current_path)

    course_name = input("Enter the name of the course: ")
    create_folder(os.path.join(current_path, course_name))
    current_path = os.path.join(current_path, course_name)
    change_directory(current_path)

    print("\nNow go to the course website and be on the lesson you want to download.")
    time.sleep(3)
    input("Done? Press any key to continue...")
    print("\nNow minimize this terminal and maximize the web browser window\n\n")
    return current_path


def main():
    images_directory, browser = get_images_diretory()
    images_paths = init_image_list(images_directory)

    current_path = menu()
    time.sleep(6)
    play_stop_video(images_paths)
    time.sleep(3)
    open_developer_tools()
    time.sleep(3)
    html = get_html(images_paths)

    subject_name = get_subject_name(html)
    create_folder(os.path.join(current_path, subject_name))
    current_path = os.path.join(current_path, subject_name)
    change_directory(current_path)

    while True:
        time.sleep(3)
        video_link = get_video(html)

        urls.append(video_link)

        pyautogui.hotkey("alt", "tab")

        response = input("\nDo you want to continue? [Y/N]: ")

        if response.lower() == "y":
            # print("Go to the next video! and minimize this terminal")
            # time.sleep(10)
            # open_developer_tools()
            # time.sleep(3)
            # play_stop_video(images_paths)
            # time.sleep(3)
            # open_developer_tools()
            # time.sleep(1)
            print("Minimize this terminal and go to the course")
            time.sleep(6)
            open_developer_tools()
            time.sleep(4)
            change_video(images_paths)
            time.sleep(7)

        if response.lower() == "n":
            break

        play_stop_video(images_paths)
        time.sleep(4)
        open_developer_tools()
        time.sleep(2)

        html = get_html(images_paths)

    download_videos(urls, current_path)


if __name__ == "__main__":
    main()
