import math
import datetime

from tabulate import tabulate
import random

import itertools

def main():
    result = []
    player = Player()
    
    #order = 1 day, 4:29:13
    orig = [
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
        Player.Met, #18
        (Player.SetProd, Player.Met, 0.9), #33
        Player.Solar,
        (Player.SetProd, Player.Met, 1), #33
        Player.Kris, #20
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Robo,
        Player.Robo,
        Player.Lab,
        Player.Ship, #30
        Player.Kris,
        Player.Ship,
        Player.Solar,
        Player.Deut,
        Player.Met,
        Player.Etech,
        Player.Combust,
        Player.Combust,
        Player.KT
    ]
    #1 day, 1 day, 4:28:11
    improv_1 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,  #8#test
        Player.Solar,#9
        Player.Kris, #10 #test
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
        Player.Robo,
        Player.Robo,
        Player.Lab,
        Player.Ship,    #30
        Player.Kris,    #31
        Player.Ship,    #32
        Player.Solar,   #33
        Player.Deut,    #34
        Player.Met,     #35
        Player.Etech,   #36
        Player.Combust, #37
        Player.Combust, #38
        Player.KT       #39
    ]
    
    #1 day, 2:43:45
    improv_2 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,  #8
        Player.Solar,#9
        Player.Kris, #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        # Player.Deut, #später
        Player.Kris, # anstatt deut
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
        Player.Robo,
        Player.Robo,
        Player.Lab,
        Player.Ship,    #30
        Player.Kris,    #31
        Player.Ship,    #32
        Player.Solar,   #33
        Player.Deut,    #34
        Player.Met,     #35
        Player.Etech,   #36
        Player.Combust, #37
        Player.Combust, #38
        Player.KT       #39
    ]
    
    #1 day, 1:23:48
    improv_3 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,  #8
        Player.Solar,#9
        Player.Kris, #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris, #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris, #20
        Player.Met,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Robo,
        Player.Robo,
        Player.Lab,
        Player.Ship,    #30
        Player.Kris,    #31
        Player.Ship,    #32
        Player.Solar,   #33
        Player.Deut,    #34
        Player.Met,     #35
        Player.Etech,   #36
        Player.Combust, #37
        Player.Combust, #38
        Player.KT       #39
    ]
    
    #1 day, 1:26:30
    improv_4 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,  #8
        Player.Solar,#9
        Player.Kris, #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris, #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris, #20
        Player.Met,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Robo,
        Player.Robo,
        Player.Lab,
        Player.Ship,    #30
        Player.Kris,    #31
        Player.Ship,    #32
        Player.Solar,   #33
        Player.Deut,    #34
        Player.Met,     #35
        Player.Etech,   #36
        Player.Combust, #37
        Player.Combust, #38
        Player.KT       #39
    ]
    
    #1 day, 1:23:44
    improv_5 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,   #8
        Player.Solar, #9
        Player.Kris,  #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris,  #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris,  #20
        Player.Met,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Solar, #25
        Player.Deut,
        Player.Deut,
        Player.Kris,    
        Player.Lab,     #29
        Player.Solar,   #30
        Player.Deut,    #31
        Player.Met,     #32
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        Player.KT       #40
    ]
    
    
    #1 day, 0:07:42
    #but may be long term inpact
    improv_6 = [
        Player.Solar,   #1
        Player.Met,     #2
        Player.Met,     #3
        Player.Solar,   #4
        Player.Met,     #5
        Player.Met,     #6
        Player.Solar,   #7
        Player.Met,     #8
        Player.Solar,   #9
        Player.Kris,    #10
        Player.Kris,    #11
        Player.Kris,    #12
        Player.Solar,   #13
        Player.Kris,    #14
        Player.Kris,    #15
        Player.Solar,   #16
        Player.Met,     #17
        Player.Met,     #18
        Player.Solar,   #19
        Player.Kris,    #20
        Player.Met,     #21
        Player.Solar,   #22
        Player.Deut,    #23
        Player.Deut,    #24
        Player.Solar,   #25
        Player.Deut,    #26
        Player.Deut,    #27
        Player.Kris,    #28
        Player.Lab,     #29
        Player.Deut,    #30
        Player.Deut,    #31
        (Player.SetProd, Player.Kris, 0.7), #32
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        (Player.SetProd, Player.Kris, 1), #40
        (Player.SetProd, Player.Deut, 0.5), #41
        Player.KT,      #42
    ]

    
    # 23:59:03
    improv_7 = [
        Player.Solar,   #1
        Player.Met,     #2
        Player.Met,     #3
        Player.Solar,   #4
        Player.Met,     #5
        Player.Met,     #6
        Player.Solar,   #7
        Player.Met,     #8
        Player.Solar,   #9
        Player.Kris,    #10
        Player.Kris,    #11
        Player.Kris,    #12
        Player.Solar,   #13
        Player.Kris,    #14
        Player.Kris,    #15
        Player.Solar,   #16
        Player.Met,     #17
        Player.Met,     #18
        Player.Solar,   #19
        Player.Kris,    #20
        Player.Met,     #21
        Player.Solar,   #22
        Player.Deut,    #23
        Player.Deut,    #24
        Player.Solar,   #25
        Player.Deut,    #26
        Player.Deut,    #27
        Player.Kris,    #28
        Player.Lab,     #29
        Player.Deut,    #30
        Player.Deut,    #31
        (Player.SetProd, Player.Kris, 0.7), #32
        (Player.SetProd, Player.Met, 0.8), #33
        Player.Robo,    #34
        Player.Robo,    #35
        Player.Ship,    #36
        Player.Ship,    #37
        Player.Etech,   #38
        (Player.SetProd, Player.Met, 0.9), #39
        Player.Combust, #40
        Player.Combust, #41
        (Player.SetProd, Player.Kris, 1), #42
        (Player.SetProd, Player.Deut, 0.5), #43
        Player.KT,      #44
    ]
    
    #from 5
    # 23:06:45
    improv_5_1 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,   #8
        Player.Solar, #9
        Player.Kris,  #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris,  #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris,  #20
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        Player.Solar, #25
        Player.Deut,
        Player.Deut,
        Player.Lab,     #29
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        Player.KT       #40
    ]
    
    # 22:33:32
    improv_5_2 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,   #8
        Player.Solar, #9
        Player.Kris,  #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris,  #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris,  #20
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        # Player.Solar, #25
        Player.Deut,
        Player.Deut,
        Player.Met, 
        (Player.SetProd, Player.Kris, 0.6), 
        (Player.SetProd, Player.Met, 0.6),
        Player.Lab,     #29
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        Player.KT       #40
    ]
    
    #22:15:58
    improv_5_3 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,   #8
        Player.Solar, #9
        Player.Kris,  #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris,  #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris,  #20
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        # Player.Solar, #25
        Player.Deut,
        Player.Deut,
        Player.Met, 
        (Player.SetProd, Player.Kris, 0.7), 
        (Player.SetProd, Player.Met, 0.6),
        Player.Lab,     #29
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        Player.KT       #40
    ]
    
    #21:59:16
    improv_5_4 = [
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Met,   #8
        Player.Solar, #9
        Player.Kris,  #10
        Player.Kris,  #11
        Player.Kris,
        Player.Solar,
        Player.Kris,
        Player.Kris,  #15
        Player.Solar,
        Player.Met,
        Player.Met,
        Player.Solar,
        Player.Kris,  #20
        Player.Deut,
        Player.Solar,
        Player.Deut,
        Player.Deut,
        (Player.SetProd, Player.Kris, 0.8), 
        Player.Deut, #25
        Player.Deut,
        (Player.SetProd, Player.Kris, 0.7), 
        (Player.SetProd, Player.Met, 0.6),
        Player.Lab,     #29
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        Player.KT       #40
    ]
    
    #21:46:55 
    improv_5_5 =[
        Player.Solar,   #1
        Player.Met,     #2
        Player.Met,     #3
        Player.Solar,   #4
        Player.Met,     #5
        Player.Met,     #6
        Player.Solar,   #7
        Player.Met,     #8
        Player.Solar,   #9
        Player.Kris,    #10
        Player.Kris,    #11
        Player.Kris,    #12
        Player.Solar,   #13
        Player.Kris,    #14
        Player.Kris,    #15
        Player.Solar,   #16
        Player.Met,     #17
        Player.Met,     #18
        Player.Solar,   #19
        Player.Kris,    #20
        Player.Deut,    #21
        Player.Deut,    #23
        Player.Solar,   #22
        Player.Deut,    #24
        Player.Deut,    #25
        (Player.SetProd, Player.Kris, 0.8), #26
        Player.Deut,
        (Player.SetProd, Player.Kris, 0.8), 
        (Player.SetProd, Player.Met, 0.7),
        Player.Lab,     #29
        Player.Robo,    #33
        Player.Robo,    #34
        Player.Ship,    #35
        Player.Ship,    #36
        Player.Etech,   #37
        Player.Combust, #38
        Player.Combust, #39
        Player.KT       #40
    ]
    
    improv_5_6 = [
        Player.Solar,   #1
        Player.Met,     #2
        Player.Met,     #3
        Player.Solar,   #4
        Player.Met,     #5
        Player.Met,     #6
        Player.Solar,   #7
        Player.Met,     #8
        Player.Solar,   #9
        Player.Kris,    #10
        Player.Kris,    #11
        Player.Kris,    #12
        Player.Solar,   #13
        Player.Kris,    #14
        Player.Kris,    #15
        Player.Solar,   #16
        Player.Met,     #17
        Player.Met,     #18
        Player.Solar,   #19
        Player.Kris,    #20
        Player.Deut,    #21
        Player.Deut,    #22
        Player.Solar,   #23
        Player.Deut,    #24
        Player.Deut,    #25
        (Player.SetProd, Player.Kris, 0.8), #26
        Player.Deut,    #27
        (Player.SetProd, Player.Kris, 0.8), #28 
        (Player.SetProd, Player.Met, 0.7), #29
        Player.Lab,     #30
        Player.Robo,    #31
        Player.Robo,    #32
        Player.Ship,    #33
        Player.Ship,    #34
        Player.Etech,   #35
        Player.Combust, #36
        Player.Combust, #37
        Player.KT,      #38
        (Player.SetProd, Player.Met, 1), #TMP
        (Player.SetProd, Player.Kris, 1), #TMP
        (Player.SetProd, Player.Deut, 1) #TMP
    ]
    
    #alternative
    improv_5_7 = [
        Player.Solar,   #1
        Player.Met,     #2
        Player.Met,     #3
        Player.Solar,   #4
        Player.Met,     #5
        Player.Met,     #6
        Player.Solar,   #7
        Player.Met,     #8
        Player.Solar,   #9
        Player.Kris,    #10
        Player.Kris,    #11
        Player.Kris,    #12
        Player.Solar,   #13
        Player.Kris,    #14
        Player.Kris,    #15
        Player.Solar,   #16
        Player.Met,     #17
        Player.Met,     #18
        Player.Solar,   #19
        Player.Kris,    #20
        Player.Deut,    #21
        Player.Deut,    #22
        Player.Solar,   #23
        Player.Deut,    #24
        Player.Deut,    #25
        (Player.SetProd, Player.Kris, 0.8), #26
        Player.Deut,    #27
        (Player.SetProd, Player.Kris, 0.8), #28 
        (Player.SetProd, Player.Met, 0.7), #29
        Player.Solar,   #19
        (Player.SetProd, Player.Kris, 1), #28 
        (Player.SetProd, Player.Met, 1), #29
        Player.Lab,     #30
        Player.Robo,    #31
        Player.Robo,    #32
        Player.Ship,    #33
        Player.Ship,    #34
        Player.Etech,   #35
        Player.Combust, #36
        Player.Combust, #37
        Player.KT,      #38
        (Player.SetProd, Player.Met, 1), #TMP
        (Player.SetProd, Player.Kris, 1), #TMP
        (Player.SetProd, Player.Deut, 1) #TMP
    ]
    
    
    i = 1
    

    for element in orig:
        data = []
        if (len(element) == 3):
            data = player.build(element[0], element[1], element[2])
        else:
            data = player.build(element)
        
        
        for row in data:
            row.insert(0,i)
            result.append(row)
        i+=1
        
    print(tabulate(result, headers=["Step","Building", "Level", "Met", "Kris", "Deut", "Power", "MetMine", "KrisMine", "DeutMine", "Solar", "Prod Met", "Prod Kris", "Prod Deut", "Step Time", "Overall Time", "time starting from 18:00"]))
    
