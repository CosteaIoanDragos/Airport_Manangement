import unittest
from domain.passenger import passenger

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.passanger1 = passenger("Ioan", "Costea", 1234567891234)
        self.passanger2 = passenger("Vlad","Gheorghe",9994567891234)
    def test_crate(self):
        self.assertEqual(self.passanger1.get_lname(),"Costea")
        self.assertEqual(self.passanger1.get_fname(),"Ioan")
        self.assertEqual(self.passanger1.get_passport(),1234567891234)
        self.assertEqual(str(self.passanger1),"The Passenger(Ioan Costea) with passport number:1234567891234")
        #test errors
        self.assertRaises(ValueError,passenger,123,"Costea",1234567891234)
        self.assertRaises(ValueError,passenger,"Ioan",123,1234567891234)
        self.assertRaises(ValueError,passenger,"Ioan","Costea",[12345,67891234])
        #test setters getters
        self.passanger1.set_passport(1234567891000)
        self.assertEqual(self.passanger1.get_passport(),1234567891000)
        self.assertEqual(self.passanger1.get_fname(),"Ioan")
        self.passanger1.set_lname("George")
        self.passanger1.set_fname("Alex")
        self.assertEqual(self.passanger1.get_fname(), "Alex")
        self.assertEqual(self.passanger1.get_lname(),"George")
        #test errors
        self.assertRaises(ValueError,self.passanger1.set_fname,[32,32])
        self.assertRaises(ValueError,self.passanger1.set_lname,[32,32])
        self.assertRaises(ValueError,self.passanger1.set_passport,[32,32])

if __name__ == '__main__':
    unittest.main()
