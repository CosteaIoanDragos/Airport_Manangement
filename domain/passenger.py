class passenger:
    def __init__(self,f_name,l_name,passport):
        """

        """
        if type(f_name)==str and type(l_name)==str:
            self.__f_name=f_name
        else :
            raise ValueError("Names are not a string")
        if type(l_name)==str:
            self.__l_name=l_name
        else :
            raise ValueError("Names are not a string")
        if type(passport)==int:
            self.__passport=passport
        else:
            raise ValueError("Passport not a number")
    def __str__(self):
        return "The Passenger("+str(self.__f_name)+" "+str(self.__l_name)+") with passport number:"+str(self.__passport)
    def set_fname(self,f_name):
        if type(f_name) == str:
            self.__f_name=f_name
        else :
            raise ValueError("Names are not a string")
    def set_lname(self,l_name):
        if type(l_name) == str:
            self.__l_name=l_name
        else :
            raise ValueError("Names are not a string")
    def set_passport(self,passport):
        if type(passport)==int and len(str(passport))==13:
            self.__passport=passport
        else:
            raise ValueError("Passport not a number")
    def get_fname(self):
        return self.__f_name
    def get_lname(self):
        return self.__l_name
    def get_passport(self):
        return self.__passport

if __name__ == "__main__":
    # data examples

    f=passenger("ioan","Costea",1234567891234)
    print(f)
    f.set_passport(1234567891233)
    print(f)
    f.set_lname("dragos")
    print(f)
    f.set_fname("Ioan")
    print(f)