class Player:
    Met = "Metall"
    Kris = "Kristall"
    Deut = "Deut"
    Solar = "Solar"
    Robo = "Robo"
    Ship = "Ship"
    Lab = "research lab"
    KT = "small cargo"
    Combust = "Combustion Drive"
    Etech = "Etechnik"
    SetProd = "set Production"
    
    def __init__(self):
        self.ressourceSpeed = 2
        self.buildSpeed = 1
        self.researchSpeed = 2.5
        
        #resources
        self.met = 500
        self.kris = 500
        self.deut = 0
        self.power = 0
        
        #ships
        self.kt = 0
        
        #prodSettings
        self.metProd = 1
        self.krisProd = 1
        self.deutProd = 1
        
        #buildings
        self.metMine = 0
        self.krisMine = 0
        self.deutMine = 0
        self.solar = 0
        self.robo = 0
        self.nani = 0
        self.ship = 0
        self.lab = 0
        
        #research
        self.combust = 0
        self.etech = 0
        
        #time
        self.timeTaken = 0
        
        #Heelper Values
        self.generatedPower = 0
        self.consumedPower = 0
        self.result = []
    
    def setPoruction(self, building, percent):
        match building:
            case Player.Met:
                self.metProd = percent
            case Player.Kris:
                self.krisProd = percent
            case Player.Deut:
                self.deutProd = percent
            case _:
                print("ERROR")
        self.updatePower()
        
    def updatePower(self):
        #generated power
        self.generatedPower = round(20 * self.solar * math.pow(1.1, self.solar))
        self.power = self.generatedPower
        #consumed power
        self.consumedPower = round(10 * self.metMine * math.pow(1.1, self.metMine) * self.metProd)
        self.consumedPower += round(10 * self.krisMine * math.pow(1.1, self.krisMine) * self.krisProd)
        self.consumedPower += round(20 * self.deutMine * math.pow(1.1, self.deutMine) * self.deutProd)
        
        self.power = self.generatedPower - self.consumedPower
    
    
    def build(self, building, target=None, production=None):
        self.result = []
        #special case Production
        if (building == Player.SetProd):
            self.setPoruction(target, production)
            displayTimeAll = str(datetime.timedelta(hours=self.timeTaken)).split(".")[0]
            displayTimeCurrent = str(datetime.timedelta(hours=0)).split(".")[0]
            displayFrom18 = str(datetime.datetime.combine(datetime.date(2023,12,1), datetime.time(18,0,0)) + datetime.timedelta(hours=self.timeTaken)).split(".")[0]
            self.result.append([building + " " + target ,production, round(self.met), round(self.kris), round(self.deut), self.power,self.metMine, self.krisMine,self.deutMine, self.solar,self.getProduction(Player.Met), self.getProduction(Player.Kris), self.getProduction(Player.Deut), displayTimeCurrent, displayTimeAll,displayFrom18])
            return self.result
        
        #check if possible
        if not self.canBuild(building):
            waitTime,reason = self.wait(building)
            self.generateResources(waitTime)
            self.timeTaken += waitTime
            displayTimeAll = str(datetime.timedelta(hours=self.timeTaken)).split(".")[0]
            displayTimeCurrent = str(datetime.timedelta(hours=waitTime)).split(".")[0]
            displayFrom18 = str(datetime.datetime.combine(datetime.date(2023,12,1), datetime.time(18,0,0)) + datetime.timedelta(hours=self.timeTaken)).split(".")[0]
            self.result.append(["Wait " + reason,"-", round(self.met), round(self.kris), round(self.deut), self.power,self.metMine, self.krisMine,self.deutMine, self.solar,self.getProduction(Player.Met), self.getProduction(Player.Kris), self.getProduction(Player.Deut), displayTimeCurrent, displayTimeAll,displayFrom18])
        
        #get BuildTime
        time = self.getBuildTime(building)
        self.timeTaken += time
        #Add resources produced while building
        self.generateResources(time)
        #remove resources from building
        met,kris,deut = self.getBuildingCost(building)
        self.met -= met
        self.kris -= kris
        self.deut -= deut
        
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
            case Player.Robo:
                self.robo +=1
                resultBuldingLevel = self.robo
            case Player.Ship:
                self.ship +=1
                resultBuldingLevel = self.ship
            case Player.Combust:
                self.combust +=1
                resultBuldingLevel = self.combust
            case Player.Lab:
                self.lab +=1
                resultBuldingLevel = self.lab
            case Player.KT:
                self.kt +=1
                resultBuldingLevel = self.kt
            case Player.Etech:
                self.etech +=1
                resultBuldingLevel = self.etech
            case _:
                print("ERROR")
        self.updatePower()
        
        displayTimeAll = str(datetime.timedelta(hours=self.timeTaken)).split(".")[0]
        displayTimeCurrent = str(datetime.timedelta(hours=time)).split(".")[0]
        displayFrom18 = str(datetime.datetime.combine(datetime.date(2023,12,1), datetime.time(18,0,0)) + datetime.timedelta(hours=self.timeTaken)).split(".")[0]
        self.result.append([building,resultBuldingLevel, round(self.met), round(self.kris), round(self.deut), self.power,self.metMine, self.krisMine,self.deutMine, self.solar, self.getProduction(Player.Met), self.getProduction(Player.Kris), self.getProduction(Player.Deut), displayTimeCurrent, displayTimeAll, displayFrom18])
        return self.result
    
    def canBuild(self, building):
        met,kris,deut = self.getBuildingCost(building)
        return self.met >= met and self.kris >= kris and self.deut >= deut

    def getBuildTime(self, building):
        met,kris,deut = self.getBuildingCost(building)
        
        if building == Player.KT:
            #Ship
            return ((met + kris) / (self.buildSpeed * 2500 * (1 + self.ship))) * math.pow(2,self.nani)
        if building == Player.Combust or building == Player.Etech:
            #Research
             return ((met + kris) / (self.researchSpeed * 1000 * (1 + self.lab)))
        else:
            #Building
            return ((met + kris) / (self.buildSpeed * 2500 * (1 + self.robo))) * math.pow(0.5,self.nani)
    
    def getProduction(self, building):
        prod = 0
        match building:
            case Player.Met:
                prod = ((self.ressourceSpeed * 30 * self.metMine * math.pow(1.1,self.metMine)) * self.metProd ) + 40
            case Player.Kris:
                prod = ((self.ressourceSpeed * 20 * self.krisMine * math.pow(1.1,self.krisMine)) * self.krisProd) + 20
            case Player.Deut:
                prod = (self.ressourceSpeed * 10 * self.deutMine * math.pow(1.1,self.deutMine)*(1.44-0.004*50)) * self.deutProd
            case _:
                print("ERROR")
        
        percentalProd = 1
        if self.power < 0:
            percentalProd = self.generatedPower / self.consumedPower
            if percentalProd == 0:
                percentalProd = 0.1

        return prod * percentalProd
        
    def generateResources(self, time):
        metProduced = self.getProduction(Player.Met) * time
        self.met += metProduced
        
        kirsProduced = self.getProduction(Player.Kris) * time
        self.kris += kirsProduced
        
        deutProduced = self.getProduction(Player.Deut) * time
        self.deut += deutProduced
        
    def getBuildingCost(self, building):
        match building:
            case Player.Met:
                return ( 40*math.pow(1.5,self.metMine+1),
                         10*math.pow(1.5,self.metMine+1),
                         0)
            case Player.Kris:
                return ( 30*math.pow(1.6,self.krisMine+1),
                         15*math.pow(1.6,self.krisMine+1),
                         0)
            case Player.Deut:
                return ( 150*math.pow(1.5,self.deutMine+1),
                         50*math.pow(1.5,self.deutMine+1),
                         0)
            case Player.Solar:
                return ( 50*math.pow(1.5,self.solar+1),
                         20*math.pow(1.5,self.solar+1),
                         0)
            case Player.Robo:
                return ( math.pow(2,self.robo+1)*100,
                         math.pow(2,self.robo+1)*30,
                         math.pow(2,self.robo+1)*50)
            case Player.Ship:
                return ( math.pow(2,self.ship+1)*100,
                         math.pow(2,self.ship+1)*50,
                         math.pow(2,self.ship+1)*25)
            case Player.Combust:
                return ( 200*math.pow(2,self.combust),
                         0,
                         300*math.pow(2,self.combust))
            case Player.Lab:
                return ( math.pow(2,self.lab)*100,
                         math.pow(2,self.lab)*200,
                         math.pow(2,self.lab)*100)
            case Player.KT:
                return ( 2000,
                         2000,
                         0 )
            case Player.Etech:
                return ( 0,
                         400*math.pow(2,self.etech),
                         200*math.pow(2,self.etech) )
            case _:
                print("ERROR")
                
    def wait(self, building):
        met,kris,deut = self.getBuildingCost(building)
        
        requiredMet =  met - self.met
        requiredKris = kris - self.kris
        requiredDeut = deut - self.deut
        
        waitTimeMet = 0
        waitTimeKris = 0
        waitTimeDeut = 0
        reason = ""
        #if value > 0 it's required
        if (requiredMet > 0):
            waitTimeMet = (1 / self.getProduction(Player.Met)) * requiredMet
            reason +="Met "
        if (requiredKris > 0):
            waitTimeKris = (1 / self.getProduction(Player.Kris)) * requiredKris
            reason +="Kris "
        if (requiredDeut > 0):
            waitTimeDeut = (1 / self.getProduction(Player.Deut)) * requiredDeut
            reason +="Deut "

        return  (max(waitTimeMet,waitTimeKris,waitTimeDeut),reason)

if __name__ == "__main__":
    main()