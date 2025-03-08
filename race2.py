import random
import time 


noofracers = 4

racer1hp = random.randint(900, 2000)
print(racer1hp, 'hp')
racer1speed = 0.1*racer1hp
print(racer1speed, 'm/s')


racer2hp = random.randint(900, 2000)
print(racer2hp, 'hp')
racer2speed = 0.1*racer2hp
print(racer2speed, 'm/s')


racer3hp = random.randint(900, 2000)
print(racer3hp, 'hp')
racer3speed = 0.1*racer1hp
print(racer3speed, 'm/s')


racer4hp = random.randint(900, 2000)
print(racer4hp, 'hp')
racer4speed = 0.1*racer4hp
print(racer4speed, 'm/s')

print('racer1', racer1hp, 'hp')
time.sleep(2)
print('racer2', racer2hp, 'hp')
time.sleep(2)
print('racer3', racer3hp, 'hp')
time.sleep(2)
print('racer4', racer4hp, 'hp')
time.sleep(2)


racer1speed = 0.1*racer1hp
print(racer1speed, 'm/s')
racer1time_tocover_firstlane = 1000/racer1speed
print(racer1time_tocover_firstlane, 's')

racer2speed = 0.1*racer2hp
print(racer2speed, 'm/s')
racer2time_tocover_firstlane = 1000/racer2speed
print(racer2time_tocover_firstlane, 's')

racer3speed = 0.1*racer3hp
print(racer3speed, 'm/s')
racer3time_tocover_firstlane = 1000/racer3speed
print(racer3time_tocover_firstlane, 's')

racer4speed = 0.1*racer4hp
print(racer4speed, 'm/s')
racer4time_tocover_firstlane = 1000/racer4speed
print(racer4time_tocover_firstlane, 's')


print('it took racer one', racer1time_tocover_firstlane, 's', 'to cover first lane')
time.sleep(3)
print('it took racer two', racer2time_tocover_firstlane, 's', 'to cover first lane')
time.sleep(3)
print('it took racer three', racer3time_tocover_firstlane, 's', 'to cover first lane')
time.sleep(3)
print('it took racer four', racer4time_tocover_firstlane, 's', 'to cover first lane')
time.sleep(3)


racer1speed_redu1 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu1, 'm/s' '' 'speed reduction')
racer1speed_before_turning = racer1speed-racer1speed_redu1
print(racer1speed_before_turning, 'm/s')
racer1time_forbend1 = 200/racer1speed_before_turning
print(racer1time_forbend1, 's')

racer2speed_redu1 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu1, 'm/s' '' 'speed reduction')
racer2speed_before_turning = racer2speed-racer2speed_redu1
print(racer2speed_before_turning, 'm/s')
racer2time_forbend1 = 200/racer2speed_before_turning
print(racer2time_forbend1, 's')

racer3speed_redu1 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu1, 'm/s' '' 'speed reduction')
racer3speed_before_turning = racer3speed-racer3speed_redu1
print(racer3speed_before_turning, 'm/s')
racer3time_forbend1 = 200/racer3speed_before_turning
print(racer3time_forbend1, 's')

racer4speed_redu1 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu1, 'm/s' '' 'speed reduction')
racer4speed_before_turning = racer4speed-racer4speed_redu1
print(racer4speed_before_turning, 'm/s')
racer4time_forbend1 = 200/racer4speed_before_turning
print(racer4time_forbend1, 's')


racer1_acc1 = random.randint(1, 10)
time.sleep(1)
print(racer1_acc1, 'm/s' '' 'acceleration')
racer1time_tocover_secondlane = 1000/(racer1speed_before_turning+racer1_acc1)
print(racer1time_tocover_secondlane, 's')

racer2_acc1 = random.randint(1, 10)
time.sleep(1)
print(racer2_acc1, 'm/s' '' 'acceleration')
racer2time_tocover_secondlane = 1000/(racer2speed_before_turning+racer2_acc1)
print(racer2time_tocover_secondlane, 's')

racer3_acc1 = random.randint(1, 10)
time.sleep(1)
print(racer3_acc1, 'm/s' '' 'acceleration')
racer3time_tocover_secondlane = 1000/(racer3speed_before_turning+racer3_acc1)
print(racer3time_tocover_secondlane, 's')

racer4_acc1 = random.randint(1, 10)
time.sleep(1)
print(racer4_acc1, 'm/s' '' 'acceleration')
racer4time_tocover_secondlane = 1000/(racer4speed_before_turning+racer4_acc1)
print(racer4time_tocover_secondlane, 's')

print('it took racer one', racer1time_tocover_secondlane, 's', 'to cover second lane')
time.sleep(3)
print('it took racer two', racer2time_tocover_secondlane, 's', 'to cover second lane')
time.sleep(3)
print('it took racer three', racer3time_tocover_secondlane, 's', 'to cover second lane')
time.sleep(3)
print('it took racer four', racer4time_tocover_secondlane, 's', 'to cover second lane')
time.sleep(3)


racer1speed_redu2 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu2, 'm/s' '' 'speed reduction')
racer1speed_before_turning2 = (racer1speed_before_turning+racer1_acc1)-racer1speed_redu2
print(racer1speed_before_turning2, 'm/s')
racer1time_forbend2 = 200/racer1speed_before_turning2
print(racer1time_forbend2, 's')

racer2speed_redu2 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu2, 'm/s' '' 'speed reduction')
racer2speed_before_turning2 = (racer2speed_before_turning+racer2_acc1)-racer2speed_redu2
print(racer2speed_before_turning2, 'm/s')
racer2time_forbend2 = 200/racer2speed_before_turning2
print(racer2time_forbend2, 's')

racer3speed_redu2 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu2, 'm/s' '' 'speed reduction')
racer3speed_before_turning2 = (racer3speed_before_turning+racer3_acc1)-racer3speed_redu2
print(racer3speed_before_turning2, 'm/s')
racer3time_forbend2 = 200/racer3speed_before_turning2
print(racer3time_forbend2, 's')

racer4speed_redu2 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu2, 'm/s' '' 'speed reduction')
racer4speed_before_turning2 = (racer4speed_before_turning+racer4_acc1)-racer4speed_redu2
print(racer4speed_before_turning2, 'm/s')
racer4time_forbend2 = 200/racer4speed_before_turning2
print(racer4time_forbend2, 's')


racer1_acc2 = random.randint(1, 10)
time.sleep(1)
print(racer1_acc2, 'm/s' '' 'acceleration')
racer1time_tocover_thirdlane = 1000/(racer1speed_before_turning2+racer1_acc2)
print(racer1time_tocover_thirdlane, 's')

racer2_acc2 = random.randint(1, 10)
time.sleep(1)
print(racer2_acc2, 'm/s' '' 'acceleration')
racer2time_tocover_thirdlane = 1000/(racer2speed_before_turning2+racer2_acc2)
print(racer2time_tocover_thirdlane, 's')

racer3_acc2 = random.randint(1, 10)
time.sleep(1)
print(racer3_acc2, 'm/s' '' 'acceleration')
racer3time_tocover_thirdlane = 1000/(racer3speed_before_turning2+racer3_acc2)
print(racer3time_tocover_thirdlane, 's')

racer4_acc2 = random.randint(1, 10)
time.sleep(1)
print(racer4_acc2, 'm/s' '' 'acceleration')
racer4time_tocover_thirdlane = 1000/(racer4speed_before_turning2+racer4_acc2)
print(racer4time_tocover_thirdlane, 's')

print('it took racer one', racer1time_tocover_thirdlane, 's', 'to cover third lane')
time.sleep(3)
print('it took racer two', racer2time_tocover_thirdlane, 's', 'to cover third lane')
time.sleep(3)
print('it took racer three', racer3time_tocover_thirdlane, 's', 'to cover third lane')
time.sleep(3)
print('it took racer four', racer4time_tocover_thirdlane, 's', 'to cover third lane')
time.sleep(3)


racer1speed_redu3 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu3, 'm/s' '' 'speed reduction')
racer1speed_before_turning3 = (racer1speed_before_turning2+racer1_acc2)-racer1speed_redu3
print(racer1speed_before_turning3, 'm/s')
racer1time_forbend3 = 200/racer1speed_before_turning3
print(racer1time_forbend3, 's')

racer2speed_redu3 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu3, 'm/s' '' 'speed reduction')
racer2speed_before_turning3 = (racer2speed_before_turning2+racer2_acc2)-racer2speed_redu3
print(racer2speed_before_turning3, 'm/s')
racer2time_forbend3 = 200/racer2speed_before_turning3
print(racer2time_forbend3, 's')

racer3speed_redu3 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu3, 'm/s' '' 'speed reduction')
racer3speed_before_turning3 = (racer3speed_before_turning2+racer3_acc2)-racer3speed_redu3
print(racer3speed_before_turning3, 'm/s')
racer3time_forbend3 = 200/racer3speed_before_turning3
print(racer3time_forbend3, 's')

racer4speed_redu3 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu3, 'm/s' '' 'speed reduction')
racer4speed_before_turning3 = (racer4speed_before_turning2+racer4_acc2)-racer4speed_redu3
print(racer4speed_before_turning3, 'm/s')
racer4time_forbend3 = 200/racer4speed_before_turning3
print(racer4time_forbend3, 's')


racer1_acc3 = random.randint(1, 10)
time.sleep(1)
print(racer1_acc3, 'm/s' '' 'acceleration')
racer1time_tocover_fourthlane = 1000/(racer1speed_before_turning3+racer1_acc3)
print(racer1time_tocover_fourthlane, 's')

