from numpy import random
import json
import time

def getRandData(inter1: int, inter2: int, mertekegyseg = "") -> str:
    return str(random.randint(inter1, inter2 +1)) + mertekegyseg

def printMoreToJSON(clss, rng: int, fileName: str) -> None:
    cnc = {"id": clss.machine_id,
           "temperature": clss.temperature,
           "vibration": clss.vibration,
           "rpm": clss.rpm}
    f = open(myFile, "w")
    f.write("[")
    f.close()
    
    try:
        with open(fileName, "a", encoding="utf-8") as myFile:
            for i in range(rng):
                json.dump(cnc, myFile, indent=4, ensure_ascii=False)
                clss.getNewData()

    except FileNotFoundError:
        with open(fileName, "w", encoding="utf-8") as myFile:
            for i in range(rng):
                json.dump(cnc, myFile, indent=2, ensure_ascii=False, separators=",")
                
    f = open(myFile, "a")
    f.write("]")
    f.close()


class CNC:
    def __init__(self, machine_id, temperature, vibration, rpm):
        self.machine_id = machine_id
        self.temperature = temperature
        self.vibration = vibration
        self.rpm = rpm


    def getNewData(self):
        self.temperature = getRandData(60, 100+1, "°C")
        self.vibration = getRandData(0, 10+1, "mm/s")
        self.rpm = getRandData(1500, 4000)

    def __str__(self):
        return f"{self.machine_id}: {self.temperature} {self.vibration} {self.rpm}"
#        return "{" + f" \"id\" : \"{self.machine_id}\", \"temperature\" : \"{self.temperature}\", \"vibration\" : \"{self.vibration}\", \"rpm\" : \"{self.rpm}\"" + "};"


def main():
    
    cnc1 = CNC("CNC_01", 
               getRandData(60, 100+1, "°C"), 
               getRandData(0, 10+1, "mm/s"),
               getRandData(1500, 4000))

    cnc2 = CNC("CNC_02", 
               getRandData(60, 100+1, "°C"), 
               getRandData(0, 10+1, "mm/s"),
               getRandData(1500, 4000))

    cnc3 = CNC("CNC_03", 
               getRandData(60, 100+1, "°C"), 
               getRandData(0, 10+1, "mm/s"),
               getRandData(1500, 4000))

    cnc4 = CNC("CNC_04", 
               getRandData(60, 100+1, "°C"), 
               getRandData(0, 10+1, "mm/s"),
               getRandData(1500, 4000))

    cnc5 = CNC("CNC_05", 
               getRandData(60, 100+1, "°C"), 
               getRandData(0, 10+1, "mm/s"),
               getRandData(1500, 4000))
    
    print(cnc1)
    cnc1.getNewData()
    print(cnc1)
    
    printMoreToJSON(cnc1, 10, "test.json")
    



if __name__ == '__main__':
    main()