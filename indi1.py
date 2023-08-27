#!/usr/bin/env python3
# -*- coding: utf-8 -*-

stoimost_july_shop1 = (100, 200, 300, 400)
stoimost_august_shop1 = (150, 250, 350, 450)

stoimost_july_shop2 = (50, 100, 150, 200)
stoimost_august_shop2 = (75, 125, 175, 225)

vsya_stoimost = 0

for stoimost in stoimost_july_shop1:
    vsya_stoimost += stoimost

for stoimost in stoimost_august_shop1:
    vsya_stoimost += stoimost

for stoimost in stoimost_july_shop2:
    vsya_stoimost += stoimost

for stoimost in stoimost_august_shop2:
    vsya_stoimost += stoimost

print("Total sales for July and August:", vsya_stoimost)