racer2_acc3 = random.randint(1, 10)
time.sleep(1)
print(racer2_acc3, 'm/s' '' 'acceleration')
racer2time_tocover_fourthlane = 1000/(racer2speed_before_turning3+racer2_acc3)
print(racer2time_tocover_fourthlane, 's')

racer3_acc3 = random.randint(1, 10)
time.sleep(1)
print(racer3_acc3, 'm/s' '' 'acceleration')
racer3time_tocover_fourthlane = 1000/(racer3speed_before_turning3+racer3_acc3)
print(racer3time_tocover_fourthlane, 's')

racer4_acc3 = random.randint(1, 10)
time.sleep(1)
print(racer4_acc3, 'm/s' '' 'acceleration')
racer4time_tocover_fourthlane = 1000/(racer4speed_before_turning3+racer4_acc3)
print(racer4time_tocover_fourthlane, 's')



print('it took racer one', racer1time_tocover_fourthlane, 's', 'to cover fourth lane')
time.sleep(3)
print('it took racer two', racer2time_tocover_fourthlane, 's', 'to cover fourth lane')
time.sleep(3)
print('it took racer three', racer3time_tocover_fourthlane, 's', 'to cover fourth lane')
time.sleep(3)
print('it took racer four', racer4time_tocover_fourthlane, 's', 'to cover fourth lane')
time.sleep(3)


racer1speed_redu4 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu4, 'speed reduction')
racer1speed_before_turning4 = (racer1speed_before_turning3+racer1_acc3)-racer1speed_redu4
print(racer1speed_before_turning4, 'm/s')
racer1time_forbend4 = 200/racer1speed_before_turning4
print(racer1time_forbend4, 's')

racer2speed_redu4 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu4, 'speed reduction')
racer2speed_before_turning4 = (racer2speed_before_turning3+racer2_acc3)-racer2speed_redu4
print(racer2speed_before_turning4, 'm/s')
racer2time_forbend4 = 200/racer2speed_before_turning4
print(racer2time_forbend4, 's')

racer3speed_redu4 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu4, 'speed reduction')
racer3speed_before_turning4 = (racer3speed_before_turning3+racer3_acc3)-racer3speed_redu4
print(racer3speed_before_turning4, 'm/s')
racer3time_forbend4 = 200/racer3speed_before_turning4
print(racer3time_forbend4, 's')

racer4speed_redu4 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu4, 'speed reduction')
racer4speed_before_turning4 = (racer4speed_before_turning3+racer4_acc3)-racer4speed_redu4
print(racer4speed_before_turning4, 'm/s')
racer4time_forbend4 = 200/racer4speed_before_turning4
print(racer4time_forbend4, 's')


racer1_firstlap_time = racer1time_tocover_firstlane+racer1time_forbend1+racer1time_tocover_secondlane+racer1time_forbend2+racer1time_tocover_thirdlane+racer1time_forbend3+racer1time_tocover_fourthlane+racer1time_forbend4
print(racer1_firstlap_time, 's', '1st lap time')

racer2_firstlap_time = racer2time_tocover_firstlane+racer2time_forbend1+racer2time_tocover_secondlane+racer2time_forbend2+racer2time_tocover_thirdlane+racer2time_forbend3+racer2time_tocover_fourthlane+racer2time_forbend4
print(racer2_firstlap_time, 's', '1st lap time')

racer3_firstlap_time = racer3time_tocover_firstlane+racer3time_forbend1+racer3time_tocover_secondlane+racer3time_forbend2+racer3time_tocover_thirdlane+racer3time_forbend3+racer3time_tocover_fourthlane+racer3time_forbend4
print(racer3_firstlap_time, 's', '1st lap time')

racer4_firstlap_time = racer4time_tocover_firstlane+racer4time_forbend1+racer4time_tocover_secondlane+racer4time_forbend2+racer4time_tocover_thirdlane+racer4time_forbend3+racer4time_tocover_fourthlane+racer4time_forbend4
print(racer4_firstlap_time, 's', '1st lap time')


print('it took racer one', racer1_firstlap_time, 's', 'to cover 1st lap')
time.sleep(4)
print('it took racer two', racer2_firstlap_time, 's', 'to cover 1st lap')
time.sleep(4)
print('it took racer three', racer3_firstlap_time, 's', 'to cover 1st lap')
time.sleep(4)
print('it took racer four', racer4_firstlap_time, 's', 'to cover 1st lap')
time.sleep(4)

a = [racer1_firstlap_time, racer2_firstlap_time, racer3_firstlap_time, racer4_firstlap_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
print(race_min)
time.sleep(2)
print(at[min_index], "is leading the race")


racer1_acclap2 = random.randint(1, 10)
time.sleep(1)
print(racer1_acclap2, 'm/s' '' 'acceleration')
racer1time_tocover_firstlanelap2 = 1000/(racer1speed_before_turning4+racer1_acclap2)
print(racer1speed_before_turning4+racer1_acclap2, 'speed for starting lap 2')
print(racer1time_tocover_firstlanelap2, 's')

racer2_acclap2 = random.randint(1, 10)
time.sleep(1)
print(racer2_acclap2, 'm/s' '' 'acceleration')
racer2time_tocover_firstlanelap2 = 1000/(racer2speed_before_turning4+racer2_acclap2)
print(racer2speed_before_turning4+racer2_acclap2, 'speed for starting lap 2')
print(racer2time_tocover_firstlanelap2, 's')

racer3_acclap2 = random.randint(1, 10)
time.sleep(1)
print(racer3_acclap2, 'm/s' '' 'acceleration')
racer3time_tocover_firstlanelap2 = 1000/(racer3speed_before_turning4+racer3_acclap2)
print(racer3speed_before_turning4+racer3_acclap2, 'speed for starting lap 2')
print(racer3time_tocover_firstlanelap2, 's')

racer4_acclap2 = random.randint(1, 10)
time.sleep(1)
print(racer4_acclap2, 'm/s' '' 'acceleration')
racer4time_tocover_firstlanelap2 = 1000/(racer4speed_before_turning4+racer4_acclap2)
print(racer4speed_before_turning4+racer4_acclap2, 'speed for starting lap 2')
print(racer4time_tocover_firstlanelap2, 's')


print('it took racer one', racer1time_tocover_firstlanelap2, 's', 'to cover ist lane lap 2')
time.sleep(3)
print('it took racer two', racer2time_tocover_firstlanelap2, 's', 'to cover ist lane lap 2')
time.sleep(3)
print('it took racer three', racer3time_tocover_firstlanelap2, 's', 'to cover ist lane lap 2')
time.sleep(3)
print('it took racer four', racer4time_tocover_firstlanelap2, 's', 'to cover ist lane lap 2')
time.sleep(3)


racer1speed_redu1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu1lap2, 'm/s' '' 'speed reduction')
racer1speed_before_turninglap2 = (racer1speed_before_turning4+racer1_acclap2)-racer1speed_redu1lap2
print(racer1speed_before_turninglap2, 'm/s')
racer1time_forbend1lap2 = 200/racer1speed_before_turninglap2
print(racer1time_forbend1lap2, 's')

racer2speed_redu1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu1lap2, 'm/s' '' 'speed reduction')
racer2speed_before_turninglap2 = (racer2speed_before_turning4+racer2_acclap2)-racer2speed_redu1lap2
print(racer2speed_before_turninglap2, 'm/s')
racer2time_forbend1lap2 = 200/racer2speed_before_turninglap2
print(racer2time_forbend1lap2, 's')

racer3speed_redu1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu1lap2, 'm/s' '' 'speed reduction')
racer3speed_before_turninglap2 = (racer3speed_before_turning4+racer3_acclap2)-racer3speed_redu1lap2
print(racer3speed_before_turninglap2, 'm/s')
racer3time_forbend1lap2 = 200/racer3speed_before_turninglap2
print(racer3time_forbend1lap2, 's')

racer4speed_redu1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu1lap2, 'm/s' '' 'speed reduction')
racer4speed_before_turninglap2 = (racer4speed_before_turning4+racer4_acclap2)-racer4speed_redu1lap2
print(racer4speed_before_turninglap2, 'm/s')
racer4time_forbend1lap2 = 200/racer4speed_before_turninglap2
print(racer4time_forbend1lap2, 's')


racer1_acc1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1_acc1lap2, 'm/s' '' 'acceleration')
racer1time_tocover_secondlanelap2 = 1000/(racer1speed_before_turninglap2+racer1_acc1lap2)
print(racer1time_tocover_secondlanelap2, 's')

racer2_acc1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2_acc1lap2, 'm/s' '' 'acceleration')
racer2time_tocover_secondlanelap2 = 1000/(racer2speed_before_turninglap2+racer2_acc1lap2)
print(racer2time_tocover_secondlanelap2, 's')

racer3_acc1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3_acc1lap2, 'm/s' '' 'acceleration')
racer3time_tocover_secondlanelap2 = 1000/(racer3speed_before_turninglap2+racer3_acc1lap2)
print(racer3time_tocover_secondlanelap2, 's')

racer4_acc1lap2 = random.randint(1, 10)
time.sleep(1)
print(racer4_acc1lap2, 'm/s' '' 'acceleration')
racer4time_tocover_secondlanelap2 = 1000/(racer4speed_before_turninglap2+racer4_acc1lap2)
print(racer4time_tocover_secondlanelap2, 's')

