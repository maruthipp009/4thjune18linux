import matplotlib.pyplot  as plt
import mpld3
x1=[2,4,5,9]
x2=[4,3,10,7]
y1=[4,6,8,3]
y2=[1,5,8,3]
plt.plot(x1,y1)
plt.plot(x2,y2)
plt.bar(x1,y1)
plt.bar(x2,y2)
mpld3.show()


