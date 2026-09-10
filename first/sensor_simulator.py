#Projekt start: 2026.09.10.
#Ezen dolgozott órák: 5

from numpy import random
import json
import time

############################################################################### Class
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

############################################################################### Method
def getRandData(inter1: int, inter2: int, mertekegyseg = "") -> str:
    return str(random.randint(inter1, inter2 +1)) + mertekegyseg


def printMoreToJSON(lst: list, rng: int, fileName: str) -> None:
    timeStamp = time.localtime()
    for cnc in lst:
        cncJSON = {"id": cnc.machine_id,
               "timestamp" : f"{timeStamp.tm_year}-{timeStamp.tm_mon}-{timeStamp.tm_mday}-{timeStamp.tm_hour}:{timeStamp.tm_min}:{timeStamp.tm_sec}",
                "temperature": cnc.temperature,
                "vibration": cnc.vibration,
                "rpm": cnc.rpm}
        try:
            with open(fileName, "a", encoding="utf-8") as myFile:
                jsonData = json.dumps(cncJSON, indent=2, ensure_ascii=False)
                myFile.write(jsonData + ",\n")
        except FileNotFoundError:
            print("#\n#\n#\n#\n#\nNem találom a filet\n#\n#\n#\n#\n#")
    
                
############################################################################### Main
def main():
    JSONFile = "test.json"
    with open(JSONFile, "w") as f:
        f.write("[\n")

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
    
    machines_lst = [cnc1, cnc2, cnc3, cnc4, cnc5]

    for i in range(5):
        printMoreToJSON(machines_lst, 10, JSONFile)
        time.sleep(2.5)
        for machine in machines_lst:
            machine.getNewData()
    
    with open(JSONFile, "r") as f:
        Lines = f.readlines()
    Lines[-1] = Lines[-1][:-2]
    with open(JSONFile, "w") as f:
        f.writelines(Lines)
        f.write("\n]")
        f.close()


if __name__ == '__main__':
    main()