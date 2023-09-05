
import pandas as pd

# Read the CSV file
#data = pd.read_csv('my_human.csv')
#data = pd.read_csv('my_human_w2v.csv')
data = pd.read_csv('my_human_ot.csv')

# Assuming 'actual_labels' and 'predicted_labels' are the column names
actual_labels = data['OT']
predicted_labels = data['OT_git_w2v']

# Calculate True Positives, False Positives, True Negatives, and False Negatives
TP = ((actual_labels == 1) & (predicted_labels == 1)).sum()
FP = ((actual_labels == 0) & (predicted_labels == 1)).sum()
TN = ((actual_labels == 0) & (predicted_labels == 0)).sum()
FN = ((actual_labels == 1) & (predicted_labels == 0)).sum()

# Calculate Precision and Recall
precision = TP / (TP + FP)
recall = TP / (TP + FN)

print("Precision:", precision)
print("Recall:", recall)