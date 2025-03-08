import random
import time

no_of_houses = 10
refuse_start = 0
refuse_size = 200

houses = []
for i in range(1, 11):
	house = i
	houses.append(f"house{house} : {random.randint(1,7)} persons")
print(houses)
print(int(houses[9][10]))

food_per_person = 50

consumption_rate = []
for i in range(len(houses)):
	try:
	    food_consumption = int(houses[i][9]) * 50
	    consumption_rate.append(food_consumption)

	except:
		food_consumption_last = int(houses[9][10]) * 50
		consumption_rate.append(food_consumption_last)

gabbage = []
for i in range(len(houses)):
	try:
		refuse = int(houses[i][9]) * 0
		gabbage.append(refuse)

	except:
		refuse_last = int(houses[9][10]) * 0
		gabbage.append(refuse_last)



print(f"Food supply: {consumption_rate}")

def restock():
	for i in range(len(houses)):
		try:
			food_consumption = int(houses[i][9]) * 50
			# print(food_consumption, 'yes')
			c_consumption_rate.insert(i, food_consumption)

		except:
			# c_consumption_rate.remove([9])
			food_consumption_last = int(houses[9][10]) * 50
			c_consumption_rate.insert(9, food_consumption_last)
	# print(c_consumption_rate)


def clear_refuse():
	for i in c_gabbage:
		try:
			if i > 200:
				refuse = 0
				c_gabbage.insert(i, refuse)

		except:
			if i > 200:
				refuse_last = 0
				c_gabbage.insert(9, refuse_last)	




simul = True
while simul == True:
	time.sleep(3)
	c_consumption_rate = []
	c_gabbage = []
	for i in range(0, 11):
		try:
		    food_consumption = consumption_rate[i] - (int(houses[i][9]) * 5)
		    c_consumption_rate.append(food_consumption)
		    refuse = gabbage[i] + (int(houses[i][9]) * 5)
		    c_gabbage.append(refuse)
		    
		    if food_consumption == 0:
		    	print(f"food has been exhaused in house {i + 1}")
		    elif refuse > 200:
		    	print(f"The trash bin is full in house {i + 1}")
		    	clear_refuse()
		    	print(f"The trash has been emptied in house {i + 1}")

		except: 
			food_consumption = consumption_rate[9] - (int(houses[9][10]) * 5)
			c_consumption_rate.append(food_consumption)
			refuse = gabbage[9] + (int(houses[9][10]) * 5)
			c_gabbage.append(refuse)
			if food_consumption == 0:
				print("food has been exhaused in house 10")
			# elif refuse > 200:
			# 	print("The trash bin is full in house 10")
			# 	clear_refuse()



	print(f"Current food supply: {c_consumption_rate[:10]}")
	print(f"Current refuse {c_gabbage[:10]}")

	consumption_rate = c_consumption_rate
	gabbage = c_gabbage

	for i in c_consumption_rate:
		if i == 0:
			c_consumption_rate.remove(i)
			restock()
	for i in c_gabbage:
		if i > 200:
			c_gabbage.remove(i)
			clear_refuse()

