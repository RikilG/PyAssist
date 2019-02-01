import os,ctypes
from datetime import datetime
import requests
from bs4 import BeautifulSoup as BS

def apply_Wallpaper(fileName,platform):
    print('applying Wallpaper '+fileName)
    if platform == 'windows':
        SPI_SETDESKWALLPAPER = 20
        path = os.getcwd() + "\\Wallpapers\\" + fileName
        ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 0)
    elif platform == 'linux':
        # check gsettings path using $ which gsettings
        path = os.getcwd() + "/Wallpapers/" + fileName
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri "+path)

def get_Wallpaper(platform):
    result = input("Do you want to change your wallpaper? : ").lower()
    if not (result == 'y' or result == "yes"):
        return None
    try:
        if platform == 'windows':
            wallPath = os.getcwd() + "\\Wallpapers\\"
        elif platform == 'linux':
            wallPath = os.getcwd() + "/Wallpapers/"
        if not os.path.isdir(wallPath):
            os.mkdir(wallPath)
        imagesExt = os.listdir(wallPath)
        images = [ image[:image.index('.')] for image in imagesExt ]
        # print(images)
        fileName = str(datetime.now().date())+".jpg"
        if str(datetime.now().date()) not in images:
            site = requests.get("https://www.bing.com")
            soup = BS(site.text, "html.parser")
            #images = soup.find_all('img', {'style':'display:none'}) # website sturcture changed 
            images = soup.find_all('link')
            #onlinePath = images[1]['src'] # website structure changed
            onlinePath = images[0]['href']
            imageFinal = "https://www.bing.com"+str(onlinePath)
            response = requests.get(imageFinal, stream=True)
            if response.status_code == 200:
                import shutil
                ext = onlinePath[onlinePath.index('.'):]
                fileName = str(datetime.now().date())+ext
                if platform == 'windows':
                    completeName = os.path.join(os.getcwd() + "\\Wallpapers",fileName)
                elif platform == 'linux':
                    completeName = os.path.join(os.getcwd() + "/Wallpapers",fileName)
                with open(completeName,'wb') as file:# open in another diectory
                    shutil.copyfileobj(response.raw, file)
                del response
        else:
            print('you already have image with todays date ready in folder...')

        reply = input("Do you want to set downloaded wallpaper? : ").lower()
        if reply=='yes' or reply=='y':
            apply_Wallpaper(fileName,platform)
    except Exception as e:
        print("Error occored :\n"+str(e))

if __name__ == "__main__":
    get_Wallpaper()