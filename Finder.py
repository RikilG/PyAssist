import os,subprocess

"""
This module requires Everything search and es.exe commandline utility installed and present in system path.
# use subprocess.call().
"""

def find(queryStr, platform):
    if platform == 'linux':
        proc = subprocess.Popen(['mlocate',queryStr])
    elif platform == 'windows':
        subprocess.call('Everything.exe -search ' + '"'+queryStr+'"')

def open(queryStr, platform):
    # use command line es.exe and pipe(using '>' operator in command) output to a list. then open accordingly.
    if platform == 'linux':
        proc = subprocess.Popen(['mlocate',queryStr],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    elif platform == 'windows':
        proc = subprocess.Popen(['es.exe','-r',queryStr],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out = list(proc.stdout)
    out = [str(o.decode("utf-8")) for o in out]
    out = [o.rstrip('\r\n') for o in out]
    out = [o.replace('\\','\\\\') for o in out]
    out = ['\"'+o+'\"' for o in out]
    if len(out) == 1:
        print("Found : " + out[0])
        option = input("Do you want to open?(y/n) : ").lower()
        if option == 'y' or option == 'yes':
            #os.system('\"'+out[0]+'\" ')
            subprocess.Popen(['start','\"'+out[0]+'\" '])
        else:
            return None
    else :
        print("Choose an option or enter 0 to return : ")
        for i in range(1,len(out)+1):
            print(str(i) + ')  ' + out[i-1])
        try:
            option = int(input("Select an option : "))
        except:
            print("Invalid choice.")
            return None
        if(option<=len(out)):
            if(option==0):
                return None
            #os.system('\"'+out[option-1]+'\" ')
            subprocess.Popen(['start','\"'+out[option-1]+'\" '])
        else:
            print("Invalid option.")


def run(queryStr,platform):
    try:
        if platform!='linux':
            subprocess.call('start '+queryStr)
        else:
            print("linux opening applications is not yet supported!.")
    except Exception:
        print('You did not specify what to open!!')

if __name__ == '__main__':
    pass