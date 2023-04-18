import unittest
from domain.plane import plane
from domain.passenger import passenger
from infrastructure.planeRepo import planeRepo

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.p1 = passenger("Ioan", "Costea", 1234567891234)
        self.p1_1 = passenger("Ioan", "Costea", 1234567891000)
        self.p2 = passenger("Mihai", "Cosmin", 4234567891234)
        self.p3 = passenger("Vlad", "Andrei", 9934567891234)
        self.f1 = plane(1, "WIZZ", 12, "Bucharest", [self.p1,self.p1_1,self.p2,self.p3])
        self.f2 = plane(2, "Bizz", 35, "Cluj", [self.p3,self.p2,self.p1])
        self.plr1 = planeRepo()
        self.plr1.addPlane(self.f1)
        self.plr1.addPlane(self.f2)
        self.emptyRepo=planeRepo()
    def test_CRUD(self):
        self.assertEqual(len(self.plr1),2)
        self.plr1.delPlane(2)
        self.assertEqual(len(self.plr1), 1)
        self.plr1.delPlane(1)
        self.assertEqual(len(self.plr1),0)
        self.plr1.addPlane(self.f1)
        self.plr1.addPlane(self.f2)
        self.assertEqual(len(self.plr1),2)
        self.assertEqual(self.plr1.printPlane(1),"The Plane(1) from airline (WIZZ) with number of seats:12 and destination:Bucharest\n list of passengers :\nThe Passenger(Ioan Costea) with passport number:1234567891234\nThe Passenger(Ioan Costea) with passport number:1234567891000\nThe Passenger(Mihai Cosmin) with passport number:4234567891234\nThe Passenger(Vlad Andrei) with passport number:9934567891234\n")
        self.plr1.updatePlane(1,"WIZZ",42, "Buc", [self.p1,self.p1_1,self.p2,self.p3])
        self.assertEqual(self.plr1.getPlane(1).get_destination(),"Buc")
    def test_sortByLastName(self):
        self.assertEqual(self.plr1.getPlaneIndex(0).get_passengers(),[self.p1,self.p1_1,self.p2,self.p3])
        self.plr1.sortByLastName(1)
        self.assertEqual(self.plr1.getPlaneIndex(0).get_passengers(),[self.p3,self.p2,self.p1_1,self.p1,])
        self.plr1.sortByLastName(2)
        self.assertEqual(self.plr1.getPlaneIndex(1).get_passengers(),[self.p3,self.p2,self.p1])
    def test_sortPlanesByNumberOfSeats(self):
        self.assertEqual(self.plr1.getPlaneIndex(0),self.f1)
        self.plr1.sortPlanesByNumberOfSeats()
        self.assertEqual(self.plr1.getPlaneIndex(0),self.f2)
        self.plr1.updatePlane(1,"WIZZ",12, "Buc", [self.p3])
        self.plr1.sortPlanesByNumberOfSeats()
        self.assertEqual(self.plr1.getPlaneIndex(0),self.f1)
    def test_sortPlanesConcatenation(self):
        self.assertEqual(self.plr1.getPlaneIndex(0),self.f1)
        self.plr1.sortPlanesConcatenation()
        self.assertEqual(self.plr1.getPlaneIndex(0),self.f2)
    def test_identifyPassengerWithPassportPrefix(self):
        for elem in self.plr1.identifyPassengerWithPassportPrefix():
            sol=elem
        self.assertEqual(sol.get_name(),1)
    def test_identifyPassengerContainsString(self):
        self.assertEqual(len(self.plr1.identifyPassengerContainsString(1,"oa")),2)
        self.assertEqual((self.plr1.identifyPassengerContainsString(1,"oa")[0]),"The Passenger(Ioan Costea) with passport number:1234567891234")
        self.assertEqual((self.plr1.identifyPassengerContainsString(1,"oa")[1]),"The Passenger(Ioan Costea) with passport number:1234567891000")
    def test_identifyPlaneWithPassengerName(self):
        for elem in self.plr1.identifyPlaneWithPassengerName("Ioan","Costea"):
            sol=elem
        self.assertEqual(sol.get_name(),2)
        p5 = passenger("1dd", "And32ei", 9934567891234)
        self.plr1.updatePlane(1, "WIZZ", 12, "Bucharest", [self.p1,self.p1_1,self.p2,self.p3,p5])
        for elem in self.plr1.identifyPlaneWithPassengerName("1dd", "And32ei"):
            sol=elem
        self.assertEqual(sol.get_name(),1)

if __name__ == '__main__':
    unittest.main()
