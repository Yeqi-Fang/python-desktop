import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
a = np.array([
    [37, 10, 0, 0],
    [9, 20, 2, 0],
    [1, 3, 9, 1],
    [0, 0, 2, 6]
])

# plot confusion matrix
sns.heatmap(a, annot=True)
# plt.show()
plt.savefig('confusion_matrix.png', dpi=600)
