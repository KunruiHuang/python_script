from sklearn.metrics import confusion_matrix
import numpy as np
"""
分类任务混淆矩阵函数计算
Args:
    ground_truth:分类任务的真值标签
    predict:分类任务的预测结果

Returns:
    cm:混淆矩阵
    precision:每个类别的查准率
    recall:每个类别的查全率
"""
#预测与真值的标签
# 获取混淆矩阵
def classifyEvaluation(y_true,y_pred): 
    cm = confusion_matrix(y_true, y_pred)
    FP = cm.sum(axis=0) - np.diag(cm) 
    FN = cm.sum(axis=1) - np.diag(cm)
    TP = np.diag(cm)
    TN = cm.sum() - (FP + FN + TP)
    precision = TP / (TP+FP)  # 查准率
    recall = TP / (TP+FN)  # 查全率
    return cm,precision,recall

if __name__ == '__main__':
    y_true = np.array([0,1,2,3])
    y_pred = np.array([0,1,0,3])
    cm,precision,recall = classifyEvaluation(y_true,y_pred)
    print("cm")
    print(cm)
    # print("precision")
    # print(precision)
    # print("recall")
    # print(recall)