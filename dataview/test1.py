import matplotlib.pyplot as plt
squares= [1,4,9,16,25,36]
plt.plot(squares,linewidth= 5)
plt.title("Squares Numbers",fontsize = 24)
plt.xlabel('Value',fontsize = 14)
plt.ylabel('Squares of Value',fontsize = 14)
plt.tick_params(axis='both',labelsize = 14)

plt.show()
