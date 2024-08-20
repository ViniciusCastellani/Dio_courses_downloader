import os
import yt_dlp
import time
import pyautogui
import pyperclip
from bs4 import BeautifulSoup


urls = []


def get_origin_path():
    if os.name == 'nt':  # Windows
        disk = input("Enter the drive letter where you want to save the videos (e.g., D): ")
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
    try:
        os.chdir("'" + user_input + "'")
        print("Directory changed successfully.")
    except FileNotFoundError:
        print("This directory does not exist.")


def download_videos(urls, output_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': os.path.join(output_path, '%(title)s.%(ext)s')
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for url in urls:  
            try:
                ydl.download(url)
            except Exception as e:
                print(f"Error downloading the video: {e}")


def play_stop_video():
    # Play and stop the video to get the hidden video link
    time.sleep(2)
    pyautogui.click(580, 313)
    time.sleep(4)
    pyautogui.click(580, 313)


def open_developer_tools():
    time.sleep(2)
    pyautogui.hotkey("ctrl", "shift", "i")
    time.sleep(2)


def get_html():
    time.sleep(2)
    pyautogui.rightClick(163, 693)
    time.sleep(2)
    pyautogui.click(276, 553)
    time.sleep(2)
    pyautogui.click(566, 589)
    html = pyperclip.paste()
    return html


def get_subject_name(html):
    """
    Dentro de um SPAN
    class="sc-cWSHoV jmOqli"
    """
    soup = BeautifulSoup(html, 'lxml')

    span = soup.find('span', class_ = "sc-cWSHoV jmOqli")
    subject_name = span.text
    return subject_name


def get_video(html):
    """
    Ex: link = src="https://www.youtube.com/embed/LOyFqTVqEXE?controls=0&disablekb=1&enablejsapi=1&fs=0&iv_load_policy=3&modestbranding=1&showinfo=0&rel=0&html5=1&cc_load_policy=0&origin=https%3A%2F%2Fweb.dio.me&widgetid=1"
    """
    
    soup = BeautifulSoup(html, 'lxml')
    iframe = soup.find(get_iframe_src)

    if iframe:
        video_link = iframe['src']
        return video_link
    else:
        print("Youtube video not found")


def get_iframe_src(iframe):
    return iframe.has_attr('src') and iframe['src'].startswith("https://www.youtube.com/embed/")


def change_video():
    time.sleep(2)
    pyautogui.click(1236, 396)


def menu():
    institution = input("Enter the name of the institution: ")
    root_path = get_origin_path()
    change_directory(root_path)
    create_folder(os.path.join(root_path, institution))
    change_directory(os.path.join(root_path, institution))

    current_path = os.path.join(root_path, institution)

    course_name = input("Enter the name of the course: ")
    create_folder(os.path.join(current_path, course_name))
    change_directory(os.path.join(current_path, course_name))

    current_path = os.path.join(current_path, course_name)

    print("Now go to the course website and be on the lesson you want to download.")
    input("Done? Press any key to continue...")
    print("Now minimize this terminal and maximize the web browser window\n")
    time.sleep(4)
    return current_path
    

def main():
    menu()
    play_stop_video()
    time.sleep(4)
    open_developer_tools()
    time.sleep(2)
    html = get_html()    

    subject_name = get_subject_name(html)    
    create_folder(os.path.join(current_path, subject_name))
    change_directory(os.path.join(current_path, subject_name))

    current_path = os.path.join(current_path, subject_name)
    
    while True:
        time.sleep(2)
        play_stop_video()
        video_link = get_video(html)

        urls.append(video_link)

        pyautogui.hotkey("alt", "tab")

        response = input("Do you want to continue? [Y/N]")

        if response.lower() == "y":
            change_video()
            time.sleep(5)
            play_stop_video()
        
        if response.lower() == "n":
            break

        html = get_html()
        
    download_videos(urls, current_path)

    
if __name__ == "__main__":
    main()