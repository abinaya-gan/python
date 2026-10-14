class Multiplefunctions():
    def Subfields():
        fields = ["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("Sub-fields in AI are:")
        for field in fields:
           print(field)

    def OddEven():
        num = int(input("Enter a number: "))

        if num % 2 == 0:
            print(num, "is Even number")
        else:
            print(num, "is Odd number")
    

    def Elegible():
        gender = input("Your Gender: ")
        age = int(input("Your age: "))
        
        if (gender == "Male"):
           if(age >= 21):
             print("ELIGIBLE")
           else:
             print("Not ELIGIBLE")
        elif (gender == "Female"):
           if(age >= 18):
             print("ELIGIBLE")
           else:
             print("Not ELIGIBLE")  

    def percentage():
        sub1= int(input("Subject1 :"))
        sub2= int(input("Subject2 :"))
        sub3= int(input("Subject3 :"))
        sub4= int(input("Subject4 :"))
        sub5= int(input("Subject5 :"))
        
        lists = [sub1,sub2,sub3,sub4,sub5]
        total=0
        count=0
        for sub in lists:
            total=total+sub
            count = count+1
            
        percentage= total/count
        print("Total :",total)
        print("Percentage :",percentage)        

    def triangle():
        height=int(input("Height: "))
        breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle: ", height*breadth/2)
        height1=int(input("Height1: "))
        height2=int(input("Height2: "))
        breadth1=int(input("Breadth: "))
        print("Perimeter formula: Height1+Height2+Breadth")
        
        lists = [height1,height2,breadth1]
        perimeter=0
        for field in lists:
          perimeter=perimeter+field
        print("Perimeter of Triangle: ",perimeter)
        
    