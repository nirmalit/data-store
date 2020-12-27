import json
import threading
class dataStore:
    def __init__(self,path=None):
        self.path=""
        if path==None:
            self.path="store.json"
        else:
            self.path=path+"\store.json"
        file=open(self.path,"w")
        file.write("{}")
        file.close()
    def create(self,key,value,time=0):
        file=open(self.path,"r")
        loader=file.readline()
        file.close()
        temp=json.loads(loader)
        for x in temp.keys():
            if x==key:
                return("Key is already availabe in Data Store")
        temp[key] = value
        json_string=json.dumps(temp)
        file=open(self.path,"w")
        file.write(json_string)
        file.close()
        if time !=0:
            self.timeToKill(key,time)
        return ("Success ,key-value pair are added to the Data Store")
    def read(self,key):
        file=open(self.path,"r")
        loader = file.readline()
        temp = json.loads(loader)
        file.close()
        if key in temp.keys():
            return temp[key]
        return("Key is not in the Data Store")
    def delete(self,key):
        file = open(self.path, "r")
        loader = file.readline()
        temp = json.loads(loader)
        file.close()
        if key in temp.keys():
            temp.pop(key)
            file=open(self.path, "w")
            tempLoad=json.dumps(temp)
            file.write(tempLoad)
            file.close()
            return("Key&pair is removed Successfully")
        return("Key is not in the Data Store")
    def deleteAfterExpire(self,key):
        file = open(self.path, "r")
        loader = file.readline()
        temp = json.loads(loader)
        file.close()
        if key not in temp.keys():
            print("Aready key-pair is removed or check the key name")
            return
        temp.pop(key)
        file=open(self.path, "w")
        tempLoad=json.dumps(temp)
        file.write(tempLoad)
        file.close()
        print(key," is removed after the specfied second")
    def timeToKill(self,key,times):
        global timer
        timer = threading.Timer(times,self.deleteAfterExpire,args=(key,))
        timer.start()



