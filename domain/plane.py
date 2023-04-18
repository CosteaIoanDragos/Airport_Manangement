from domain.passenger import passenger
class plane:
    """

    """
    def __init__(self,name,airline_c,n_seats,destination,passenger_list):

        if type(name)==int or type(name)==str:
            self.__name=name
        else:
            raise ValueError("Name of plaane not correct")
        if type(airline_c)==str:
            self.__airline_c=airline_c
        else:
            raise ValueError("Airline not correct")
        if type(n_seats)==int and n_seats>=0:
            self.__n_seats=n_seats
        else:
            raise ValueError("Number of seats not correct")
        if type(destination)==str:
            self.__destination=destination
        else:
            raise ValueError("Destination not a string")
        self.__passenger_copy = []
        for pas in passenger_list:
            self.__passenger_copy.append(pas)


    def __str__(self):
        """

        :return:
        """

        return "The Plane("+str(self.__name)+") from airline ("+str(self.__airline_c)+") with number of seats:"+str(self.__n_seats)+" and destination:"+str(self.__destination)+"\n list of passengers :\n" +self.print_passengers()
    def set_name(self,name):
        if type(name) == int or type(name) == str:
            self.__name = name
    def set_airline_c(self,airline_c):
        if type(airline_c)==str:
            self.__airline_c=airline_c
        else:
            raise ValueError("Airline not correct")
    def set_n_seats(self,n_seats):
        if type(n_seats)==int and n_seats>=0:
            self.__n_seats=n_seats
        else:
            raise ValueError("Number of seats not correct")
    def set_passengers(self,passenger_list):
        self.__passenger_copy = []
        for pas in passenger_list:
            self.__passenger_copy.append(pas)
    def add_passengers(self,passenger):
        ok=1
        for elem in self.__passenger_copy:
            if passenger.get_passport()==elem.get_passport():
                return ValueError
        self.__passenger_copy.append(passenger)
    def set_destination(self,destination):
        self.__destination=destination
    def get_passengers(self):
        passenger = []
        for pas in self.__passenger_copy:
            passenger.append(pas)
        return passenger
    def print_passengers(self):
        s=""
        for elem in self.get_passengers():
           s=s+str(elem)+"\n"
        return s
    def get_name(self):
        return self.__name
    def get_airline_c(self):
        return self.__airline_c
    def get_destination(self):
        return self.__destination
    def get_n_seats(self):
        return self.__n_seats
    def delete_passenger(self,passport):
        for i in range(len(self.__passenger_copy)-1,-1,-1):
            if self.__passenger_copy[i].get_passport()==passport:
                del self.__passenger_copy[i]
    def returnNumberByName(self,name):
        counter=0
        for elem in self.__passenger_copy:
            if elem.get_fname().startswith(name):
                counter=counter+1
        return counter
    def concatenatio(self):
        return str(len(self.__passenger_copy)) + self.__destination
    def starts3letter(self):
        for i in range (len(self.__passenger_copy)-1):
            if str(self.__passenger_copy[i].get_passport())[0:3]==str(self.__passenger_copy[i+1].get_passport())[0:3]:
                return True
        return False
    def identifyPassengerContainsString(self,name):
        s = []
        for elem in self.__passenger_copy:
            if name in elem.get_fname() or name in elem.get_lname():
                s.append(str(elem))
        return s

    def identifyPlaneWithPassengerName(self,fname,lname):
        for elem in self.__passenger_copy:
            if fname == elem.get_fname() and lname == elem.get_lname():
                return True
        return False
    def passagers_number(self):
        return len(self.__passenger_copy)
if __name__ == "__main__":
    #data examples
    z =passenger("ioan", "Costea", 9934567891239)
    x=passenger("vlad", "Ao", 9934567891233)
    y=passenger("Alex", "Gheorge", 1134567891233)
    f=plane("primul","rom",51,"bucuresti",[z,x])

    print(f.get_passengers())
    print(f)
    f.add_passengers(y)
    print(f)
    print(f.starts3letter())
    print(f.identifyPassengerContainsString("le"))
    print(f.returnNumberByName("io"))
    f.add_passengers(y)
    f.add_passengers(y)
    print(f)
    f.set_n_seats(42)
    print(f)