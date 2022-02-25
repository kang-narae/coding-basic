import matplotlib.pyplot as plt
import matplotlib 
import pandas as pd

matplotlib.rcParams['font.family'] = 'Malgun Gothic'
matplotlib.rcParams['font.size']=15
matplotlib.rcParams['axes.unicode_minus'] = False
df= pd.read_excel('score.xlsx')


x=[1,2,3]
y=[2,4,8]
yy=[2,9,5]

plt.title('학생성적 그래프')
plt.plot(df['이름'],df['국어'], label='국어')
plt.plot(df['이름'],df['영어'], label='영어')
plt.plot(df['이름'],df['수학'], label='수학')
plt.plot(df['이름'],df['사회'], label='사회')
plt.plot(df['이름'],df['과학'], label='과학')
plt.legend()
plt.show()