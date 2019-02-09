import os
from datetime import datetime
from datetime import timezone
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

with open("IdleThoughts/OAUTH-2-token",'r') as tokenfile:
    TOKEN = tokenfile.readline().strip()
dbx = dropbox.Dropbox(TOKEN)

def run_query(query):
    if 'add' in query:
        addIdea()
    elif 'remove' in query or 'delete' in query or 'del' in query:
        deleteIdea()
    elif 'show' in query or 'view' in query:
        showIdeas()
    else:
        selectOption()

def selectOption():
    syncDB()
    print("What do you want to do?")
    print("1:add idea")
    print("2:show ideas(default)")
    print("3:delete idea")
    print("0:quit")
    option = int(input("Enter your option here : "))
    if(option == 1):
        addIdea()
    elif(option == 3):
        deleteIdea()
    elif(option == 0):
        return
    else:
        showIdeas()

def addIdea():
    idea = input("Enter idea here : ")
    with open("IdleThoughts/thoughts.txt",'a') as file:
        file.write(idea+'\n')
    syncDB()

def deleteIdea():
    print("Select idea no to be deleted")
    showIdeas()
    with open("IdleThoughts/thoughts.txt",'r') as file:
        ideas = file.readlines()
    x = int(input("Select idea no to be deleted : ")) - 1
    if x>=len(ideas):
        print("improper line index given")
        return
    del ideas[x]
    with open("IdleThoughts/thoughts.txt",'w') as file:
        for idea in ideas:
            file.write(idea)
    syncDB()

def syncDB():
    try:
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
            print("Performing DropBox Sync")
            upload()
    except dropbox.exceptions.HttpError as err:
        print(err)
    except ApiError as err:
        print(err)
    except OSError:
        print("OSErr : User offline. Changes are made locally")

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
    flag=0
    print("downloading thoughts.txt from dropbox...")
    try:
        # md is metadata of file
        md, res = dbx.files_download('/thoughts-db.txt')
    except dropbox.exceptions.HttpError as err:
        print('*** HTTP error', err)
        return None
    data = res.content
    print('downloaded ',len(data), 'bytes;')
    with open("IdleThoughts/thoughts.txt",'rb') as f:
        if(data != f.read()):
            flag = 1
    if(flag == 1):
        with open("IdleThoughts/thoughts.txt",'wb') as f:
                f.write(data)

def showIdeas():
    lineno = 1
    with open("IdleThoughts/thoughts.txt",'r') as file:
        ideas = file.readlines()
    print("\nStored Thoughts : ")
    for idea in ideas:
        print(' ' + str(lineno) + ' : ' + idea,end='')
        lineno += 1
    print()

if __name__ == '__main__':
    # Please input yout oauth 2 token here or from file
    selectOption()
