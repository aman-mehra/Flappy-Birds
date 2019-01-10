f=open("High Score.txt","r+")

def highscore(curscore):
    f.seek(0)
    s=int(f.read())
    if curscore>s:
        write(curscore)
        

def write(data):
    f.seek(0)
    f.truncate()
    f.write(str(data))

def read():
    f.seek(0)
    return int(f.read())
