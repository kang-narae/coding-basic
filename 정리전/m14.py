import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')

plt.bar(df['이름'], df['국어'])
plt.xticks(df['이름'], rotation=45)
plt.show()