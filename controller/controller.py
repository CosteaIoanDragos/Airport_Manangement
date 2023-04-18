from domain.passenger import passenger
from domain.plane import plane
from infrastructure.planeRepo import planeRepo
from utils.backtrack import combinations
from utils.searchsort import mySearch
from utils.searchsort import mySort
from utils.searchsort import mySearch1
class AirportController:

    def __init__(self,planeRepo:planeRepo=planeRepo()):
        self.__airportrepo=planeRepo
    def __len__(self):
        return len(self.__airportrepo)
    def __str__(self):
        return str(self.__airportrepo)
    def addPlane(self,st):
        self.__airportrepo.addPlane(st)
    def delPlane(self,name):
        self.__airportrepo.delPlane(name)
    def updatePlane(self,name,airline_c,n_seats,destination,l_passengers):
        self.__airportrepo.updatePlane(name,airline_c,n_seats,destination,l_passengers)
    def getPlaneIndex(self,index):
        return self.__airportrepo.getPlaneIndex(index)
    def getPlane(self,name):
        return self.__airportrepo.getPlane(name)
    def printPlane(self,name):
        return self.__airportrepo.printPlane(name)
    def sortByLastName(self,plane):
        self.__airportrepo.sortByLastName(plane)
    def sortPlanesByNumberOfSeats(self):
        self.__airportrepo.sortPlanesByNumberOfSeats()
    def sortPlanesWithNameByNrSeats(self,name):
        self.__airportrepo.sortPlanesWithNameByNrSeats(name)
    def sortPlanesConcatenation(self):
        self.__airportrepo.sortPlanesConcatenation()
    def identifyPassengerWithPassportPrefix(self):
        return self.__airportrepo.identifyPassengerWithPassportPrefix()
    def identifyPassengerContainsString(self,plane1,name):
        return self.__airportrepo.identifyPassengerContainsString(plane1,name)
    def identifyPlaneWithPassengerName(self, fname, lname):
        return self.__airportrepo.identifyPlaneWithPassengerName(fname,lname)
    def formGroupsByDestination(self,d1,k):
        return self.__airportrepo.formGroupsByDestination(d1,k)
    def formGroupsInPlaneame(self,planeName,k):
        return self.__airportrepo.formGroupsInPlaneame(planeName,k)
if __name__=="__main__":
    p1 = passenger("Ioan", "Costea", 1234567891234)
    p1_1 = passenger("Ioan", "Costea", 1234567891000)
    p2 = passenger("Mihai", "Cosmin", 4234567891234)
    p3 = passenger("Vlad", "Andrei", 9934567891234)
    f1 = plane(1, "WIZZ", 12, "Bucharest", [p1, p1_1, p2, p3])
    f2 = plane(2, "Bizz", 35, "Cluj", [p3, p2, p1])
    plr1 = planeRepo()
    plr1.addPlane(f1)
    plr1.addPlane(f2)
    print(plr1)
    plr1.formGroupsInPlaneame(1,2)