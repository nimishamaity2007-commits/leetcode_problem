class UndergroundSystem:

    def __init__(self):
        self.customer={}
        self.station={}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.customer[id]=(stationName,t)
    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation,startTime=self.customer.pop(id)
        trip=startStation,stationName
        if trip in self.station:
            self.station[trip][0]+=(t-startTime)
            self.station[trip][1]+=1
        else:
            self.station[trip]=[t-startTime,1]    
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trip=(startStation,endStation)
        return self.station[trip][0]/self.station[trip][1]
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)