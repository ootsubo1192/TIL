# 統計の基礎

推測統計：母集団の割合や平均から推論する(統計学のメイン)
記述統計：母集団から一部のデータを取り出し(標本)、分析する

# 平均

算術平均

```python
import numpy as np
x = [1, 2, 3, 4, 5]
np.mean(x)
```

$$
\bar{x} = \frac{1}{n}\sum_{i=1}^{n}x_i
$$

幾何平均：データが比率の場合

```python
from scipy import stats
x = stats.gmean(y_list)
```

$$
m_g = \sqrt[n]{{x_1}{x_2}{x_3}\cdots{x_n}}
$$

調和平均：往復したときの平均時速など

```python
form scipy import stats
x = stats.hmean(y_list)
```

$$
\begin{align}
m_h &=\frac{1}{\frac{1}{n}(\frac{1}{x_1}+\frac{1}{x_2}+\cdots+\frac{1}{x_n})}\\
&=\frac{1}{\frac{1}{n}\sum_{i=1}^{n}(\frac{1}{x_n})}
\end{align}
$$

算術平均からの差の合計は常に0になる
ここから平均につながっていく