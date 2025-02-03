""" A program that ask the user for sandwich ingredients and how many sandwiches
    and return The price"""
import pyinputplus as py
prices={"wheat":0.5,"white":0.25,"sourdough":0.5,
        "chicken":0.35,"turkey":0.35,"ham":0.25,
        "tofu":40,"cheddar":0.2,"swiss":0.3,
        "mozzarella":0.3,"mayo":0.1,"mustard":0.1,
        "tomato":0.1,
}
total_cost=[]
choices=[]
bread_type=["wheat", "white","sourdough"]
protein_type=["chicken", "turkey", "ham","tofu"]
cheese_type=["cheddar","swiss","mozzarella"]

# ask for bread type
choose_bread=py.inputMenu(prompt="What is the type of bread do you want:\n"\
                        ,choices=bread_type,numbered=abs)
choices.append(choose_bread)
# ask for protein type
choose_protein=py.inputMenu(prompt="What is the type of protein do you want: \n "\
                            ,choices=protein_type,numbered=abs)
choices.append(choose_protein)
# ask if they want cheese
ask_cheese=py.inputYesNo(prompt="Do you want cheese? ")
if ask_cheese =="yes":
    ask_cheese_type=py.inputMenu(prompt="What is the type of cheese do you want?\n"\
                                ,choices=cheese_type,numbered=abs)
    choices.append(ask_cheese_type)
# ask for mayo, mustard, lettuce, or tomato
ask_mayo=py.inputYesNo(prompt="Do you want mayo? ")
if ask_mayo =='yes':
    choices.append("mayo")

ask_mustard=py.inputYesNo(prompt="Do you want mustard? ")
if ask_mustard =="yes":
    choices.append("mustard")
ask_tomato=py.inputYesNo(prompt="Do you want tomato? ")
if ask_tomato =="yes":
    choices.append("tomato")
# Using inputInt() to ask how many sandwiches they want. Make sure this number is 1 or more.
ask_how_many_sandwiches=int(py.inputInt(prompt="How many sandwiches do you want? ",max=10,min=1))
for k ,v in prices.items():
    if k in choices:
        total_cost.append(v)
new_check=sum(total_cost)
new_check_total=new_check*ask_how_many_sandwiches
print("Total sandwich price: "+str(new_check_total)+"$")
