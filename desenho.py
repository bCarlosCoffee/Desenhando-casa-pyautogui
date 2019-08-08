# -*- coding: utf-8 -*-

# Carlos coffee
# Caffee Tec 2019

import pyautogui as pg 

def pintar(codernadas):
	for i in codernadas:
		x = i[0]
		y = i[1]

		pg.dragRel(x,y, button='left', duration=1)

# Casa
telhado = [(0,-60), (160, -200), (50,0), (160,200), (0, 60),(-160, -200), (-50,0), (-160, 200)]
corpo = [(40, -50), (0, 200), (289, 0), (0,-200)]
porta = [(0, 200), (-90, 0), (0, -200), (-100,0),(0, 200)]
chamine = [(190,0), (0, -200), (40, 50), (0, -60), (-110, -140), (0, -80), (50,0), (0, 140)]

pintar(telhado)
pintar(corpo)
pintar(porta)
pintar(chamine)