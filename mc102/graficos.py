import matplotlib.pyplot as plt
import numpy as np

# x = np.linspace(0.1, 2 * np.pi, 41)
# y = np.exp(np.sin(x))

# plt.stem(x, y)
# plt.show()
# ----------------------------------------------------------------
fig, ax = plt.subplots()

colunas = ['Coluna 1', 'Coluna 2', 'Coluna 3', 'Coluna 4']
counts = [7, 100, 28, 54]
bar_labels = ['red', 'blue', '_red', 'orange']
bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

ax.bar(colunas, counts, label=bar_labels, color=bar_colors)

ax.set_ylabel('Texto Lateral')
ax.set_title('Fruit supply by kind and color')
ax.legend(title='LEGENDA')

plt.show()