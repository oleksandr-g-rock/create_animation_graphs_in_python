import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('seaborn')
fig = plt.figure()
ax = fig.add_subplot(1,1,1)

def animation(i):
  data_for_show = pd.read_csv('data_for_show.txt')
  x = []
  y = []

  x = data_for_show[0:i]['Time']
  y = data_for_show[0:i]['Value']

  ax.clear()
  ax.plot(x, y)

  plt.xlabel('Time in seconds')
  plt.ylabel('Value')
  plt.title('data_for_show') 

animation = FuncAnimation(fig, func=animation, interval=250)
plt.show()
