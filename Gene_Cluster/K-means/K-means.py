#K-means算法

import numpy as np
import matplotlib.pyplot as plt
import PCA as P
import GetData as GD
import operator
from sklearn.cluster import KMeans
from sklearn import metrics

random_state = 170

X = P.PCA_sf(GD.get_gene_matrix())
Evaluation = []

for i in range(2,6):
    y_pred = KMeans(n_clusters=i, random_state=random_state).fit_predict(X)
    No = '22' + str(i-1)
    plt.subplot(No)
    plt.scatter(X[:,0] , X[: , 1], c=y_pred)
    plt.title("K-means algorithm after PCA %d" % (i-1))
    Evaluation.append(metrics.calinski_harabasz_score(X, y_pred))
plt.savefig('.\outpic2\GeneFamPAV_K-means.png')   #保存图片
#plt.savefig('.\outpic2\GeneAV_K-means.png')   #保存图片
plt.show()

#选取最优的聚类个数及评估数值
max_index, max_number = max(enumerate(Evaluation), key=operator.itemgetter(1))
print((max_index+2,max_number))
print(Evaluation)