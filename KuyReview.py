import os
#import codereview Comingsoon
#import CodeReview Comingsoon
#import pylint

print("---------------------------------------------------------------------------------\n")

nama= "KuyReview Tools\n"
istools= "For review code from file,from folder, and from Github repository\n"
versi = "1.0.0\n"
devby = "Ananda Rauf Maududi\n"
devdate = "02 August 2023\n"
product= "Product from TMD Group\n"

print(nama)
print(istools)
print(versi)
print(devby)
print(devdate)
print(product)

print("---------------------------------------------------------------------------------\n")

class MenuKuyReview():
    def menu():
        print("Menu KuyReview Tools:\n")
        print
        print("1.Review code Python Projects")
        print("2.Review code all projects software development from file and folder")
        print("3.Review code all projects software development from Github Repository")
        print("4.Keluar")

class ReviewCodePy():
    def reviewpy(self):
        os.system("pylint KuyReview.py")
        print("Your Code under review!")
        print("Please check result")
        print("Thank You")

class ReviewCodeAll():
    def reviewaallfromfile(self):
        print("Library package CodeReview has Bug, and under maintenace")
        print("Thank You")
    
    def reviewallfromgithubrepo(self):
        print("Library package CodeReview has Bug, and under maintenace")
        print("Thank You")

MenuKuyReview.menu()

choosemenu = int(input("Please choose number on menu:"))
RevPY = ReviewCodePy()
RevAll = ReviewCodeAll()

if choosemenu== 1:
    RevPY.reviewpy()

elif choosemenu== 2:
    RevAll.reviewaallfromfile()

elif choosemenu== 3:
    RevAll.reviewallfromgithubrepo()

elif choosemenu== 4:
    print("Thanks for using ^-^")
    print("Dont forget share and give star ^-^")
    exit

else:
    print("Not found, sorry!")
    print("Please try again!")

MenuKuyReview.menu()
choosemenu = int(input("Please choose number on menu:"))



print("---------------------------------------------------------------------------------\n")
