import matplotlib.pyplot as plt
from random_walk import  RandomWalk
while True:

  rw = RandomWalk(50000)
  rw.fill_wark()
  plt.figure(figsize=(10,3),dpi=128)
  point_numbers = list(range(rw.num_points))
  plt.scatter(rw.x_values, rw.y_values, c=point_numbers, edgecolors='none', s=1)
  plt.scatter(0,0,c = 'green',edgecolors='none',s = 100)
  plt.scatter(rw.x_values[-1],rw.y_values[-1],c = 'red',edgecolors='none',s = 15)
  plt.axes().get_xaxis().set_visible(False)
  plt.axes().get_yaxis().set_visible(False)
  plt.show()
  keep_running = raw_input("Make another wark?(y/n):")
  if keep_running == 'n':
      break
