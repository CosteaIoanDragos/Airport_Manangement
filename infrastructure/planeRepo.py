from domain.plane import plane
from utils.backtrack import combinations
from utils.searchsort import mySearch
from utils.searchsort import mySort
from utils.searchsort import mySearch1
from domain.passenger import passenger#de sters
class planeRepo:
    def __init__(self):
        self.__data=[]
    def __str__(self):
        s=""
        for elem in self.__data:
            s+=str(elem)+"\n"
        return s
    def __len__(self):
        return len(self.__data)

    def addPlane(self,st):
        for elem in self.__data:
            if elem.get_name()==st.get_name():
                ValueError("Plane already exists")
        self.__data.append(st)
    def delPlane(self,name):
        for i in range(len(self.__data)-1,-1,-1):
            if name==self.__data[i].get_name():
                del self.__data[i]
    def updatePlane(self,name,airline_c,n_seats,destination,l_passengers):
        for elem in self.__data:
            if name==elem.get_name():
                try:
                    elem.set_airline_c(airline_c)
                    elem.set_n_seats(n_seats)
                    elem.set_destination(destination)
                    elem.set_passengers(l_passengers)
                except:
                    ValueError("Somtingh is wrong")
    def getPlaneIndex(self,index):
        return self.__data[index]
    def getPlane(self,name):
        """
        return objesct type from list
        :param name:
        :return:
        """
        for i in range(len(self.__data)):
            if name==self.__data[i].get_name():
                return self.__data[i]
    def printPlane(self,name):
        """
        used for string representation of a plane from repo
        :param name:
        :return:
        """
        for i in range(len(self.__data)):
            if name==self.__data[i].get_name():
                return str(self.__data[i])


    #3

    def sortByLastName(self,plane):
        s=self.getPlane(plane)
        l_passengers=s.get_passengers()
        l_passengers=mySort(l_passengers,lambda elem1,elem2:elem1.get_lname()<elem2.get_lname())
        s.set_passengers(l_passengers)
    #4

    def sortPlanesByNumberOfSeats(self):
        self.__data=mySort(self.__data,lambda elem1,elem2:elem1.passagers_number()<elem2.passagers_number())


    #5
    def sortPlanesWithNameByNrSeats(self,name):
        self.__data=mySort(self.__data,lambda elem1,elem2:elem1.returnNumberByName(name)<elem2.returnNumberByName(name))


    #6

    def sortPlanesConcatenation(self):
        self.__data=mySort(self.__data,lambda elem1,elem2:elem1.concatenatio()<elem2.concatenatio())
    #7

    def identifyPassengerWithPassportPrefix(self):
        return mySearch(self.__data,lambda elem:elem.starts3letter())

    #8

    def identifyPassengerContainsString(self,plane1,name):
        for elem in self.__data:
            if elem.get_name()==plane1:
                return elem.identifyPassengerContainsString(name)
    #9
    def identifyPlaneWithPassengerName(self, fname, lname):
        return mySearch(self.__data,lambda elem:elem.identifyPlaneWithPassengerName(fname,lname))

    #10

    def formGroupsByDestination(self,d1,k):
        p=list(self.__data)
        z1=[]
        destinatie=p[0].get_destination()
        existenta=[]
        for i in range(len(p)-1):
            z=p[i].get_destination()
            ok=1
            for elem in existenta:
                if elem ==z:
                    ok=0

            if ok==1:
                existenta.append(z)
                z1=[]
                z1.append(p[i].get_name())
                for j in range(i+1,len(self.__data)):
                    if p[j].get_destination()==z :
                        z1.append(p[j].get_name())
                        #print(p[j])

                if d1==z:
                    print(f"destinatia: {z} ")
                    for combination in combinations(z1,k):
                        print(f"\t{combination}")
    def formGroupsInPlaneame(self,planeName,k):
        all=[]
        for elem in self.__data:
            if elem.get_name()==planeName:
                all=elem.get_passengers().copy()
        all1=[]

        for elem in all:
            ok=0
            for e in all1:
                if elem.get_lname()==e:
                    ok=1
            if ok==0:
                all1.append(elem.get_lname())

        for combination in combinations(all1, k):
            print(f"\t{combination}")

if __name__=="__main__":
    p1 = passenger("Ioan", "Costea", 1234567891234)
    p1_1 = passenger("Ioan", "Costea", 1234567891000)
    p2 = passenger("Mihai", "Cosmin", 4234567891234)
    p3 = passenger("Vlad", "Andrei", 9934567891234)
    f1 = plane(1, "WIZZ", 54, "Bucharest", [p1, p1_1, p2, p3])
    f2 = plane(2, "Bizz", 35, "Cluj", [p3, p2, p1])
    plr1 = planeRepo()
    plr1.addPlane(f1)
    plr1.addPlane(f2)
    print(plr1)
    print("######")
    plr1.sortByLastName(1)
    print(plr1)
    print("######")

    plr1.sortPlanesByNumberOfSeats()
    print(plr1)
    print("######")
    plr1.sortPlanesWithNameByNrSeats("oa")
    print(plr1)
    print("######1")
    plr1.sortPlanesConcatenation()
    print(plr1)
    print("######2")
    for elem in plr1.identifyPassengerWithPassportPrefix():
        print(elem)
    print("######3")
    for elem in plr1.identifyPlaneWithPassengerName("Ioan","Costea"):
        print(elem)
    print("######4")

    print(plr1.identifyPassengerContainsString(1,"oa"))

    plr1.delPlane(1)
    print("423442")
    print(plr1)