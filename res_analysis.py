from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import pandas as pd
import csv
import os

curr_dir = os.getcwd()
y_path = os.path.join(curr_dir, 'res_analysis/human.csv')
pred_path = os.path.join(curr_dir, 'data/res_ot_knn.csv')

y = pd.read_csv(y_path, encoding='utf-8')
prd = pd.read_csv(pred_path, encoding='utf-8')

# print(y.head())
# print(prd.head())

print("Des Precision Score -> ",precision_score(prd['DES'], y['DES'])*100)
print("Des Recall Score -> ",recall_score(prd['DES'], y['DES'])*100)
print("Des  F1 Score -> ",f1_score(prd['DES'], y['DES'])*100)

print("Org Precision Score -> ",precision_score(prd['Org'], y['Org'])*100)
print("Org Recall Score -> ",recall_score(prd['Org'], y['Org'])*100)
print("Org  F1 Score -> ",f1_score(prd['Org'], y['Org'])*100)

print("QT Precision Score -> ",precision_score(prd['QT'], y['QT'])*100)
print("QT Recall Score -> ",recall_score(prd['QT'], y['QT'])*100)
print("QT  F1 Score -> ",f1_score(prd['QT'], y['QT'])*100)

print("CW Precision Score -> ",precision_score(prd['CW'], y['CW'])*100)
print("CW Recall Score -> ",recall_score(prd['CW'], y['CW'])*100)
print("CW  F1 Score -> ",f1_score(prd['CW'], y['CW'])*100)

print("RES Precision Score -> ",precision_score(prd['RES'], y['RES'])*100)
print("RES Recall Score -> ",recall_score(prd['RES'], y['RES'])*100)
print("RES  F1 Score -> ",f1_score(prd['RES'], y['RES'])*100)

print("OT Precision Score -> ",precision_score(prd['OT'], y['OT'])*100)
print("OT Recall Score -> ",recall_score(prd['OT'], y['OT'])*100)
print("OT  F1 Score -> ",f1_score(prd['OT'], y['OT'])*100)

print("URL Precision Score -> ",precision_score(prd['URL'], y['URL'])*100)
print("URL Recall Score -> ",recall_score(prd['URL'], y['URL'])*100)
print("URL  F1 Score -> ",f1_score(prd['URL'], y['URL'])*100)

print("C Precision Score -> ",precision_score(prd['C'], y['C'])*100)
print("C Recall Score -> ",recall_score(prd['C'], y['C'])*100)
print("C  F1 Score -> ",f1_score(prd['C'], y['C'])*100)