print('it took racer one', racer1time_tocover_secondlanelap2, 's', 'to cover 2nd lane lap 2')
time.sleep(3)
print('it took racer two', racer2time_tocover_secondlanelap2, 's', 'to cover 2nd lane lap 2')
time.sleep(3)
print('it took racer three', racer3time_tocover_secondlanelap2, 's', 'to cover 2nd lane lap 2')
time.sleep(3)
print('it took racer four', racer4time_tocover_secondlanelap2, 's', 'to cover 2nd lane lap 2')
time.sleep(3)


racer1speed_redu2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu2lap2, 'm/s' '' 'deceleration')
racer1speed_before_turning2lap2 = (racer1speed_before_turninglap2+racer1_acc1lap2)-racer1speed_redu2lap2
print(racer1speed_before_turning2lap2, 'm/s')
racer1time_forbend2lap2 = 200/racer1speed_before_turning2lap2
print(racer1time_forbend2lap2, 's')

racer2speed_redu2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu2lap2, 'm/s' '' 'deceleration')
racer2speed_before_turning2lap2 = (racer2speed_before_turninglap2+racer2_acc1lap2)-racer2speed_redu2lap2
print(racer2speed_before_turning2lap2, 'm/s')
racer2time_forbend2lap2 = 200/racer2speed_before_turning2lap2
print(racer2time_forbend2lap2, 's')

racer3speed_redu2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu2lap2, 'm/s' '' 'deceleration')
racer3speed_before_turning2lap2 = (racer3speed_before_turninglap2+racer3_acc1lap2)-racer3speed_redu2lap2
print(racer3speed_before_turning2lap2, 'm/s')
racer3time_forbend2lap2 = 200/racer3speed_before_turning2lap2
print(racer3time_forbend2lap2, 's')

racer4speed_redu2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu2lap2, 'm/s' '' 'deceleration')
racer4speed_before_turning2lap2 = (racer4speed_before_turninglap2+racer4_acc1lap2)-racer4speed_redu2lap2
print(racer4speed_before_turning2lap2, 'm/s')
racer4time_forbend2lap2 = 200/racer4speed_before_turning2lap2
print(racer4time_forbend2lap2, 's')


racer1_acc2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1_acc2lap2, 'm/s' '' 'acceleration')
racer1time_tocover_thirdlanelap2 = 1000/(racer1speed_before_turning2lap2+racer1_acc2lap2)
print(racer1time_tocover_thirdlanelap2, 's')

racer2_acc2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2_acc2lap2, 'm/s' '' 'acceleration')
racer2time_tocover_thirdlanelap2 = 1000/(racer2speed_before_turning2lap2+racer2_acc2lap2)
print(racer2time_tocover_thirdlanelap2, 's')

racer3_acc2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3_acc2lap2, 'm/s' '' 'acceleration')
racer3time_tocover_thirdlanelap2 = 1000/(racer3speed_before_turning2lap2+racer3_acc2lap2)
print(racer3time_tocover_thirdlanelap2, 's')

racer4_acc2lap2 = random.randint(1, 10)
time.sleep(1)
print(racer4_acc2lap2, 'm/s' '' 'acceleration')
racer4time_tocover_thirdlanelap2 = 1000/(racer4speed_before_turning2lap2+racer4_acc2lap2)
print(racer4time_tocover_thirdlanelap2, 's')

print('it took racer one', racer1time_tocover_thirdlanelap2, 's', 'to cover 3rd lane lap 2')
time.sleep(3)
print('it took racer two', racer2time_tocover_thirdlanelap2, 's', 'to cover 3rd lane lap 2')
time.sleep(3)
print('it took racer three', racer3time_tocover_thirdlanelap2, 's', 'to cover 3rd lane lap 2')
time.sleep(3)
print('it took racer four', racer4time_tocover_thirdlanelap2, 's', 'to cover 3rd lane lap 2')
time.sleep(3)


racer1speed_redu3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu3lap2, 'm/s' '' 'deceleration')
racer1speed_before_turning3lap2 = (racer1speed_before_turning2lap2+racer1_acc2lap2)-racer1speed_redu3lap2
print(racer1speed_before_turning3lap2, 'm/s')
racer1time_forbend3lap2 = 200/racer1speed_before_turning3lap2
print(racer1time_forbend3lap2, 's')

racer2speed_redu3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu3lap2, 'm/s' '' 'deceleration')
racer2speed_before_turning3lap2 = (racer2speed_before_turning2lap2+racer2_acc2lap2)-racer2speed_redu3lap2
print(racer2speed_before_turning3lap2, 'm/s')
racer2time_forbend3lap2 = 200/racer2speed_before_turning3lap2
print(racer2time_forbend3lap2, 's')

racer3speed_redu3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu3lap2, 'm/s' '' 'deceleration')
racer3speed_before_turning3lap2 = (racer3speed_before_turning2lap2+racer3_acc2lap2)-racer3speed_redu3lap2
print(racer3speed_before_turning3lap2, 'm/s')
racer3time_forbend3lap2 = 200/racer3speed_before_turning3lap2
print(racer3time_forbend3lap2, 's')

racer4speed_redu3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu3lap2, 'm/s' '' 'deceleration')
racer4speed_before_turning3lap2 = (racer4speed_before_turning2lap2+racer4_acc2lap2)-racer4speed_redu3lap2
print(racer4speed_before_turning3lap2, 'm/s')
racer4time_forbend3lap2 = 200/racer4speed_before_turning3lap2
print(racer4time_forbend3lap2, 's')


racer1_acc3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1_acc3lap2, 'm/s' '' 'acceleration')
racer1time_tocover_fourthlanelap2 = 1000/(racer1speed_before_turning3lap2+racer1_acc3lap2)
print(racer1time_tocover_fourthlanelap2, 's')

racer2_acc3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2_acc3lap2, 'm/s' '' 'acceleration')
racer2time_tocover_fourthlanelap2 = 1000/(racer2speed_before_turning3lap2+racer2_acc3lap2)
print(racer2time_tocover_fourthlanelap2, 's')

racer3_acc3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3_acc3lap2, 'm/s' '' 'acceleration')
racer3time_tocover_fourthlanelap2 = 1000/(racer3speed_before_turning3lap2+racer3_acc3lap2)
print(racer3time_tocover_fourthlanelap2, 's')

racer4_acc3lap2 = random.randint(1, 10)
time.sleep(1)
print(racer4_acc3lap2, 'm/s' '' 'acceleration')
racer4time_tocover_fourthlanelap2 = 1000/(racer4speed_before_turning3lap2+racer4_acc3lap2)
print(racer4time_tocover_fourthlanelap2, 's')


racer1speed_redu4lap2 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu4lap2, 'm/s' '' 'deceleration')
racer1speed_before_turning4lap2 = (racer1speed_before_turning3lap2+racer1_acc3lap2)-racer1speed_redu4lap2
print(racer1speed_before_turning4lap2, 'm/s')
racer1time_forbend4lap2 = 200/racer1speed_before_turning4lap2
print(racer1time_forbend4lap2, 's')

racer2speed_redu4lap2 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu4lap2, 'm/s' '' 'deceleration')
racer2speed_before_turning4lap2 = (racer2speed_before_turning3lap2+racer2_acc3lap2)-racer2speed_redu4lap2
print(racer2speed_before_turning4lap2, 'm/s')
racer2time_forbend4lap2 = 200/racer2speed_before_turning4lap2
print(racer2time_forbend4lap2, 's')

racer3speed_redu4lap2 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu4lap2, 'm/s' '' 'deceleration')
racer3speed_before_turning4lap2 = (racer3speed_before_turning3lap2+racer3_acc3lap2)-racer3speed_redu4lap2
print(racer3speed_before_turning4lap2, 'm/s')
racer3time_forbend4lap2 = 200/racer3speed_before_turning4lap2
print(racer3time_forbend4lap2, 's')

racer4speed_redu4lap2 = random.randint(1, 10)
print(racer4speed_redu4lap2, 'deceleration')
racer4speed_before_turning4lap2 = (racer4speed_before_turning3lap2+racer4_acc3lap2)-racer1speed_redu4lap2
print(racer4speed_before_turning4lap2, 'm/s')
racer4time_forbend4lap2 = 200/racer4speed_before_turning4lap2
print(racer4time_forbend4lap2, 's')


racer1_secondlap_time = racer1time_tocover_firstlanelap2+racer1time_forbend1lap2+racer1time_tocover_secondlanelap2+racer1time_forbend2lap2+racer1time_tocover_thirdlanelap2+racer1time_forbend3lap2+racer1time_tocover_fourthlanelap2+racer1time_forbend4lap2
print(racer1_secondlap_time, 's', '2nd lap time')
racer2_secondlap_time = racer2time_tocover_firstlanelap2+racer2time_forbend1lap2+racer2time_tocover_secondlanelap2+racer2time_forbend2lap2+racer2time_tocover_thirdlanelap2+racer2time_forbend3lap2+racer2time_tocover_fourthlanelap2+racer2time_forbend4lap2
print(racer2_secondlap_time, 's', '2nd lap time')
racer3_secondlap_time = racer3time_tocover_firstlanelap2+racer3time_forbend1lap2+racer3time_tocover_secondlanelap2+racer3time_forbend2lap2+racer3time_tocover_thirdlanelap2+racer3time_forbend3lap2+racer3time_tocover_fourthlanelap2+racer3time_forbend4lap2
print(racer3_secondlap_time, 's', '2nd lap time')
racer4_secondlap_time = racer4time_tocover_firstlanelap2+racer4time_forbend1lap2+racer4time_tocover_secondlanelap2+racer4time_forbend2lap2+racer4time_tocover_thirdlanelap2+racer4time_forbend3lap2+racer4time_tocover_fourthlanelap2+racer4time_forbend4lap2
print(racer4_secondlap_time, 's', '2nd lap time')

