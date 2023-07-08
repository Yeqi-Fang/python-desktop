import torch
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
y = torch.load(r"D:\multiMedia\Download\y.pt", map_location=torch.device('cpu')).short()
# y_ = torch.load(r"D:\multiMedia\Download\y_hat.pt", map_location=torch.device('cpu'))
y_pred_int = torch.load(r"D:\multiMedia\Download\y_pred_int.pt", map_location=torch.device('cpu'))
print(y.shape)
print(y.min(), y.max())
# print(y_.shape)
# print(y_.min(), y_.max())
print(y_pred_int.shape)
print(y_pred_int.min(), y_pred_int.max())


mat = confusion_matrix(y, y_pred_int)
sns.heatmap(mat, annot=True)
# plt.show()

