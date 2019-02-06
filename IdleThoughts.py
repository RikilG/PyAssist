import os
from datetime import datetime
from datetime import timezone
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError


def selectOption():
    syncDB()
    print("What do you want to do?")
    print("1:add idea(default)")
    print("2:delete idea")
    print("0:quit")
    option = int(input("Enter your option here : "))
    if(option == 1):
        addIdea()
    elif(option == 0):
        return
    else:
        deleteIdea()

def addIdea():
    idea = input("Enter idea here : ")
    with open("IdleThoughts/thoughts.txt",'a') as file:
        file.write(idea+'\n')
    syncDB()

def deleteIdea():
    print("delete idea under development")

def syncDB():
    server_modified = dbx.files_list_folder("").entries[0].server_modified
    try:
        mtime = os.path.getmtime("IdleThoughts/thoughts.txt")
    except OSError:
        mtime = 0
    local_modified = datetime.fromtimestamp(mtime)
    server_modified = server_modified.replace(tzinfo=timezone.utc).astimezone(tz=None).replace(tzinfo=None)
    #print("server modified " + str(server_modified))
    #print("local modified " + str(local_modified))
    if(server_modified > local_modified):
        print("download latest from server")
        download()
    else:
        print("uploading latest to server")
        upload()

def upload():
    with open("IdleThoughts/thoughts.txt",'rb') as f:
        print("uploading thoughts.txt to dropbox...")
        try:
            dbx.files_upload(f.read(),'/thoughts-db.txt',mode=WriteMode('overwrite'))
        except ApiError as err:
            if ( err.error.is_path() and err.error.get_path().reason.is_insufficient_space()):
                print("Insufficient online space")
            elif err.user_message_text:
                print(err.user_message_text)
            else:
                print(str(err))

def download():
    print("downloading thoughts.txt from dropbox...")
    try:
        # md is metadata of file
        md, res = dbx.files_download('/thoughts-db.txt')
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        return None
    data = res.content
    print('downloaded ',len(data), 'bytes; md:', md)
    with open("IdleThoughts/thoughts.txt",'wb') as f:
        if(data != f.read()):
            f.write(data)

if __name__ == '__main__':
    # Please input yout oauth 2 token here or from file
    TOKEN = None
    with open("IdleThoughts/OAUTH-2-token",'r') as tokenfile:
        TOKEN = tokenfile.readline().strip()
    dbx = dropbox.Dropbox(TOKEN)
    selectOption()
