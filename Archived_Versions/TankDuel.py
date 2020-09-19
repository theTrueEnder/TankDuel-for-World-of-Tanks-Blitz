#Copyright 2020, Kai Delsing, all rights reserved

##TO-DO##
#classes for each tank (no [2] pointers, etc, tank2.hp)
#av vs max/min rolls
#shell velocity and distancwe


#Name, HP, Damage, Reload, Adrenaline
tank1 = ['Obj. 704', 1500, 640, 11.79, False]
tank2 = ['T-55A', 1650, 310, 6.32, False]

################################################################
time = [0.000, tank1[3], tank2[3]]
active = True
adr = [0, 0, 75, 75]
def tank1_fire():
    tank2[1] -= tank1[2]
    print(tank1[0], 'fires, dealing', tank1[2], 'damage.')
    state()
    time[1] = tank1[3]

def tank2_fire():
    tank1[1] -= tank2[2]
    print(tank2[0], 'fires, dealing', tank2[2], 'damage.')
    state()
    time[2] = tank2[3]

def state():
    print('Time: {:0.2f}'.format(time[0]), 'seconds')
    print(tank1[0], 'has', tank1[1], 'HP remaining.')
    print(tank2[0], 'has', tank2[1], 'HP remaining.\n')

def check_sim():
    if tank1[1] <= 0 or tank2[1] <=0:
        return False
    else:
        return True

def run_sim():
    if tank1[4]:
        adr[0] = 1.2
    else:
        adr[0] = 1
    if tank2[4]:
        adr[1] = 1.2
    else:
        adr[1] = 1

    print('Begin Simulation:', tank1[0], 'vs', tank2[0])
    tank1_fire()
    time[0] += .001
    tank2_fire()

    while(time[0] < 1000):
        time[0] += .001
        adr[2] -= 0.001
        adr[3] -= 0.001

        time[1], time[2] = time[1] - (.001 * adr[0]), time[2] - (.001 * adr[1])
        if time[1] <= 0:
            i = time[1]
            tank1_fire()
            time[1] -= i #eliminate error from excess speed

        if not check_sim():
            break;

        if time[2] <= 0:
            i = time[2]
            tank2_fire()
            time[2] -= i #eliminate error from excess speed

        if not check_sim():
            break;

    print('Simulation Complete.')
    state()
    if time[1] <= .001 or time[2] <= .001:
        print('Result: Tie')
        print('Tanks destroyed each other within margin of error.')

    elif tank1[1] > tank2[1]:
        print('Result:', tank1[0], 'wins.')

    elif tank1[1] < tank2[1]:
        print('Result:', tank2[0], 'wins.')

    else:
        print('Error')


run_sim()
