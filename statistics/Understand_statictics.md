# 統計学がわかる

```python
import pandas as pd
import numpy as np 
from scipy import stats
import math
``` 
## 分散
```math
分散 = ((データ - 平均値)^2 の総和)/サンプルサイズ
数値が大きいほどばらつきが大きい(Numpy)
```
## 標準偏差
```math
標準偏差 = \sqrt{分散}
```
## 不偏分散
```math
不偏分散 = ((データ - 平均値)^2 の総和)/(サンプルサイズ - 1)
サンプルサイズが大きく、母集団からサンプリングしたときに使用(Pandas, Scipy)
```
練習問題
```python
core = {
    'ch' : [78, 62, 81, 59, 72, 68, 75, 65, 80, 60, 78, 62, 70],
    'pe' : [70, 72, 68, 75, 65, 71, 69, 76, 64, 80, 60, 73, 67],
    'wi' : [57, 59, 55, 62, 52, 58, 56, 63, 51, 67, 47, 60, 54]
}
df = pd.DataFrame(score)
df 

#	ch	pe	wi
#0	78	70	57
#1	62	72	59
#2	81	68	55
#3	59	75	62
#4	72	65	52
#5	68	71	58
#6	75	69	56
#7	65	76	63
#8	80	64	51
#9	60	80	67
#10	78	60	47
#11	62	73	60
#12	70	67	54
```
分散
```python
x = np.var(df)
print(round(x, 2))

# ch    58.15
# pe    26.92
# wi    26.92
# dtype: float64
```
標準偏差
```python
y = np.std(df)
print(round(y,2))

# ch    7.63
# pe    5.19
# wi    5.19
# dtype: float64
```
# 信頼区間
```python
n = 500 # サンプルサイズ
ud = 60 #　不偏分散
se = math.sqrt(ud/n)

bottom, up = stats.norm.interval(alpha=0.95, loc=65, scale=se)
print('95%信頼区間は {:.2f} < x < {:.2f}'.format(bottom, up))
bottom1, up1 = stats.norm.interval(alpha=0.99, loc=65, scale=se)
print('99%信頼区間は {:.2f} < x < {:.2f}'.format(bottom1, up1))

# 95%信頼区間は 64.32 < x < 65.68
# 99%信頼区間は 64.11 < x < 65.89
```
# t検定
```python
ch = pd.Series( [7, 8, 10, 5, 8, 7, 9, 5, 6, 9, 10, 6, 7, 8, 7, 9, 10, 6])
pe = pd.Series( [9, 9, 6, 10, 9, 8, 10, 7, 9, 10, 6, 8, 9, 9, 10, 7, 8, 8, 10, 9])

print(f'桜組の平均点 = {ch.mean():.2f}')
print(f'桃組の平均点 = {pe.mean():.2f}')
print(f'2群の平均点 = {(abs(ch.mean()-pe.mean())):.2f}')

# 桜組の平均点 = 7.61
# 桃組の平均点 = 8.55
# 2群の平均の差 = 0.94

t, p = stats.ttest_ind(pe, ch, equal_var=True)
MU = abs(ch.mean()-pe.mean())
SE = MU/t
DF = len(ch)+len(pe)-2
CI = stats.t.interval( alpha=0.99, loc=MU, scale=SE, df=DF)

print(f'p値 = {p:.3f}')
print(f't値 = {t:.2f}')
print(f'自由度は = {DF}')
print(f'平均値の差 = {MU:.2f}')
print(f'差の標準誤差 = {SE:.2f}')
print(f'平均値の差の99％信頼区間 = [{CI[0]:.2f},{CI[1]:.2f}]')

# p値 = 0.056
# t値 = 1.97
# 自由度は = 36
# 平均値の差 = 0.94
# 差の標準誤差 = 0.48
# 平均値の差の99％信頼区間 = [-0.36,2.23]
```
## t検定(対応あり)




