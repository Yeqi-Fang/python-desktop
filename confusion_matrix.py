import numpy as np
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
a = np.array([[54, 1], [5, 43]])

# plot confusion matrix
sns.heatmap(a, annot=True)
plt.show()