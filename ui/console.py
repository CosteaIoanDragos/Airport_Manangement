from domain.passenger import passenger
from domain.plane import plane
from infrastructure.planeRepo import planeRepo
from controller.controller import AirportController
def print_menu():
    print("\nType '1' to list all commands\nType '0' to finish the program")
    print("0 - exit")
    print("1 - help")
    print("2 - List of Planes")
    print("3 - Add Plane")
    print("4 - Delete Plane")
    print("5 - Sort the passengers in a plane by last name")
    print("6 - Sort planes according to the number of passengers")
    print("7 - Sort planes according to the number of passengers with the first name starting with a given substring")
    print("8 - Sort planes according to the string obtained by concatenation of the number of passengers in the plane and the destination")
    print("9 - Identify  planes  that  have  passengers  with  passport  numbers  starting  with  the  same 3 letters")
    print("10 - Identify  passengers  from  a  given  plane  for  which  the  first  name  or  last  namecontain a string given as parameter")
    print("11 - Identify plane/planes where there is a passenger with given name")
    print("12 - Form groups of 𝒌 passengers from the same plane but with different last names")
    print("13 - Form  groups  of  𝒌  planes  with  the  same  destination  but  belonging  to  different  airline companies ")
def printCrud():
    print("1-add")
    print("2-delete")
    print("3-update")
    print("select passenger (crude opperations)")
def run(controller :AirportController):
    print_menu()
    p1 = passenger("Ioan", "Costea", 1234567891234)
    p1_1 = passenger("Ioan", "Costea", 1234567891000)
    p2 = passenger("Mihai", "Cosmin", 4234567891234)
    p3 = passenger("Vlad", "Andrei", 9934567891234)
    f1 = plane("1", "WIZZ", 12, "Bucharest", [p1, p1_1, p2, p3])
    f2 = plane("2", "Bizz", 35, "Cluj", [p3, p2, p1])
    controller.addPlane(f1)
    controller.addPlane(f2)
    command = input(">>> ")
    while command !="0":
        if command=="1":
            print_menu()
        elif command=="2":
            if len(controller)==0:
                print("No plane")
            else:
                print(controller)
        elif command=="3":
            try:
            name=input("Numele avionului:")
            airline_c=input("Compania :")
            nr_seats=int(input("Nr locuri:"))
            destination=input("Destinatia:")

                f3=plane(name,airline_c,nr_seats,destination,[])
            except ValueError as ex:
                print(f"Enter the right info.\n{ex}")

            nr_pasenger=int(input("Cati pasageri va avea avionul?"))
            for i in range(nr_pasenger):
                nume_p=input("Numele pasagerului:")
                prenume=input("prenumele pasagerului:")
                passaport=int(input("passaport: "))
                p3=passenger(nume_p,prenume,passaport)
                f3.add_passengers(p3)
            controller.addPlane(f3)
        elif command=="4":
            nume=input("numele avionului de sters")
            controller.delPlane(nume)
        elif command=="5":
            plane1=input("Numele avionului")
            controller.sortByLastName(1)
        elif command=="6":
            controller.sortPlanesByNumberOfSeats()
        elif command=="7":
            name=input("substring:")
            controller.sortPlanesWithNameByNrSeats(name)
        elif command=="8":
            controller.sortPlanesConcatenation()
        elif command=="9":
            for elem in controller.identifyPassengerWithPassportPrefix():
                print(elem)

        elif command=="10":
            plane1=input("plane name:")
            name=input("string :")
            print(controller.identifyPassengerContainsString(plane1,name))
        elif command=="11":
            fname=input("First name")
            lname=input("Last name")
            for elem in controller.identifyPlaneWithPassengerName("Ioan", "Costea"):
                print(elem)
        elif command=="12":
            pname=input("plane name")
            k=int(input("k"))
            controller.formGroupsInPlaneame(pname,k)
        elif command=="13":
            pname = input("destination name")
            k = int(input("k"))
            print(controller.formGroupsByDestination(pname,k))
        else:
            print("Command not def")
        #print_menu()
        command=input(">>>>>>")
