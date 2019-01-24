import os,ctypes
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS

def apply_Wallpaper(fileName):
    SPI_SETDESKWALLPAPER = 20
    print('applying Wallpaper '+fileName)
    path = os.getcwd() + "\\Wallpapers\\" + fileName
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)

def get_Wallpaper():
    result = input("Do you want to change your wallpaper? : ").lower()
    if not (result == 'y' or result == "yes"):
        return None
    try:
        wallPath = os.getcwd() + "\\Wallpapers\\"
        if not os.path.isdir(wallPath):
            os.mkdir(wallPath)
        imagesExt = os.listdir(wallPath)
        images = [ image[:image.index('.')] for image in imagesExt ]
        # print(images)
        fileName = str(datetime.now().date())+".jpg"
        if str(datetime.now().date()) not in images:
            site = requests.get("https://www.bing.com")
            soup = BS(site.text, "html.parser")
            soup.find_all('img')
            images = soup.find_all('img', {'style':'display:none'})
            onlinePath = images[1]['src']
            imageFinal = "https://www.bing.com"+images[1]['src']
            response = requests.get(imageFinal, stream=True)
            if response.status_code == 200:
                import shutil
                ext = onlinePath[onlinePath.index('.'):]
                fileName = str(datetime.now().date())+ext
                completeName = os.path.join(os.getcwd() + "\\Wallpapers",fileName)
                with open(completeName,'wb') as file:# open in another diectory
                    shutil.copyfileobj(response.raw, file)
                del response
        else:
            print('you already have image with todays date ready in folder...')

        reply = input("Do you want to set downloaded wallpaper? : ").lower()
        if reply=='yes' or reply=='y':
            apply_Wallpaper(fileName)
    except Exception as e:
        print("Error occored :\n"+e)

if __name__ == "__main__":
    get_Wallpaper()