# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 20:38:46 2015

@author: Tjeerd
"""
#list of possible effects:
#disable, lower stats (you have to define which stat and by how much, effect target is optional), increase stats, increase life 
#burned will be added shortly
import moves_properties
moves_dict={}
moves_dict['fire ball']=moves_properties.move(damage=80, element='fire', miss=10, hit=90, effect='burn',
 mana_cost=40, discription='shoots a fireball at the opponent, can inflict burns', lvl_required=5)
moves_dict['CHARGE']=moves_properties.move(damage=10, element='physical', miss=5, hit=95, mana_cost=0,
 discription='charge at the enemy to inflict very low dmg', lvl_required=0)
