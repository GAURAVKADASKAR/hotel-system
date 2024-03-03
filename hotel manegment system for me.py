class hotel:
    def __init__(self,tr='',r=0,l=0,g=0,sv=1000,rm=0,name='',addre='',cindate='',coutdate=''):
        self.tr=tr
        self.r=r
        self.l=l
        self.g=g
        self.sv=sv
        self.rm=rm
        self.name=name
        self.addre=addre
        self.cindate=cindate
        self.coutdate=coutdate
    def roombook(self):
        print("press 1 for type ->7000/night")
        print("press 2 for type ->5000/night")
        print("press 3 for type ->3000/night")
        print("press 4 for type ->1000/night")
        c1=int(input("Enter your choice : "))
        night=int(input("Enter how many night's do you wants to stay : "))
        if(c1==1):
            self.r=self.r+7000*night
        elif(c1==2):
            self.r=self.r+5000*night
        elif(c1==3):
            self.r=self.r+3000*night
        elif(c1==4):
            self.r=self.r+1000*night
        else:
            print("please enter the correct choice")
        print("total room bill is -> ",self.r)
    def data(self):
        self.name=input("Enter your name : ")
        self.addre=input("Enter your address : ")
        self.cindate=input("Enter your cheack in date : ")
        self.coutdate=input("Enter your cheack out date : ")
        print("your rome number is : ",101)
    def food(self):
        while(1):
            print("press 1 for tea->10rs")
            print("press 2 for water bottel ->15rs")
            print("press 3 for breakfast ->50rs")
            print("press 4 for lunch ->100rs")
            print("press 5 for dinner ->200rs")
            print("press 6 for exit")
            c2=int(input("Enter your choice : "))
            if(c2==1):
                q=int(input("Enter the quantity : "))
                self.rm=self.rm+10*q
            elif(c2==2):
                q = int(input("Enter the quantity : "))
                self.rm=self.rm+15*q
            elif(c2==3):
                q = int(input("Enter the quantity : "))
                self.rm=self.rm+50*q
            elif(c2==4):
                q = int(input("Enter the quantity : "))
                self.rm=self.rm+100*q
            elif(c2==5):
                q = int(input("Enter the quantity : "))
                self.rm=self.rm+200*q
            elif(c2==6):
                break;
            else:
                print("please enter the correct choice ")

    def laundry(self):
        while(1):
            print("press 1 for shirt ->10rs")
            print("press 2 for trouser ->50rs")
            print("press 3 for t-shirt ->20rs")
            print("press 4 for other ->100rs")
            print("press 5 for exit")
            c3=int(input("Enter the choice : "))
            if(c3==1):
                q1=int(input("Enter the quantity : "))
                self.l=self.l+10*q1
            elif(c3==2):
                q1 = int(input("Enter the quantity : "))
                self.l=self.l+50*q1
            elif(c3==3):
                q1 = int(input("Enter the quantity : "))
                self.l=self.l+20*q1
            elif(c3==4):
                self.l=self.l+100*q1
            elif(c3==5):
                break;
            else:
                print("please enter the correct choice")
    def game(self):
        while(1):
            print("press 1 for carrom ->100rs/game")
            print("press 2 for chese->200rs/game")
            print("press 3 for pole->500rs/game")
            print("press 4 for ludo->100rs/game")
            print("press 5 for computer game->1000rs/game")
            print("press 6 for exit")
            c4=int(input("Enter your choice : "))
            if(c4==1):
                q4 = int(input("Enter the quantity : "))
                self.g=self.g+100*q4
            elif(c4==2):
                q4 = int(input("Enter the quantity : "))
                self.g=self.g+200*q4
            elif(c4==3):
                q4 = int(input("Enter the quantity : "))
                self.g=self.g+500*q4
            elif(c4==4):
                q4 = int(input("Enter the quantity : "))
                self.g=self.g+100*q4
            elif(c4==5):
                q4 = int(input("Enter the quantity : "))
                self.g=self.g+1000*q4
            elif(c4==6):
                break;
            else:
                print("please Enter the correct choice")
    def total(self):
        c=self.rm+self.r+self.l+self.g
        self.tr=c+self.sv
        print("totla bill ",c)
        print("total bill with service charges ",self.tr)
    def bill(self):
        print('name is : ',self.name)
        print("address is : ",self.addre)
        print("cheackin date : ",self.cindate)
        print("cheackout date : ",self.coutdate)
        print("total charge ",self.tr)
def main():
    aa=hotel()
    while(1):
        print("--------------------WELCOME TO DIVINE HOTEL--------------------")
        print("press 1 for book a room")
        print("press 2 for Enter the data ")
        print("press 3 for food")
        print("press 4 for laundry")
        print("press 5 for game")
        print("press 6 for finding total bill only")
        print("press 7 for display bill")
        print("press 8 for exit")
        cc=int(input("Enter the choice "))
        if(cc==1):
            aa.roombook()
        elif(cc==2):
            aa.data()
        elif(cc==4):
            aa.laundry()
        elif(cc==3):
            aa.food()
        elif(cc==5):
            aa.game()
        elif(cc==7):
            aa.bill()
        elif(cc==6):
            aa.total()
        elif(cc==8):
            break;
        else:
            print("Please enter the correct choice")
main()