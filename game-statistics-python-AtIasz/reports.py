
# Report functions
path="game_stat.txt"

def count_games(file_name):
    statfile=open(file_name,"r")
    cnt=0
    with open(file_name)as l:
        line=l.readline()
        while line:
            line=l.readline()
            cnt+=1
    return cnt
def decide(file_name, year):
    statfile=open(file_name,"r")
    isthere=False
    with open(file_name)as l:
        line=l.readline()
        while line:
            if str(year) in line:
                isthere=True
                return isthere
            line=l.readline()
    return isthere
def get_latest(file_name):
    statfile=open(file_name,"r")
    latest=0
    lN=""
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            r=lisalisa[-1]
            w=""
            if "\n" in r:     
                for i in range(len(r)-1):
                    w+=r[i]       
            lisalisa[-1]=w
            if len(lisalisa[0])!=0:
                o=int(lisalisa[2])
                if o>latest:
                    latest=o
                    lN=lisalisa[0]
    return lN
def count_by_genre(file_name, genre):
    statfile=open(file_name,"r")
    cnt=0
    
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            r=lisalisa[-1]
            w=""
            if "\n" in r:     
                for i in range(len(r)-1):
                    w+=r[i]       
            lisalisa[-1]=w
            if len(lisalisa[0])!=0:
                if lisalisa[3]==genre:
                    cnt+=1
    return cnt
def get_line_number_by_title(file_name, title):
    statfile=open(file_name,"r")
    cnt=0
    
    with open(file_name)as l:
        r=l.readline()
        cnt+=1
        lisalisa=r.split("\t")
        while r:
            if title==lisalisa[0]:
                return cnt
            r=l.readline()
            cnt+=1
            lisalisa=r.split("\t")
            r=lisalisa[-1]
            w=""
            if "\n" in r:     
                for i in range(len(r)-1):
                    w+=r[i]       
            lisalisa[-1]=w
        raise ValueError
def sort_abc(file_name):
    statfile=open(file_name,"r")
    listli=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listli.append(lisalisa[0])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            listli.append(lisalisa[0])
    listli.remove(listli[-1])
    sorye = False
    while sorye == False:
        sorye = True
        for obj in range(len(listli) - 1):
            if listli[obj] > listli[obj + 1]:
                temp = listli[obj]
                listli[obj] = listli[obj + 1]
                listli[obj + 1] = temp
                sorye = False
    return listli 
def get_genres(file_name):    
    statfile=open(file_name,"r")
    listli=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listli.append(lisalisa[3])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            
            if len(lisalisa[0])!=0:
                listli.append(lisalisa[3])
    reli=[]
    for i in range(len(listli)):
        if listli[i] not in reli:
            reli.append(listli[i])
    print(reli)
    
    sorye = False
    while sorye == False:
        sorye = True
        for obj in range(len(reli) - 1):
            if reli[obj] > reli[obj + 1]:
                temp = reli[obj]
                reli[obj] = reli[obj + 1]
                reli[obj + 1] = temp
                sorye = False
    return reli
def when_was_top_sold_fps(file_name):
    statfile=open(file_name,"r")
    cnt=2020
    num=0
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            if len(lisalisa[0])!=0:
                if lisalisa[3]=="First-person shooter":
                    if float(num)<float(lisalisa[1]):
                        num=float(lisalisa[1])
                        cnt=int(lisalisa[2])
                r=l.readline()
                lisalisa=r.split("\t")
        if cnt!=2020:
            return cnt
        else:
            raise ValueError




text=open("export.py","a")
text.write("'''"+"\n"+str(count_games(path))+"\n"+str(decide(path, 1996))+"\n"+str(get_latest(path))+"\n"+str(count_by_genre(path, "RPG"))+"\n"+str(get_line_number_by_title(path, "Minecraft"))+"\n"+str(sort_abc(path))+"\n"+str(get_genres(path))+"\n"+str(when_was_top_sold_fps(path))+"\n"+"'''")
text.close()
