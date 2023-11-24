import math
import datetime

from tabulate import tabulate

def main():
    result = []
    player = Player()
    
    order = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris,
        Player.Solar,
        Player.Met, #10
        Player.Kris,
        Player.Kris,
        Player.Solar,
        Player.Deut,
        Player.Kris, #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris, #20
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Solar,
        Player.Deut,
    ]
    i = 1
    for element in order:
        print("Step", i)
        data = player.build(element)
        
        
        for row in data:
            row.insert(0,i)
            result.append(row)
        i+=1

    print(tabulate(result, headers=["Step","Building", "Level", "Met", "Kris", "Deut", "Power", "MetMine", "KrisMine", "DeutMine", "Solar", "Prod Met", "Prod Kris", "Prod Deut", "Step Time", "Overall Time", "time starting from 18:00",]))

class Player:
    Met = "Metall"
    Kris = "Kristall"
    Deut = "Deut"
    Solar = "Solar"
    
    def __init__(self):
        self.prodMulti = 2
        
        #resources
        self.met = 500
        self.kris = 500
        self.deut = 0
        self.power = 0
        
        #buildings
        self.metMine = 0
        self.krisMine = 0
        self.deutMine = 0
        self.solar = 0
        self.robo = 0
        self.nani = 0
        
        #time
        self.timeTaken = 0
        
        #Heelper Values
        self.generatedPower = 0
        self.consumedPower = 0
        self.result = []
        
        
    def updatePower(self):
        #generated power
        self.generatedPower = round(20 * self.solar * math.pow(1.1, self.solar))
        self.power = self.generatedPower
        #consumed power
        self.consumedPower = round(10 * self.metMine * math.pow(1.1, self.metMine))
        self.consumedPower += round(10 * self.krisMine * math.pow(1.1, self.krisMine))
        self.consumedPower += round(20 * self.deutMine * math.pow(1.1, self.deutMine))
        
        self.power = self.generatedPower - self.consumedPower
        print("upded Power to ", self.power)
    
    def build(self, building):
        self.result = []
        print("----------")
        print("Building " + building)
        
        #check if possible
        if not self.canBuild(building):
            print("Waiting for Resources")
            waitTime = self.wait(building)
            self.generateResources(waitTime)
            self.timeTaken += waitTime
            displayTimeAll = str(datetime.timedelta(hours=self.timeTaken)).split(".")[0]
            displayTimeCurrent = str(datetime.timedelta(hours=waitTime)).split(".")[0]
            displayFrom18 = str(datetime.datetime.combine(datetime.date(2023,12,1), datetime.time(18,0,0)) + datetime.timedelta(hours=self.timeTaken)).split(".")[0]
            self.result.append(["Wait","-", self.met, self.kris, self.deut, self.power,self.metMine, self.krisMine,self.deutMine, self.solar,self.getProduction(Player.Met), self.getProduction(Player.Kris), self.getProduction(Player.Deut), displayTimeCurrent, displayTimeAll,displayFrom18])
        
        #get BuildTime
        time = self.getBuildTime(building)
        self.timeTaken += time
        #Add resources produced while building
        self.generateResources(time)
        #remove resources from building
        met,kris = self.getBuildingCost(building)
        self.met -= met
        self.kris -= kris
        
        resultBuldingLevel = 0
        match building:
            case Player.Met:
                self.metMine +=1
                resultBuldingLevel = self.metMine
            case Player.Kris:
                self.krisMine +=1
                resultBuldingLevel = self.krisMine
            case Player.Deut:
                self.deutMine +=1
                resultBuldingLevel = self.deutMine
            case Player.Solar:
                self.solar +=1
                resultBuldingLevel = self.solar
            case _:
                print("ERROR")
        self.updatePower()
        
        displayTimeAll = str(datetime.timedelta(hours=self.timeTaken)).split(".")[0]
        displayTimeCurrent = str(datetime.timedelta(hours=time)).split(".")[0]
        displayFrom18 = str(datetime.datetime.combine(datetime.date(2023,12,1), datetime.time(18,0,0)) + datetime.timedelta(hours=self.timeTaken)).split(".")[0]
        self.result.append([building,resultBuldingLevel, self.met, self.kris, self.deut, self.power,self.metMine, self.krisMine,self.deutMine, self.solar, self.getProduction(Player.Met), self.getProduction(Player.Kris), self.getProduction(Player.Deut), displayTimeCurrent, displayTimeAll, displayFrom18])
        return self.result
    
    def canBuild(self, building):
        met,kris = self.getBuildingCost(building)
        return self.met >= met and self.kris >= kris

    def getBuildTime(self, building):
        met,kris = self.getBuildingCost(building)
        time = ((met + kris) / (2500 * (1 + self.robo))) * math.pow(0.5,self.nani)
        print("Time: " + str(time) )
        return time
    
    def getProduction(self, building):
        prod = 0
        match building:
            case Player.Met:
                prod = (self.prodMulti *30 * self.metMine * math.pow(1.1,self.metMine)) + 40
            case Player.Kris:
                prod = (self.prodMulti *20 * self.krisMine * math.pow(1.1,self.krisMine)) + 20
            case Player.Deut:
                prod = self.prodMulti * 10*self.deutMine*math.pow(1.1,self.deutMine)*(1.44-0.004*50)
        
        percentalProd = 1
        if self.power < 0:
            percentalProd = self.generatedPower / self.consumedPower

        return prod * percentalProd
        
    def generateResources(self, time):
        metProduced = self.getProduction(self.Met) * time
        self.met += metProduced
        
        kirsProduced = self.getProduction(self.Kris) * time
        self.kris += kirsProduced
        
        deutProduced = self.getProduction(self.Deut) * time
        self.deut += deutProduced
        
    def getBuildingCost(self, building):
        match building:
            case Player.Met:
                return ( 40*math.pow(1.5,self.metMine+1),
                         10*math.pow(1.5,self.metMine+1))
            case Player.Kris:
                return ( 30*math.pow(1.6,self.krisMine+1),
                         15*math.pow(1.6,self.krisMine+1))
            case Player.Deut:
                return ( 150*math.pow(1.5,self.deutMine+1),
                         50*math.pow(1.5,self.deutMine+1))
            case Player.Solar:
                return ( 50*math.pow(1.5,self.solar+1),
                         20*math.pow(1.5,self.solar+1))
            case _:
                print("ERROR")
                
    def wait(self, building):
        met,kris = self.getBuildingCost(building)
        
        requiredMet =  met - self.met
        requiredKris = kris - self.kris
        
        waitTimeMet = 0
        waitTimeKris = 0
        #if value > 0 it's required
        if (requiredMet > 0):
            waitTimeMet = (1 / self.getProduction(Player.Met)) * requiredMet
            print("Waiting for Met ", waitTimeMet)
        if (requiredKris > 0):
            waitTimeKris = (1 / self.getProduction(Player.Kris)) * requiredKris
            print("Waiting for Kris ", waitTimeKris)
        
        maxWaitTime = max(waitTimeMet,waitTimeKris)
        return maxWaitTime

if __name__ == "__main__":
    main()