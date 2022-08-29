#*ARGS - parameter that will pack all arguments into a tuple

#def add (*args):
    #sum = 0
    #for i in args :
        #sum +=i
    #return sum

#print(add (4,5,6,7,8,9,10))


#**KWARGS -parameter that will pack all arguments into dictionary
 
#def hello(**kwargs):
    #print("Hello",end=" ")
    #for key,value in kwargs.items():
        #print (value,end=" ")
#hello(title="Mr",first=1,hell = "hahaha")


#str.format() = optional method that give users more
#               control when displayin output
#animal = "cow"
#item = "moon"

#print ("The "+animal+"jumped over the "+ item)
#print ("The {0} jumped over to the {0}".format(animal,item))
#print ("The {animal} jumped over to the {item}".format(animal="cow",item="moon"))

#text = "Hi {} putang ina {}"
#print(text.format("Carlo","ulol"))

#name = "CARLO"

#print("Helol my name is {}".format(name))
#print("Helol my name is {:10}. Nice to meet you".format(name))
#print("Helol my name is {:<10}. Nice to meet you".format(name))
#print("Helol my name is {:>10}. Nice to meet you".format(name))
#print("Helol my name is {:^10}. Nice to meet you".format(name))

#number = 3.14568
#large_number = 100000000

#print ("The number is {:.3f}".format(number))
#print ("The number is {:,}".format(large_number)) putting commas in every thousanth
#print ("The number is {:b}".format(large_number)) #making binary
#print ("The number is {:o}".format(large_number)) #octal
#print ("The number is {:X}".format(large_number)) #x or X fo hexa
#print ("The number is {:e}".format(large_number)) #e or E for scientific notation


#random mdule
#import random

#x = random.randint(1,6) #random number within the range of arguments
#y = random.random( ) #random floating number less than 1
#mylist = ["rock","paper","scissors"]
#z = random.choice(mylist) # random choice with in the list

#cards = [1,2,3,4,5,6,7,8,9,"Q","K","A"]
#random.shuffle(cards) #shuffleling the lst
#print (cards)


#exception 
#try:
    #numerator = eval(input("Enter number to divide: "))
    #denominator = eval(input("Enter number to divide by: "))

    #result = numerator / denominator

    #print (result)
#except Exception as e: #all errors
    #print (e)
    #print ("somethin went wrong")
#except ZeroDivisionError as e:
    #print (e)
    #print ("Your denominator is 0 cant divide")
#except ValueError as e:
    #print (e)
    #print("Please put number only")
#finally:
   # print("This will always execute")

    







