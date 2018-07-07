#!/usr/bin/python

import matplotlib.pyplot  as plt
import mpld3

fig,y=plt.subplots()

x1=[2,4,5,9]
y1=[3,7,8,9]
x2=[4,6,8,3]
y2=[9,6,2,2]
plt.bar(x1,y1)
plt.bar(x2,y2)
mpld3.save_html(fig,'aa.html')

