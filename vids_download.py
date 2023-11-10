from pytube import YouTube
import time

class Downloader:

    def __init__(self , url : str) -> None:
        self.url = url

    
        
    def download_vid(self , path : str) -> bool:
    
        try:    
            yt = YouTube(self.url)
            print(f"Start to downlad the video {yt.title} in {path}:- " )
            start_time = time.time()
            yt.streams.get_highest_resolution().download()
            print(f"The video has downloaded in {path} , {time.time() - start_time}")
            return True
        
        except Exception as e:
            print(e)
            return False
        

    @staticmethod
    def download_vids(list_of_vids : list , path : str) -> None:
       
        number_of_vids : int = len(list_of_vids)
        downloaded_vids : int = 0

        start_time = time.time()
        for i in list_of_vids:
            
            yt = YouTube(i)

            try:
                print(f"Start to downlad the video {yt.title} in {path}:- " )
                yt.streams.get_highest_resolution().download()
                print(f"The video {yt.title} has downloaded in {path} successfully")
                downloaded_vids += 1

            except Exception as err:
                print(f"The video {yt.title} hasn\'t downloaded in {path} successfully")
                print(f"Error log : {err}")

        print(f"{downloaded_vids} out of {number_of_vids} had been downloaded in {path} in {time.time() - start_time} secs")
               

    