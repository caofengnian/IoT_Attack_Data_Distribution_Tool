import matplotlib.pyplot as plt
import numpy as np

#x=np.arange(0,1,0.001)
x=[0,0.4,0.6,1]
#y=-0.5675*pow(x,0.5)+1
#y3=-0.515*pow(x,0.5)+1
#y4=-0.675*pow(x,0.5)+1
#y5=-0.0725*pow(x,0.5)+1
#y6=np.cos(x*8)*1.4
#y7=-pow(x,2)+1
#y7=[1,1]
y7=[1,1,0,0]

x2=[0,1]
y2=[0.5,0.5]

#plt.plot(x,y,label='Connection & SYN Flooding')
#plt.plot(x,y3,label='Get & CC Flooding')
#plt.plot(x,y4,label='SQL Search')
#plt.plot(x,y5,label='UDP Flooding')
#plt.plot(x,y6,label='Node Attack')
plt.plot(x,y7,label='RansomWare Attack')
plt.plot(x2,y2,'--')
plt.xlabel('Confidence of Attack')
plt.ylabel('Probability of Operation')
plt.title('Output Distribution')
plt.xlim(0,1)
plt.ylim(-0.05,1.05)
plt.legend(loc='down')


plt.show()