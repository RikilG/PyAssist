import os

def showBanner():
    if os.path.isfile('Banner-text'):
        os.system('cat Banner-text')

if __name__ == "__main__":
    showBanner()