# 統計学がわかる

```python
import pandas as pd
import numpy as np 
from scipy import stats
import math
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