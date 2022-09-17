week_temps_f = "75.1,77.7,83.2,82.5,81.0,79.5,85.7"
n= week_temps_f.split(",")
print(n)

new = [float(i) for i in n]
print(new)

average_temp= (sum(new))/7
print(average_temp)


#new problem, create a list of numbers from 0 to 67)
for n in range(69):
    print(n)

#print(range(n))
nums= (list(range(n)))
print(nums)