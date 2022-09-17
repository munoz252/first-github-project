#camping_stuff = "tent, sleeping bag, water, raspberry pi, coffee, knife, ethernet cable, falsh drive"
#print(camping_stuff)
#python list needs []

#camping_list = ["test", "sleeping bag", "water", "raspberry pi", 
#"coffie", "flash drive"]

camp_site = ["crystal Lake", 404, 89.3, True]
#ORDERED SEQUUENCE, the list is numbered and you can call
#out that number, but it starts from "0"

# you can also count backwards starting at "-1"

#me = camping_list[4]
#print(me)
#you = camping_list[5]
#print(you)

supplies = ["tent", "sleeping bag", "water", "raspberry pi", 
"coffie", "flash drive"]

#append is a "method" built in python tool/function
#supplies.append("toilet paper")

#append can only add one item, extend adds another list
#supplies.extend(["toilet paper", "bidet"])
#supplies = supplies + ["toilet paper", "bidet"]

supplies.insert(0,"bidet")
#when we are inserting items -1 is second to last not last
supplies.insert(-1, "toilet paper")
#.clear clears() the entire list
#supplies.clear()

#supplies.remove("tent")

print("this item was just deleted: " +
supplies.pop(0))

supplies.pop(0)
print(supplies)