print('it took racer one', racer1_secondlap_time, 's', 'to cover 2nd lap')
time.sleep(3)
print('it took racer two', racer2_secondlap_time, 's', 'to cover 2nd lap')
time.sleep(3)
print('it took racer three', racer3_secondlap_time, 's', 'to cover 2nd lap')
time.sleep(3)
print('it took racer four', racer4_secondlap_time, 's', 'to cover 2nd lap')
time.sleep(3)


a = [racer1_secondlap_time, racer2_secondlap_time, racer3_secondlap_time, racer4_secondlap_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
print(race_min)
time.sleep(2)
print(at[min_index], "had the shortest second lap time")

current_racer1_time = racer1_firstlap_time + racer1_secondlap_time
current_racer2_time = racer2_firstlap_time + racer2_secondlap_time
current_racer3_time = racer3_firstlap_time + racer3_secondlap_time
current_racer4_time = racer4_firstlap_time + racer4_secondlap_time

a = [current_racer1_time, current_racer2_time, current_racer3_time, current_racer4_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
time.sleep(2)
print(race_min)
time.sleep(2)
print(at[min_index], "is currently leading the race")



racer1_acclap3 = random.randint(1, 10)
time.sleep(1)
print(racer1_acclap3, 'm/s' '' 'acceleration')
racer1time_tocover_firstlanelap3 = 1000/(racer1speed_before_turning4+racer1_acclap3)
print(racer1speed_before_turning4+racer1_acclap3, 'speed for starting lap 3')
print(racer1time_tocover_firstlanelap3, 's')

racer2_acclap3 = random.randint(1, 10)
time.sleep(1)
print(racer2_acclap3, 'm/s' '' 'acceleration')
racer2time_tocover_firstlanelap3 = 1000/(racer2speed_before_turning4+racer2_acclap3)
print(racer2speed_before_turning4+racer2_acclap3, 'speed for starting lap 3')
print(racer2time_tocover_firstlanelap3, 's')

racer3_acclap3 = random.randint(1, 10)
time.sleep(1)
print(racer3_acclap3, 'm/s' '' 'acceleration')
racer3time_tocover_firstlanelap3 = 1000/(racer3speed_before_turning4+racer3_acclap3)
print(racer3speed_before_turning4+racer3_acclap3, 'speed for starting lap 3')
print(racer3time_tocover_firstlanelap3, 's')

racer4_acclap3 = random.randint(1, 10)
time.sleep(1)
print(racer4_acclap3, 'm/s' '' 'acceleration')
racer4time_tocover_firstlanelap3 = 1000/(racer4speed_before_turning4+racer4_acclap3)
print(racer4speed_before_turning4+racer4_acclap3, 'speed for starting lap 3')
print(racer4time_tocover_firstlanelap3, 's')


print('it took racer one', racer1time_tocover_firstlanelap3, 's', 'to cover ist lane lap 3')
time.sleep(3)
print('it took racer two', racer2time_tocover_firstlanelap3, 's', 'to cover ist lane lap 3')
time.sleep(3)
print('it took racer three', racer3time_tocover_firstlanelap3, 's', 'to cover ist lane lap 3')
time.sleep(3)
print('it took racer four', racer4time_tocover_firstlanelap3, 's', 'to cover ist lane lap 3')
time.sleep(3)


racer1speed_redu1lap3 = random.randint(1, 10)
time.sleep(1)
print(racer1speed_redu1lap3, 'm/s' '' 'deceleration')
racer1speed_before_turninglap3 = (racer1speed_before_turning4+racer1_acclap3)-racer1speed_redu1lap3
print(racer1speed_before_turninglap3, 'm/s')
racer1time_forbend1lap3 = 200/racer1speed_before_turninglap3
print(racer1time_forbend1lap3, 's')

racer2speed_redu1lap3 = random.randint(1, 10)
time.sleep(1)
print(racer2speed_redu1lap3, 'm/s' '' 'deceleration')
racer2speed_before_turninglap3 = (racer2speed_before_turning4+racer2_acclap3)-racer2speed_redu1lap3
print(racer2speed_before_turninglap3, 'm/s')
racer2time_forbend1lap3 = 200/racer2speed_before_turninglap3
print(racer2time_forbend1lap3, 's')

racer3speed_redu1lap3 = random.randint(1, 10)
time.sleep(1)
print(racer3speed_redu1lap3, 'm/s' '' 'deceleration')
racer3speed_before_turninglap3 = (racer3speed_before_turning4+racer3_acclap3)-racer3speed_redu1lap3
print(racer3speed_before_turninglap3, 'm/s')
racer3time_forbend1lap3 = 200/racer3speed_before_turninglap3
print(racer3time_forbend1lap3, 's')

racer4speed_redu1lap3 = random.randint(1, 10)
time.sleep(1)
print(racer4speed_redu1lap3, 'm/s' '' 'deceleration')
racer4speed_before_turninglap3 = (racer4speed_before_turning4+racer4_acclap3)-racer4speed_redu1lap3
print(racer4speed_before_turninglap3, 'm/s')
racer4time_forbend1lap3 = 200/racer4speed_before_turninglap3
print(racer4time_forbend1lap3, 's')


racer1_acc1lap3 = random.randint(1, 10)
print(racer1_acc1lap3, 'acceleration')
racer1time_tocover_secondlanelap3 = 1000/(racer1speed_before_turninglap3+racer1_acc1lap3)
print(racer1time_tocover_secondlanelap3, 's')

racer2_acc1lap3 = random.randint(1, 10)
print(racer2_acc1lap3, 'acceleration')
racer2time_tocover_secondlanelap3 = 1000/(racer2speed_before_turninglap3+racer2_acc1lap3)
print(racer2time_tocover_secondlanelap3, 's')

racer3_acc1lap3 = random.randint(1, 10)
print(racer3_acc1lap3, 'acceleration')
racer3time_tocover_secondlanelap3 = 1000/(racer3speed_before_turninglap3+racer3_acc1lap3)
print(racer3time_tocover_secondlanelap3, 's')

racer4_acc1lap3 = random.randint(1, 10)
print(racer4_acc1lap3, 'acceleration')
racer4time_tocover_secondlanelap3 = 1000/(racer4speed_before_turninglap3+racer4_acc1lap3)
print(racer4time_tocover_secondlanelap3, 's')

print('it took racer one', racer1time_tocover_secondlanelap3, 's', 'to cover 2nd lane lap 3')
time.sleep(3)
print('it took racer two', racer2time_tocover_secondlanelap3, 's', 'to cover 2nd lane lap 3')
time.sleep(3)
print('it took racer three', racer3time_tocover_secondlanelap3, 's', 'to cover 2nd lane lap 3')
time.sleep(3)
print('it took racer four', racer4time_tocover_secondlanelap3, 's', 'to cover 2nd lane lap 3')
time.sleep(3)


racer1speed_redu2lap3 = random.randint(1, 10)
print(racer1speed_redu2lap3, 'deceleration')
racer1speed_before_turning2lap3 = (racer1speed_before_turninglap3+racer1_acc1lap3)-racer1speed_redu2lap3
print(racer1speed_before_turning2lap3, 'm/s')
racer1time_forbend2lap3 = 200/racer1speed_before_turning2lap3
print(racer1time_forbend2lap3, 's')

racer2speed_redu2lap3 = random.randint(1, 10)
print(racer2speed_redu2lap3, 'deceleration')
racer2speed_before_turning2lap3 = (racer2speed_before_turninglap3+racer2_acc1lap3)-racer2speed_redu2lap3
print(racer2speed_before_turning2lap3, 'm/s')
racer2time_forbend2lap3 = 200/racer2speed_before_turning2lap3
print(racer2time_forbend2lap3, 's')

racer3speed_redu2lap3 = random.randint(1, 10)
print(racer3speed_redu2lap3, 'deceleration')
racer3speed_before_turning2lap3 = (racer3speed_before_turninglap3+racer3_acc1lap3)-racer3speed_redu2lap3
print(racer3speed_before_turning2lap3, 'm/s')
racer3time_forbend2lap3 = 200/racer3speed_before_turning2lap3
print(racer3time_forbend2lap3, 's')

racer4speed_redu2lap3 = random.randint(1, 10)
print(racer4speed_redu2lap3, 'deceleration')
racer4speed_before_turning2lap3 = (racer4speed_before_turninglap3+racer4_acc1lap3)-racer4speed_redu2lap3
print(racer4speed_before_turning2lap3, 'm/s')
racer4time_forbend2lap3 = 200/racer4speed_before_turning2lap3
print(racer4time_forbend2lap3, 's')


racer1_acc2lap3 = random.randint(1, 10)
print(racer1_acc2lap3, 'acceleration')
racer1time_tocover_thirdlanelap3 = 1000/(racer1speed_before_turning2lap3+racer1_acc2lap3)
print(racer1time_tocover_thirdlanelap3, 's')

racer2_acc2lap3 = random.randint(1, 10)
print(racer2_acc2lap3, 'acceleration')
racer2time_tocover_thirdlanelap3 = 1000/(racer2speed_before_turning2lap3+racer2_acc2lap3)
print(racer2time_tocover_thirdlanelap3, 's')

racer3_acc2lap3 = random.randint(1, 10)
print(racer3_acc2lap3, 'acceleration')
racer3time_tocover_thirdlanelap3 = 1000/(racer3speed_before_turning2lap3+racer3_acc2lap3)
print(racer3time_tocover_thirdlanelap3, 's')

racer4_acc2lap3 = random.randint(1, 10)
print(racer4_acc2lap3, 'acceleration')
racer4time_tocover_thirdlanelap3 = 1000/(racer4speed_before_turning2lap3+racer4_acc2lap3)
print(racer4time_tocover_thirdlanelap3, 's')

print('it took racer one', racer1time_tocover_thirdlanelap3, 's', 'to cover 3rd lane lap 3')
time.sleep(3)
print('it took racer two', racer2time_tocover_thirdlanelap3, 's', 'to cover 3rd lane lap 3')
time.sleep(3)
print('it took racer three', racer3time_tocover_thirdlanelap3, 's', 'to cover 3rd lane lap 3')
time.sleep(3)
print('it took racer four', racer4time_tocover_thirdlanelap3, 's', 'to cover 3rd lane lap 3')
time.sleep(3)


racer1speed_redu3lap3 = random.randint(1, 10)
racer1speed_before_turning3lap3 = (racer1speed_before_turning2lap3+racer1_acc2lap3)-racer1speed_redu3lap3
print(racer1speed_before_turning3lap3, 'm/s')
racer1time_forbend3lap3 = 200/racer1speed_before_turning3lap3
print(racer1time_forbend3lap3, 's')

racer2speed_redu3lap3 = random.randint(1, 10)
racer2speed_before_turning3lap3 = (racer2speed_before_turning2lap3+racer2_acc2lap3)-racer2speed_redu3lap3
print(racer2speed_before_turning3lap3, 'm/s')
racer2time_forbend3lap3 = 200/racer2speed_before_turning3lap3
print(racer2time_forbend3lap3, 's')

racer3speed_redu3lap3 = random.randint(1, 10)
racer3speed_before_turning3lap3 = (racer3speed_before_turning2lap3+racer3_acc2lap3)-racer3speed_redu3lap3
print(racer3speed_before_turning3lap3, 'm/s')
racer3time_forbend3lap3 = 200/racer3speed_before_turning3lap3
print(racer3time_forbend3lap3, 's')

racer4speed_redu3lap3 = random.randint(1, 10)
racer4speed_before_turning3lap3 = (racer4speed_before_turning2lap3+racer4_acc2lap3)-racer4speed_redu3lap3
print(racer4speed_before_turning3lap3, 'm/s')
racer4time_forbend3lap3 = 200/racer4speed_before_turning3lap3
print(racer4time_forbend3lap3, 's')


racer1_acc3lap3 = random.randint(1, 10)
racer1time_tocover_fourthlanelap3 = 1000/(racer1speed_before_turning3lap3+racer1_acc3lap3)
print(racer1time_tocover_fourthlanelap3, 's')

racer2_acc3lap3 = random.randint(1, 10)
racer2time_tocover_fourthlanelap3 = 1000/(racer2speed_before_turning3lap3+racer2_acc3lap3)
print(racer2time_tocover_fourthlanelap3, 's')

racer3_acc3lap3 = random.randint(1, 10)
racer3time_tocover_fourthlanelap3 = 1000/(racer3speed_before_turning3lap3+racer3_acc3lap3)
print(racer3time_tocover_fourthlanelap3, 's')

racer4_acc3lap3 = random.randint(1, 10)
racer4time_tocover_fourthlanelap3 = 1000/(racer4speed_before_turning3lap3+racer4_acc3lap3)
print(racer4time_tocover_fourthlanelap3, 's')


racer1speed_redu4lap3 = random.randint(1, 10)
racer1speed_before_turning4lap3 = (racer1speed_before_turning3lap3+racer1_acc3lap3)-racer1speed_redu4lap3
print(racer1speed_before_turning4lap3, 'm/s')
racer1time_forbend4lap3 = 200/racer1speed_before_turning4lap3
print(racer1time_forbend4lap3, 's')

racer2speed_redu4lap3 = random.randint(1, 10)
racer2speed_before_turning4lap3 = (racer2speed_before_turning3lap3+racer2_acc3lap3)-racer2speed_redu4lap3
print(racer2speed_before_turning4lap3, 'm/s')
racer2time_forbend4lap3 = 200/racer2speed_before_turning4lap3
print(racer2time_forbend4lap3, 's')

racer3speed_redu4lap3 = random.randint(1, 10)
racer3speed_before_turning4lap3 = (racer3speed_before_turning3lap3+racer3_acc3lap3)-racer3speed_redu4lap3
print(racer3speed_before_turning4lap3, 'm/s')
racer3time_forbend4lap3 = 200/racer3speed_before_turning4lap3
print(racer3time_forbend4lap3, 's')

racer4speed_redu4lap3 = random.randint(1, 10)
racer4speed_before_turning4lap3 = (racer4speed_before_turning3lap3+racer4_acc3lap3)-racer1speed_redu4lap3
print(racer4speed_before_turning4lap3, 'm/s')
racer4time_forbend4lap3 = 200/racer4speed_before_turning4lap3
print(racer4time_forbend4lap3, 's')


racer1_thirdlap_time = racer1time_tocover_firstlanelap3+racer1time_forbend1lap3+racer1time_tocover_secondlanelap3+racer1time_forbend2lap3+racer1time_tocover_thirdlanelap3+racer1time_forbend3lap3+racer1time_tocover_fourthlanelap3+racer1time_forbend4lap3
print(racer1_thirdlap_time, 's', '3rdd lap time')
racer2_thirdlap_time = racer2time_tocover_firstlanelap3+racer2time_forbend1lap3+racer2time_tocover_secondlanelap3+racer2time_forbend2lap3+racer2time_tocover_thirdlanelap3+racer2time_forbend3lap3+racer2time_tocover_fourthlanelap3+racer2time_forbend4lap3
print(racer2_thirdlap_time, 's', '3rd lap time')
racer3_thirdlap_time = racer3time_tocover_firstlanelap3+racer3time_forbend1lap3+racer3time_tocover_secondlanelap3+racer3time_forbend2lap3+racer3time_tocover_thirdlanelap3+racer3time_forbend3lap3+racer3time_tocover_fourthlanelap3+racer3time_forbend4lap3
print(racer3_thirdlap_time, 's', '3rdd lap time')
racer4_thirdlap_time = racer4time_tocover_firstlanelap3+racer4time_forbend1lap3+racer4time_tocover_secondlanelap3+racer4time_forbend2lap3+racer4time_tocover_thirdlanelap3+racer4time_forbend3lap3+racer4time_tocover_fourthlanelap3+racer4time_forbend4lap3
print(racer4_thirdlap_time, 's', '3rd lap time')

print('it took racer one', racer1_thirdlap_time, 's', 'to cover 3rd lap')
time.sleep(3)
print('it took racer two', racer2_thirdlap_time, 's', 'to cover 3rd lap')
time.sleep(3)
print('it took racer three', racer3_thirdlap_time, 's', 'to cover 3rd lap')
time.sleep(3)
print('it took racer four', racer4_thirdlap_time, 's', 'to cover 3rd lap')
time.sleep(3)


a = [racer1_thirdlap_time, racer2_thirdlap_time, racer3_thirdlap_time, racer4_thirdlap_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
print(race_min)
time.sleep(2)
print(at[min_index], "had the shortest third lap time")

current_racer1_time = racer1_firstlap_time + racer1_secondlap_time + racer1_thirdlap_time
current_racer2_time = racer2_firstlap_time + racer2_secondlap_time + racer2_thirdlap_time
current_racer3_time = racer3_firstlap_time + racer3_secondlap_time + racer3_thirdlap_time
current_racer4_time = racer4_firstlap_time + racer4_secondlap_time + racer4_thirdlap_time

a = [current_racer1_time, current_racer2_time, current_racer3_time, current_racer4_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
time.sleep(2)
print(race_min)
time.sleep(2)
print(at[min_index], "is currently leading the race")




racer1_acclap4 = random.randint(1, 10)
print(racer1_acclap4)
racer1time_tocover_firstlanelap4 = 1000/(racer1speed_before_turning4+racer1_acclap4)
print(racer1speed_before_turning4+racer1_acclap4, 'speed for starting lap 4')
print(racer1time_tocover_firstlanelap4, 's')

racer2_acclap4 = random.randint(1, 10)
print(racer2_acclap4)
racer2time_tocover_firstlanelap4 = 1000/(racer2speed_before_turning4+racer2_acclap4)
print(racer2speed_before_turning4+racer2_acclap4, 'speed for starting lap 4')
print(racer2time_tocover_firstlanelap4, 's')

racer3_acclap4 = random.randint(1, 10)
print(racer3_acclap4)
racer3time_tocover_firstlanelap4 = 1000/(racer3speed_before_turning4+racer3_acclap4)
print(racer3speed_before_turning4+racer3_acclap4, 'speed for starting lap 4')
print(racer3time_tocover_firstlanelap4, 's')

racer4_acclap4 = random.randint(1, 10)
print(racer4_acclap4)
racer4time_tocover_firstlanelap4 = 1000/(racer4speed_before_turning4+racer4_acclap4)
print(racer4speed_before_turning4+racer4_acclap4, 'speed for starting lap 4')
print(racer4time_tocover_firstlanelap4, 's')


print('it took racer one', racer1time_tocover_firstlanelap4, 's', 'to cover ist lane lap 4')
time.sleep(3)
print('it took racer two', racer2time_tocover_firstlanelap4, 's', 'to cover ist lane lap 4')
time.sleep(3)
print('it took racer three', racer3time_tocover_firstlanelap4, 's', 'to cover ist lane lap 4')
time.sleep(3)
print('it took racer four', racer4time_tocover_firstlanelap4, 's', 'to cover ist lane lap 4')
time.sleep(3)


racer1speed_redu1lap4 = random.randint(1, 10)
racer1speed_before_turninglap4 = (racer1speed_before_turning4+racer1_acclap4)-racer1speed_redu1lap4
print(racer1speed_before_turninglap4, 'm/s')
racer1time_forbend1lap4 = 200/racer1speed_before_turninglap4
print(racer1time_forbend1lap4, 's')

racer2speed_redu1lap4 = random.randint(1, 10)
racer2speed_before_turninglap4 = (racer2speed_before_turning4+racer2_acclap4)-racer2speed_redu1lap4
print(racer2speed_before_turninglap4, 'm/s')
racer2time_forbend1lap4 = 200/racer2speed_before_turninglap4
print(racer2time_forbend1lap4, 's')

racer3speed_redu1lap4 = random.randint(1, 10)
racer3speed_before_turninglap4 = (racer3speed_before_turning4+racer3_acclap4)-racer3speed_redu1lap4
print(racer3speed_before_turninglap4, 'm/s')
racer3time_forbend1lap4 = 200/racer3speed_before_turninglap4
print(racer3time_forbend1lap4, 's')

racer4speed_redu1lap4 = random.randint(1, 10)
racer4speed_before_turninglap4 = (racer4speed_before_turning4+racer4_acclap4)-racer4speed_redu1lap4
print(racer4speed_before_turninglap4, 'm/s')
racer4time_forbend1lap4 = 200/racer4speed_before_turninglap4
print(racer4time_forbend1lap4, 's')


racer1_acc1lap4 = random.randint(1, 10)
racer1time_tocover_secondlanelap4 = 1000/(racer1speed_before_turninglap4+racer1_acc1lap4)
print(racer1time_tocover_secondlanelap4, 's')

racer2_acc1lap4 = random.randint(1, 10)
racer2time_tocover_secondlanelap4 = 1000/(racer2speed_before_turninglap4+racer2_acc1lap4)
print(racer2time_tocover_secondlanelap4, 's')

racer3_acc1lap4 = random.randint(1, 10)
racer3time_tocover_secondlanelap4 = 1000/(racer3speed_before_turninglap4+racer3_acc1lap4)
print(racer3time_tocover_secondlanelap4, 's')

racer4_acc1lap4 = random.randint(1, 10)
racer4time_tocover_secondlanelap4 = 1000/(racer4speed_before_turninglap4+racer4_acc1lap4)
print(racer4time_tocover_secondlanelap4, 's')

print('it took racer one', racer1time_tocover_secondlanelap4, 's', 'to cover 2nd lane lap 4')
time.sleep(3)
print('it took racer two', racer2time_tocover_secondlanelap4, 's', 'to cover 2nd lane lap 4')
time.sleep(3)
print('it took racer three', racer3time_tocover_secondlanelap4, 's', 'to cover 2nd lane lap 4')
time.sleep(3)
print('it took racer four', racer4time_tocover_secondlanelap4, 's', 'to cover 2nd lane lap 4')
time.sleep(3)


racer1speed_redu2lap4 = random.randint(1, 10)
racer1speed_before_turning2lap4 = (racer1speed_before_turninglap4+racer1_acc1lap4)-racer1speed_redu2lap4
print(racer1speed_before_turning2lap4, 'm/s')
racer1time_forbend2lap4 = 200/racer1speed_before_turning2lap4
print(racer1time_forbend2lap4, 's')

racer2speed_redu2lap4 = random.randint(1, 10)
racer2speed_before_turning2lap4 = (racer2speed_before_turninglap4+racer2_acc1lap4)-racer2speed_redu2lap4
print(racer2speed_before_turning2lap4, 'm/s')
racer2time_forbend2lap4 = 200/racer2speed_before_turning2lap4
print(racer2time_forbend2lap4, 's')

racer3speed_redu2lap4 = random.randint(1, 10)
racer3speed_before_turning2lap4 = (racer3speed_before_turninglap4+racer3_acc1lap4)-racer3speed_redu2lap4
print(racer3speed_before_turning2lap4, 'm/s')
racer3time_forbend2lap4 = 200/racer3speed_before_turning2lap4
print(racer3time_forbend2lap4, 's')

racer4speed_redu2lap4 = random.randint(1, 10)
racer4speed_before_turning2lap4 = (racer4speed_before_turninglap4+racer4_acc1lap4)-racer4speed_redu2lap4
print(racer4speed_before_turning2lap4, 'm/s')
racer4time_forbend2lap4 = 200/racer4speed_before_turning2lap4
print(racer4time_forbend2lap4, 's')


racer1_acc2lap4 = random.randint(1, 10)
racer1time_tocover_thirdlanelap4 = 1000/(racer1speed_before_turning2lap4+racer1_acc2lap4)
print(racer1time_tocover_thirdlanelap4, 's')

racer2_acc2lap4 = random.randint(1, 10)
racer2time_tocover_thirdlanelap4 = 1000/(racer2speed_before_turning2lap4+racer2_acc2lap4)
print(racer2time_tocover_thirdlanelap4, 's')

racer3_acc2lap4 = random.randint(1, 10)
racer3time_tocover_thirdlanelap4 = 1000/(racer3speed_before_turning2lap4+racer3_acc2lap4)
print(racer3time_tocover_thirdlanelap4, 's')

racer4_acc2lap4 = random.randint(1, 10)
racer4time_tocover_thirdlanelap4 = 1000/(racer4speed_before_turning2lap4+racer4_acc2lap4)
print(racer4time_tocover_thirdlanelap4, 's')

print('it took racer one', racer1time_tocover_thirdlanelap4, 's', 'to cover 3rd lane lap 4')
time.sleep(3)
print('it took racer two', racer2time_tocover_thirdlanelap4, 's', 'to cover 3rd lane lap 4')
time.sleep(3)
print('it took racer three', racer3time_tocover_thirdlanelap4, 's', 'to cover 3rd lane lap 4')
time.sleep(3)
print('it took racer four', racer4time_tocover_thirdlanelap4, 's', 'to cover 3rd lane lap 4')
time.sleep(3)


racer1speed_redu3lap4 = random.randint(1, 10)
racer1speed_before_turning3lap4 = (racer1speed_before_turning2lap4+racer1_acc2lap4)-racer1speed_redu3lap4
print(racer1speed_before_turning3lap4, 'm/s')
racer1time_forbend3lap4 = 200/racer1speed_before_turning3lap4
print(racer1time_forbend3lap4, 's')

racer2speed_redu3lap4 = random.randint(1, 10)
racer2speed_before_turning3lap4 = (racer2speed_before_turning2lap4+racer2_acc2lap4)-racer2speed_redu3lap4
print(racer2speed_before_turning3lap4, 'm/s')
racer2time_forbend3lap4 = 200/racer2speed_before_turning3lap4
print(racer2time_forbend3lap4, 's')

racer3speed_redu3lap4 = random.randint(1, 10)
racer3speed_before_turning3lap4 = (racer3speed_before_turning2lap4+racer3_acc2lap4)-racer3speed_redu3lap4
print(racer3speed_before_turning3lap4, 'm/s')
racer3time_forbend3lap4 = 200/racer3speed_before_turning3lap4
print(racer3time_forbend3lap4, 's')

racer4speed_redu3lap4 = random.randint(1, 10)
racer4speed_before_turning3lap4 = (racer4speed_before_turning2lap4+racer4_acc2lap4)-racer4speed_redu3lap4
print(racer4speed_before_turning3lap4, 'm/s')
racer4time_forbend3lap4 = 200/racer4speed_before_turning3lap4
print(racer4time_forbend3lap4, 's')


racer1_acc3lap4 = random.randint(1, 10)
racer1time_tocover_fourthlanelap4 = 1000/(racer1speed_before_turning3lap4+racer1_acc3lap4)
print(racer1time_tocover_fourthlanelap4, 's')

racer2_acc3lap4 = random.randint(1, 10)
racer2time_tocover_fourthlanelap4 = 1000/(racer2speed_before_turning3lap4+racer2_acc3lap4)
print(racer2time_tocover_fourthlanelap4, 's')

racer3_acc3lap4 = random.randint(1, 10)
racer3time_tocover_fourthlanelap4 = 1000/(racer3speed_before_turning3lap4+racer3_acc3lap4)
print(racer3time_tocover_fourthlanelap4, 's')

racer4_acc3lap4 = random.randint(1, 10)
racer4time_tocover_fourthlanelap4 = 1000/(racer4speed_before_turning3lap4+racer4_acc3lap4)
print(racer4time_tocover_fourthlanelap4, 's')


racer1speed_redu4lap4 = random.randint(1, 10)
racer1speed_before_turning4lap4 = (racer1speed_before_turning3lap4+racer1_acc3lap4)-racer1speed_redu4lap4
print(racer1speed_before_turning4lap4, 'm/s')
racer1time_forbend4lap4 = 200/racer1speed_before_turning4lap4
print(racer1time_forbend4lap4, 's')

racer2speed_redu4lap4 = random.randint(1, 10)
racer2speed_before_turning4lap4 = (racer2speed_before_turning3lap4+racer2_acc3lap4)-racer2speed_redu4lap4
print(racer2speed_before_turning4lap4, 'm/s')
racer2time_forbend4lap4 = 200/racer2speed_before_turning4lap4
print(racer2time_forbend4lap4, 's')

racer3speed_redu4lap4 = random.randint(1, 10)
racer3speed_before_turning4lap4 = (racer3speed_before_turning3lap4+racer3_acc3lap4)-racer3speed_redu4lap4
print(racer3speed_before_turning4lap4, 'm/s')
racer3time_forbend4lap4 = 200/racer3speed_before_turning4lap4
print(racer3time_forbend4lap4, 's')

racer4speed_redu4lap4 = random.randint(1, 10)
racer4speed_before_turning4lap4 = (racer4speed_before_turning3lap4+racer4_acc3lap4)-racer1speed_redu4lap4
print(racer4speed_before_turning4lap4, 'm/s')
racer4time_forbend4lap4 = 200/racer4speed_before_turning4lap4
print(racer4time_forbend4lap4, 's')


racer1_fourthlap_time = racer1time_tocover_firstlanelap4+racer1time_forbend1lap4+racer1time_tocover_secondlanelap4+racer1time_forbend2lap4+racer1time_tocover_thirdlanelap4+racer1time_forbend3lap4+racer1time_tocover_fourthlanelap4+racer1time_forbend4lap4
print(racer1_fourthlap_time, 's', '4th lap time')
racer2_fourthlap_time = racer2time_tocover_firstlanelap4+racer2time_forbend1lap4+racer2time_tocover_secondlanelap4+racer2time_forbend2lap4+racer2time_tocover_thirdlanelap4+racer2time_forbend3lap4+racer2time_tocover_fourthlanelap4+racer2time_forbend4lap4
print(racer2_fourthlap_time, 's', '4th lap time')
racer3_fourthlap_time = racer3time_tocover_firstlanelap4+racer3time_forbend1lap4+racer3time_tocover_secondlanelap4+racer3time_forbend2lap4+racer3time_tocover_thirdlanelap4+racer3time_forbend3lap4+racer3time_tocover_fourthlanelap4+racer3time_forbend4lap4
print(racer3_fourthlap_time, 's', '4th lap time')
racer4_fourthlap_time = racer4time_tocover_firstlanelap4+racer4time_forbend1lap4+racer4time_tocover_secondlanelap4+racer4time_forbend2lap4+racer4time_tocover_thirdlanelap4+racer4time_forbend3lap4+racer4time_tocover_fourthlanelap4+racer4time_forbend4lap4
print(racer4_fourthlap_time, 's', '4th lap time')

print('it took racer one', racer1_fourthlap_time, 's', 'to cover 4th lap')
time.sleep(3)
print('it took racer two', racer2_fourthlap_time, 's', 'to cover 4th lap')
time.sleep(3)
print('it took racer three', racer3_fourthlap_time, 's', 'to cover 4th lap')
time.sleep(3)
print('it took racer four', racer4_fourthlap_time, 's', 'to cover 4th lap')
time.sleep(3)


a = [racer1_fourthlap_time, racer2_fourthlap_time, racer3_fourthlap_time, racer4_fourthlap_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
print(race_min)
time.sleep(2)
print(at[min_index], "had the shortest fourth lap time")

current_racer1_time = racer1_firstlap_time + racer1_secondlap_time + racer1_thirdlap_time + racer1_fourthlap_time
current_racer2_time = racer2_firstlap_time + racer2_secondlap_time + racer2_thirdlap_time + racer2_fourthlap_time
current_racer3_time = racer3_firstlap_time + racer3_secondlap_time + racer3_thirdlap_time + racer3_fourthlap_time
current_racer4_time = racer4_firstlap_time + racer4_secondlap_time + racer4_thirdlap_time + racer4_fourthlap_time

a = [current_racer1_time, current_racer2_time, current_racer3_time, current_racer4_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
time.sleep(2)
print(race_min)
time.sleep(3)
print(at[min_index], "is currently leading the race")



racer1_acclap5 = random.randint(1, 10)
print(racer1_acclap5)
racer1time_tocover_firstlanelap5 = 1000/(racer1speed_before_turning4+racer1_acclap5)
print(racer1speed_before_turning4+racer1_acclap5, 'speed for starting lap 5')
print(racer1time_tocover_firstlanelap5, 's')

racer2_acclap5 = random.randint(1, 10)
print(racer2_acclap5)
racer2time_tocover_firstlanelap5 = 1000/(racer2speed_before_turning4+racer2_acclap5)
print(racer2speed_before_turning4+racer2_acclap5, 'speed for starting lap 5')
print(racer2time_tocover_firstlanelap5, 's')

racer3_acclap5 = random.randint(1, 10)
print(racer3_acclap5)
racer3time_tocover_firstlanelap5 = 1000/(racer3speed_before_turning4+racer3_acclap5)
print(racer3speed_before_turning4+racer3_acclap5, 'speed for starting lap 5')
print(racer3time_tocover_firstlanelap5, 's')

racer4_acclap5 = random.randint(1, 10)
print(racer4_acclap5)
racer4time_tocover_firstlanelap5 = 1000/(racer4speed_before_turning4+racer4_acclap5)
print(racer4speed_before_turning4+racer4_acclap5, 'speed for starting lap 5')
print(racer4time_tocover_firstlanelap5, 's')


print('it took racer one', racer1time_tocover_firstlanelap5, 's', 'to cover ist lane lap 5')
time.sleep(3)
print('it took racer two', racer2time_tocover_firstlanelap5, 's', 'to cover ist lane lap 5')
time.sleep(3)
print('it took racer three', racer3time_tocover_firstlanelap5, 's', 'to cover ist lane lap 5')
time.sleep(3)
print('it took racer four', racer4time_tocover_firstlanelap5, 's', 'to cover ist lane lap 5')
time.sleep(3)


racer1speed_redu1lap5 = random.randint(1, 10)
racer1speed_before_turninglap5 = (racer1speed_before_turning4+racer1_acclap5)-racer1speed_redu1lap5
print(racer1speed_before_turninglap5, 'm/s')
racer1time_forbend1lap5 = 200/racer1speed_before_turninglap5
print(racer1time_forbend1lap5, 's')

racer2speed_redu1lap5 = random.randint(1, 10)
racer2speed_before_turninglap5 = (racer2speed_before_turning4+racer2_acclap5)-racer2speed_redu1lap5
print(racer2speed_before_turninglap5, 'm/s')
racer2time_forbend1lap5 = 200/racer2speed_before_turninglap5
print(racer2time_forbend1lap5, 's')

racer3speed_redu1lap5 = random.randint(1, 10)
racer3speed_before_turninglap5 = (racer3speed_before_turning4+racer3_acclap5)-racer3speed_redu1lap5
print(racer3speed_before_turninglap5, 'm/s')
racer3time_forbend1lap5 = 200/racer3speed_before_turninglap5
print(racer3time_forbend1lap5, 's')

racer4speed_redu1lap5 = random.randint(1, 10)
racer4speed_before_turninglap5 = (racer4speed_before_turning4+racer4_acclap5)-racer4speed_redu1lap5
print(racer4speed_before_turninglap5, 'm/s')
racer4time_forbend1lap5 = 200/racer4speed_before_turninglap5
print(racer4time_forbend1lap5, 's')


racer1_acc1lap5 = random.randint(1, 10)
racer1time_tocover_secondlanelap5 = 1000/(racer1speed_before_turninglap5+racer1_acc1lap5)
print(racer1time_tocover_secondlanelap5, 's')

racer2_acc1lap5 = random.randint(1, 10)
racer2time_tocover_secondlanelap5 = 1000/(racer2speed_before_turninglap5+racer2_acc1lap5)
print(racer2time_tocover_secondlanelap5, 's')

racer3_acc1lap5 = random.randint(1, 10)
racer3time_tocover_secondlanelap5 = 1000/(racer3speed_before_turninglap5+racer3_acc1lap5)
print(racer3time_tocover_secondlanelap5, 's')

racer4_acc1lap5 = random.randint(1, 10)
racer4time_tocover_secondlanelap5 = 1000/(racer4speed_before_turninglap5+racer4_acc1lap5)
print(racer4time_tocover_secondlanelap5, 's')

print('it took racer one', racer1time_tocover_secondlanelap5, 's', 'to cover 2nd lane lap 5')
time.sleep(3)
print('it took racer two', racer2time_tocover_secondlanelap5, 's', 'to cover 2nd lane lap 5')
time.sleep(3)
print('it took racer three', racer3time_tocover_secondlanelap5, 's', 'to cover 2nd lane lap 5')
time.sleep(3)
print('it took racer four', racer4time_tocover_secondlanelap5, 's', 'to cover 2nd lane lap 5')
time.sleep(3)


racer1speed_redu2lap5 = random.randint(1, 10)
racer1speed_before_turning2lap5 = (racer1speed_before_turninglap5+racer1_acc1lap5)-racer1speed_redu2lap5
print(racer1speed_before_turning2lap5, 'm/s')
racer1time_forbend2lap5 = 200/racer1speed_before_turning2lap5
print(racer1time_forbend2lap5, 's')

racer2speed_redu2lap5 = random.randint(1, 10)
racer2speed_before_turning2lap5 = (racer2speed_before_turninglap5+racer2_acc1lap5)-racer2speed_redu2lap5
print(racer2speed_before_turning2lap5, 'm/s')
racer2time_forbend2lap5 = 200/racer2speed_before_turning2lap5
print(racer2time_forbend2lap5, 's')

racer3speed_redu2lap5 = random.randint(1, 10)
racer3speed_before_turning2lap5 = (racer3speed_before_turninglap5+racer3_acc1lap5)-racer3speed_redu2lap5
print(racer3speed_before_turning2lap5, 'm/s')
racer3time_forbend2lap5 = 200/racer3speed_before_turning2lap5
print(racer3time_forbend2lap5, 's')

racer4speed_redu2lap5 = random.randint(1, 10)
racer4speed_before_turning2lap5 = (racer4speed_before_turninglap5+racer4_acc1lap5)-racer4speed_redu2lap5
print(racer4speed_before_turning2lap5, 'm/s')
racer4time_forbend2lap5 = 200/racer4speed_before_turning2lap5
print(racer4time_forbend2lap5, 's')


racer1_acc2lap5 = random.randint(1, 10)
racer1time_tocover_thirdlanelap5 = 1000/(racer1speed_before_turning2lap5+racer1_acc2lap5)
print(racer1time_tocover_thirdlanelap5, 's')

racer2_acc2lap5 = random.randint(1, 10)
racer2time_tocover_thirdlanelap5 = 1000/(racer2speed_before_turning2lap5+racer2_acc2lap5)
print(racer2time_tocover_thirdlanelap5, 's')

racer3_acc2lap5 = random.randint(1, 10)
racer3time_tocover_thirdlanelap5 = 1000/(racer3speed_before_turning2lap5+racer3_acc2lap5)
print(racer3time_tocover_thirdlanelap5, 's')

racer4_acc2lap5 = random.randint(1, 10)
racer4time_tocover_thirdlanelap5 = 1000/(racer4speed_before_turning2lap5+racer4_acc2lap5)
print(racer4time_tocover_thirdlanelap5, 's')

print('it took racer one', racer1time_tocover_thirdlanelap5, 's', 'to cover 3rd lane lap 5')
time.sleep(3)
print('it took racer two', racer2time_tocover_thirdlanelap5, 's', 'to cover 3rd lane lap 5')
time.sleep(3)
print('it took racer three', racer3time_tocover_thirdlanelap5, 's', 'to cover 3rd lane lap 5')
time.sleep(3)
print('it took racer four', racer4time_tocover_thirdlanelap5, 's', 'to cover 3rd lane lap 5')
time.sleep(3)


racer1speed_redu3lap5 = random.randint(1, 10)
racer1speed_before_turning3lap5 = (racer1speed_before_turning2lap5+racer1_acc2lap5)-racer1speed_redu3lap5
print(racer1speed_before_turning3lap5, 'm/s')
racer1time_forbend3lap5 = 200/racer1speed_before_turning3lap5
print(racer1time_forbend3lap5, 's')

racer2speed_redu3lap5 = random.randint(1, 10)
racer2speed_before_turning3lap5 = (racer2speed_before_turning2lap5+racer2_acc2lap5)-racer2speed_redu3lap5
print(racer2speed_before_turning3lap5, 'm/s')
racer2time_forbend3lap5 = 200/racer2speed_before_turning3lap5
print(racer2time_forbend3lap5, 's')

racer3speed_redu3lap5 = random.randint(1, 10)
racer3speed_before_turning3lap5 = (racer3speed_before_turning2lap5+racer3_acc2lap5)-racer3speed_redu3lap5
print(racer3speed_before_turning3lap5, 'm/s')
racer3time_forbend3lap5 = 200/racer3speed_before_turning3lap5
print(racer3time_forbend3lap5, 's')

racer4speed_redu3lap5 = random.randint(1, 10)
racer4speed_before_turning3lap5 = (racer4speed_before_turning2lap5+racer4_acc2lap5)-racer4speed_redu3lap5
print(racer4speed_before_turning3lap5, 'm/s')
racer4time_forbend3lap5 = 200/racer4speed_before_turning3lap5
print(racer4time_forbend3lap5, 's')


racer1_acc3lap5 = random.randint(1, 10)
racer1time_tocover_fourthlanelap5 = 1000/(racer1speed_before_turning3lap5+racer1_acc3lap5)
print(racer1time_tocover_fourthlanelap5, 's')

racer2_acc3lap5 = random.randint(1, 10)
racer2time_tocover_fourthlanelap5 = 1000/(racer2speed_before_turning3lap5+racer2_acc3lap5)
print(racer2time_tocover_fourthlanelap5, 's')

racer3_acc3lap5 = random.randint(1, 10)
racer3time_tocover_fourthlanelap5 = 1000/(racer3speed_before_turning3lap5+racer3_acc3lap5)
print(racer3time_tocover_fourthlanelap5, 's')

racer4_acc3lap5 = random.randint(1, 10)
racer4time_tocover_fourthlanelap5 = 1000/(racer4speed_before_turning3lap5+racer4_acc3lap5)
print(racer4time_tocover_fourthlanelap5, 's')


racer1speed_redu4lap5 = random.randint(1, 10)
racer1speed_before_turning4lap5 = (racer1speed_before_turning3lap5+racer1_acc3lap5)-racer1speed_redu4lap5
print(racer1speed_before_turning4lap5, 'm/s')
racer1time_forbend4lap5 = 200/racer1speed_before_turning4lap5
print(racer1time_forbend4lap5, 's')

racer2speed_redu4lap5 = random.randint(1, 10)
racer2speed_before_turning4lap5 = (racer2speed_before_turning3lap5+racer2_acc3lap5)-racer2speed_redu4lap5
print(racer2speed_before_turning4lap5, 'm/s')
racer2time_forbend4lap5 = 200/racer2speed_before_turning4lap5
print(racer2time_forbend4lap5, 's')

racer3speed_redu4lap5 = random.randint(1, 10)
racer3speed_before_turning4lap5 = (racer3speed_before_turning3lap5+racer3_acc3lap5)-racer3speed_redu4lap5
print(racer3speed_before_turning4lap5, 'm/s')
racer3time_forbend4lap5 = 200/racer3speed_before_turning4lap5
print(racer3time_forbend4lap5, 's')

racer4speed_redu4lap5 = random.randint(1, 10)
racer4speed_before_turning4lap5 = (racer4speed_before_turning3lap5+racer4_acc3lap5)-racer1speed_redu4lap5
print(racer4speed_before_turning4lap5, 'm/s')
racer4time_forbend4lap5 = 200/racer4speed_before_turning4lap5
print(racer4time_forbend4lap5, 's')


racer1_fifthlap_time = racer1time_tocover_firstlanelap5+racer1time_forbend1lap5+racer1time_tocover_secondlanelap5+racer1time_forbend2lap5+racer1time_tocover_thirdlanelap5+racer1time_forbend3lap5+racer1time_tocover_fourthlanelap5+racer1time_forbend4lap5
print(racer1_fifthlap_time, 's', '5th lap time')
racer2_fifthlap_time = racer2time_tocover_firstlanelap5+racer2time_forbend1lap5+racer2time_tocover_secondlanelap5+racer2time_forbend2lap5+racer2time_tocover_thirdlanelap5+racer2time_forbend3lap5+racer2time_tocover_fourthlanelap5+racer2time_forbend4lap5
print(racer2_fifthlap_time, 's', '5th lap time')
racer3_fifthlap_time = racer3time_tocover_firstlanelap5+racer3time_forbend1lap5+racer3time_tocover_secondlanelap5+racer3time_forbend2lap5+racer3time_tocover_thirdlanelap5+racer3time_forbend3lap5+racer3time_tocover_fourthlanelap5+racer3time_forbend4lap5
print(racer3_fifthlap_time, 's', '5th lap time')
racer4_fifthlap_time = racer4time_tocover_firstlanelap5+racer4time_forbend1lap5+racer4time_tocover_secondlanelap5+racer4time_forbend2lap5+racer4time_tocover_thirdlanelap5+racer4time_forbend3lap5+racer4time_tocover_fourthlanelap5+racer4time_forbend4lap5
print(racer4_fifthlap_time, 's', '5th lap time')

print('it took racer one', racer1_fifthlap_time, 's', 'to cover 5th lap')
time.sleep(3)
print('it took racer two', racer2_fifthlap_time, 's', 'to cover 5th lap')
time.sleep(3)
print('it took racer three', racer3_fifthlap_time, 's', 'to cover 5th lap')
time.sleep(3)
print('it took racer four', racer4_fifthlap_time, 's', 'to cover 5th lap')
time.sleep(3)


a = [racer1_fifthlap_time, racer2_fifthlap_time, racer3_fifthlap_time, racer4_fifthlap_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
print(race_min)
time.sleep(2)
print(at[min_index], "had the shortest fourth lap time")

current_racer1_time = racer1_firstlap_time + racer1_secondlap_time + racer1_thirdlap_time + racer1_fourthlap_time + racer1_fifthlap_time
current_racer2_time = racer2_firstlap_time + racer2_secondlap_time + racer2_thirdlap_time + racer2_fourthlap_time + racer2_fifthlap_time
current_racer3_time = racer3_firstlap_time + racer3_secondlap_time + racer3_thirdlap_time + racer3_fourthlap_time + racer3_fifthlap_time
current_racer4_time = racer4_firstlap_time + racer4_secondlap_time + racer4_thirdlap_time + racer4_fourthlap_time + racer4_fifthlap_time

a = [current_racer1_time, current_racer2_time, current_racer3_time, current_racer4_time]
at = ['racer 1', 'racer 2', 'racer 3', 'racer 4']
race_min = min(a)
min_index = a.index(race_min)
time.sleep(2)
print(race_min)
time.sleep(3)
print(at[min_index], "is currently leading the race")







