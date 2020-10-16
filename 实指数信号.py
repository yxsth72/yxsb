#yxsb
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.rcParams['font.family']='SimHei'
matplotlib.rcParams['axes.unicode_minus']=False

plt.subplot(2,2,1)
t = np.linspace(-1.0,1.0,500) 
plt.ylim(0,2)
x = np.exp(-2*t)
plt.plot(t,x)
x = np.exp(2*t)
plt.plot(t,x)
x = np.exp(0*t)
plt.plot(t,x)
plt.title("实指数信号")
plt.xlabel("t")
plt.ylabel("x")

plt.subplot(2,2,2)
x=np.arange(-1*np.pi,1*np.pi,0.01)
y=np.cos(x+1)
plt.title("正弦信号")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x,y)

plt.subplot(2,2,3)
t=np.arange(-5,10,0.01)
x=0.1*np.exp(0.1*t)*np.cos(np.pi*t+0.5*np.pi)
plt.title("幅度衰减")
plt.xlabel("t")
plt.ylabel("x")
plt.plot(t,x)

plt.subplot(2,2,4)
t=np.arange(-5,10,0.01)
x=0.1*np.exp(-0.1*t)*np.cos(np.pi*t+0.5*np.pi)
plt.title("幅度增长")
plt.xlabel("t")
plt.ylabel("x")
plt.plot(t,x)

plt.show()
