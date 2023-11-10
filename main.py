from vids_download import Downloader
from colorama import Fore as f
import pyfiglet
import os

def main() -> None:
    print(f.GREEN + pyfiglet.figlet_format("Youtube Uploader"))
    print(f.RED + "By : Ahmad Odeh aka undefined010")
    print(f.RESET)
    print("1 for one video :- ")
    print("2 for list of videos :- ")
    user_input = int(input("Write a number :- "))

    if user_input == 1:
        video_downloader = Downloader(str(input("enter a youtube url : ")))
        path = str(input("write where you want to install the video or leave a blank to install here : "))
        
        if path is None or path.__len__ == 0:
            video_downloader.download_vid(os.path.dirname(os.path.realpath(__file__)))

        else:
            video_downloader.download_vid(path)
        

    if user_input == 2:
        number_of_vids : int         = int(input("How many video do wish to install :- "))
        path           : str         = str(input("write where you want to install the video or leave a blank to install here : "))
        list_of_vids   : list[str]   = list()

        for i in range(number_of_vids):
            vid_url : str = str(input(f"enter the {i + 1} video url : "))
            list_of_vids.append(vid_url)

        video_downloader1 = Downloader("")
        
        if path is None or path.__len__ == 0:
            video_downloader1.download_vids(list_of_vids,os.path.dirname(os.path.realpath(__file__)))

        else:
            video_downloader1.download_vids(list_of_vids,path)
    


if __name__ == '__main__':
    main()