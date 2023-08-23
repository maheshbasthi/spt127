import pandas as pd
import numpy as np

import matplotlib.pyplot as plt
data = pd.read_csv("C:/Users/SPTINT-16/Downloads/tips.csv")
print(data)

plt.scatter(data['day'],data['tip'])
plt.xlabel('data')
plt.ylabel('tip')
plt.title('scatter plot')
plt.show()

plt.plot(data['tip'])
plt.xlabel('tip')
plt.title('line plot')
plt.show()


plt.bar(data['day'],data['tip'])
plt.xlabel('day')
plt.ylabel('tip')
plt.title('bar plot')
plt.show()

plt.hist(data['total_bill'])
plt.title('histogram plot')
plt.show()


