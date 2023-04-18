import unittest
from domain.passenger import passenger
from domain.plane import plane

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.passenger1 = passenger("Ioan", "Costea", 9934567891239)
        self.passenger2 = passenger("Vlad", "Ao", 9934567891233)
        self.passenger3 = passenger("Alex", "Gheorge", 1134567891233)
        self.plane=plane("primul","rom",51,"bucuresti",[self.passenger1,self.passenger2])
    def test_crate(self):
        self.assertEqual(self.plane.get_name(),"primul")
        self.assertEqual(self.plane.get_airline_c(),"rom")
        self.assertEqual(self.plane.get_n_seats(),51)
        self.assertEqual(self.plane.get_destination(),"bucuresti")
        self.assertEqual(self.plane.print_passengers(),"The Passenger(Ioan Costea) with passport number:9934567891239\nThe Passenger(Vlad Ao) with passport number:9934567891233\n")
        #test errors
        self.assertRaises(ValueError,plane,[32,42],"rom",51,"bucuresti",[self.passenger1,self.passenger2])
        self.assertRaises(ValueError,plane,"primul",[32,42],51,"bucuresti",[self.passenger1,self.passenger2])
        self.assertRaises(ValueError,plane,"primul","rom",[32,42],"bucuresti",[self.passenger1,self.passenger2])
        self.assertRaises(ValueError,plane,"primul","rom",51,[32,42],[self.passenger1,self.passenger2])
    def test_returnNumberByName(self):
        self.assertEqual(self.plane.returnNumberByName("oa"),0)
        self.assertEqual(self.plane.returnNumberByName("Io"), 1)
        self.assertEqual(self.plane.returnNumberByName("Vl"), 1)
    def test_add_passanger(self):
        self.assertEqual(len(self.plane.get_passengers()),2)
        self.plane.add_passengers(self.passenger3)
        self.assertEqual(len(self.plane.get_passengers()), 3)
        self.plane.add_passengers(self.passenger3)
        self.assertEqual(len(self.plane.get_passengers()), 3)
        #it doesnt add if passport are the same
    def test_concatenatio(self):
        self.assertEqual(self.plane.concatenatio(),"2bucuresti")
        self.plane.add_passengers(self.passenger3)
        self.assertEqual(self.plane.concatenatio(),"3bucuresti")
    def test_starts3letter(self):
        self.assertEqual(self.plane.starts3letter(),True)
        self.plane.delete_passenger(9934567891239)
        self.assertEqual(self.plane.starts3letter(),False)
        self.plane.add_passengers(self.passenger3)
        self.assertEqual(self.plane.starts3letter(),False)
    def test_identifyPassengerContainsString(self):
        self.assertEqual(self.plane.identifyPassengerContainsString("oa"),['The Passenger(Ioan Costea) with passport number:9934567891239'])
        self.assertEqual(self.plane.identifyPassengerContainsString("la"),['The Passenger(Vlad Ao) with passport number:9934567891233'])
        self.assertEqual(self.plane.identifyPassengerContainsString("z"),[])
    def test_identifyPlaneWithPassengerName(self):
        self.assertEqual(self.plane.identifyPlaneWithPassengerName("Ioan","Costea"),True)
        self.assertEqual(self.plane.identifyPlaneWithPassengerName("Vlad","Ao"),True)
        self.assertEqual(self.plane.identifyPlaneWithPassengerName("Ioan","z"),False)


if __name__ == '__main__':
    unittest.main()
