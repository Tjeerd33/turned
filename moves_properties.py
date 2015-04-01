# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:38:46 2015

@author: Tjeerd
"""
import random
class move:
    def __init__(self, damage=0, element='none',misschance=[], miss=0, hit=0, effect=[], effected_stats=[], effect_target='enemy', up=0, lower=0, increase_life=0, mana_cost=0, discription='', lvl_required=0):
        self.damage=0
        self.element='none'
        self.misschance=misschance
        self.lvl_required=lvl_required
        try:
            for i in range(miss):
                self.misschance.append('miss')
            for i in range(hit):
                self.misschance.append('hit')
            self.accuracy=self.misschance.count('hit')/len(self.misschance)*100
        except ZeroDivisionError:
            self.accuracy=100
            self.misschance=['hit']
        self.status='available'
        self.mana_cost=mana_cost
        self.effect={}
        self.affected=effect_target
        if 'lower stats' in effect:
            for i in effected_stats:
                self.effect['lower {}'.format(i)]=lower
        elif 'disable' in effect:
            self.effect['disable']='disabled'
        elif 'increase stats' in effect:
            for i in effected_stats:
                self.effect['up {}'.format(i)]=up
        elif 'increase life' in effect:
            self.effect['increase life']=increase_life
        self.str=discription
    def __str__(self):
        return self.str
    def use(self, target, target_dict, user, user_dict):
        try:
            if user_dict[user].mana>self.mana_cost:
                user_dict[user].mana-=self.mana_cost
                if random.choice(self.misschance)!='miss' and self.status!='disable':
                    damage_done=target_dict[target].take_damage(elemental=self.element, damage=self.damage)
                    for i in self.effect:
                        if 'lower' in i and self.affected=='enemy':
                            target_dict[target].lower_stats(stat=i[7:],lower=self.effect[i])
                        elif 'up' in i and self.affected=='enemy':
                            target_dict[target].lowet_stats(stat=i[4:], lower=-self.effect[i])
                        elif 'disable' in i and self.affected=='enemy':
                            target_dict[target].dissable_move()
                        elif 'burn' in i and self.affected=='enemy':
                            target_dict[target].change_status('burning')
                    return damage_done
                else:
                    return 'missed'
            else:
                return 'not enough mana'
        except KeyError:
            print("Key error, move isn't used correctly")
    def disable(self):
        self.status='disabled'
