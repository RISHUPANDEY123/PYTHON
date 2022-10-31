def compound_interest(principle , time , rate):
     Amount= principle*(pow((1 + rate /100),time))
     CI = Amount-principle
     print("the compound interest is", CI)

compound_interest(1000,10,3.25)