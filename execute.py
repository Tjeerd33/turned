# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 19:55:52 2015

@author: Tjeerd
"""
import random
import moves_library
from tkinter import *
from tkinter import messagebox
class turner:
    def __init__(self, hp=0, strenght=0, defense=0, magic=0, speec=0, mana=0, mana_regen=0, moves=[], element='none', lvl=0):
        self.hp=hp
        self.strenght=strenght
        self.defense=defense
        self.magic=magic
        self.mana=0
        self.mana_regen=mana_regen
        self.moves=moves
        self.element=element
        self.status='normal'
        self.lvl=lvl
    def take_damage(self, elemental='none', damage=0):
        damage-=self.defense
        if self.element=='fire':
            if elemental=='water':
                damage*=2
            elif elemental=='fire':
                damage/=2
        elif self.element=='water':
            if (elemental=='electricity' or elemental=='grass'):
                damage*=2
            elif elemental=='fire':
                damage=0
        elif self.element=='grass':
            if elemental=='fire':
                damage*=2
            elif(elemental=='electricity' or elemental=='water' or elemental=='grass'):
                damage/=2
        elif self.element=='electricity':
            if elemental=='ground':
                damage*=2
            elif elemental=='electricity':
                damage/=2
        elif self.element=='magic':
            if elemental=='dark magic':
                damage*=2
            elif elemental=='magic' or elemental=='electricity' or elemental=='fire':
                damage/=2
        elif self.element=='dark magic':
            if elemental=='nature' or elemental=='grass':
                damage*=2
            elif elemental=='dark magic':
                damage/=4
        elif self.element=='physical':
            if elemental=='physical':
                if damage<self.strenght:
                    damage/=2
            elif elemental=='magic':
                damage*=2
        elif self.element=='nature':
            if elemental=='fire':
                damage*=2
            elif elemental=='grass' or elemental=='ground' or elemental=='water':
                damage/=2
        elif self.element=='ground':
            if elemental=='electricity':
                damage=0
            elif elemental=='water' or elemental=='grass':
                damage*=2
        if damage<0:
            damage=0
        self.hp-=damage
        return int(damage)
    def lower_stats(self, stat, lower):
        if stat=='strenght':
            self.strenght-=lower
        elif stat=='speed':
            self.speed-=lower
        elif stat=='defense':
            self.defense-=lower
        elif stat=='magic':
            self.magic-=lower
        elif stat=='mana':
            self.mana-=lower
        elif stat=='mana_regen':
            self.mana_regen-=mana_regen
    def disable_move(self):
        disabled=random.choice(self.moves)
        moves_dict[disabled].disable()
    def change_status(self, new_status):
        self.status=new_status
        return self.status
class player(turner):
    def select_moves(self):
        self.moves_select=Tk()
        self.moves_select.title('select moves')
        Label(self.moves_select, text='selected moves:').pack()
        selected_moves={}
        x=0
        for i in self.moves:
            x+=1
            selected_moves['selected{}'.format(x)]=StringVar(self.moves_select)
            selected_moves['selected{}'.format(x)].set(i)
        if self.moves==[]:
            Label(self.moves_select, text='none').pack()
        for i in selected_moves:
            Label(self.moves_select, text=selected_moves[i], textvariable=selected_moves[i]).pack()
        Label(self.moves_select, text='available moves:').pack()
        self.available_moves=Listbox(self.moves_select)
        self.available_moves.pack()
        for i in moves_library.moves_dict:
            if moves_library.moves_dict[i].lvl_required==self.lvl:
                self.available_moves.insert(0, '{0}: {1}'.format(i, str(moves_library.moves_dict[i].element)))
        self.moves_select.mainloop()
        
