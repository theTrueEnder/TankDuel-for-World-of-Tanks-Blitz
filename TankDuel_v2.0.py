#Copyright 2020, Kai Delsing, all rights reserved

##TO-DO##
#av vs max/min rolls
#shell velocity and distancwe
#graphical hp bar

#####################################################
############### ENTER TANK STATS HERE ###############
#####################################################
tank_1_name = 'Obj. 704'
tank_1_hp = 1500
tank_1_damage = 640
tank_1_reload_time = 11.79
tank_1_adrenaline = False
#---------------------------------------------------#
tank_2_name = 'T-55A'
tank_2_hp = 1650
tank_2_damage = 310
tank_2_reload_time = 6.32
tank_2_adrenaline = False
#####################################################
#####################################################
#####################################################


#Name, HP, Damage, Reload, Adrenaline
tank1stats = [tank_1_name, tank_1_hp, tank_1_damage, tank_1_reload_time, tank_1_adrenaline]
tank2stats = [tank_2_name, tank_2_hp, tank_2_damage, tank_2_reload_time, tank_2_adrenaline]

class duel():
    def __init__(self):
        self.adr_cooldown = 75
        self.adr_duration = -15
        self.t1_name, self.t2_name = tank1stats[0], tank2stats[0]
        self.t1_hp, self.t2_hp = tank1stats[1], tank2stats[1]
        self.t1_dmg, self.t2_dmg = tank1stats[2], tank2stats[2]
        self.t1_rld, self.t2_rld = tank1stats[3], tank2stats[3]
        self.t1_adr, self.t2_adr = tank1stats[4], tank2stats[4]

        self.time = 0.000   #global time
        self.t1_active, self.t2_active = self.t1_rld, self.t2_rld      #active reload countdowns

        self.t1_adr_x, self.t2_adr_x = 1, 1   #tank1's adrenaline multiplier
        self.t1_adr_cool, self.t2_adr_cool = 0, 0     #adrenaline cooldown

        self.run_sim()

    def tank1_fire(self):
        self.t2_hp -= self.t1_dmg
        print(self.t1_name, 'fires, dealing', self.t1_dmg, 'damage.')
        self.state()
        self.t1_active = self.t1_rld

    def tank2_fire(self):
        self.t1_hp -= self.t2_dmg
        print(self.t2_name, 'fires, dealing', self.t2_dmg, 'damage.')
        self.state()
        self.t2_active = self.t2_rld

    def state(self):
        print('Time: {:0.2f}'.format(self.time), 'seconds')
        print(self.t1_name, 'has', self.t1_hp, 'HP remaining.')
        print(self.t2_name, 'has', self.t2_hp, 'HP remaining.\n')

    def check_sim(self):
        if self.t1_hp <= 0:
            print('!!!', self.t1_name, 'destroyed !!!\n')
            return False
        elif self.t2_hp <=0:
            print('!!!', self.t2_name, 'destroyed !!!\n')
            return False
        else:
            return True

    def run_sim(self):
        print(self.t1_name, 'vs', self.t2_name)
        self.tank1_fire()
        self.time += .001
        self.tank2_fire()

        while(self.time < 1000):
            self.time += .001
            self.t1_adr_cool -= 0.001
            self.t2_adr_cool -= 0.001

            if self.t1_adr_cool < -15
                self.t1_adr_cool = 75
            if self.t2_adr_cool < -15
                self.t2_adr_cool = 75

            if self.t1_adr and self.t1_adr_cool <= 0:
                self.t1_adr_x = 1.2
            else:
                self.t1_adr_x = 1
            if self.t2_adr and self.t2_adr_cool:
                self.t2_adr_x = 1.2
            else:
                self.t2_adr_x = 1

            self.t1_active, self.t2_active = self.t1_active - (.001 * self.t1_adr_x), self.t2_active - (.001 * self.t2_adr_x)
            if self.t1_active <= 0:
                i = self.t1_active
                self.tank1_fire()
                self.t1_active -= i #eliminate error from excess speed

            if not self.check_sim():
                break;

            if self.t2_active <= 0:
                i = self.t2_active
                self.tank2_fire()
                self.t2_active -= i #eliminate error from excess speed

            if not self.check_sim():
                break;

        if self.t1_active <= .001 or self.t2_active <= .001:
            print('Result: Tie')
            print('Tanks destroyed each other within margin of error.')

        elif self.t1_hp > self.t2_hp:
            print(self.t1_name, 'wins with', self.t1_hp, 'hp remaining')

        elif self.t1_hp < self.t2_hp:
            print(self.t2_name, 'wins with', self.t2_hp, 'hp remaining')

        else:
            print('Error')


duel()
