#主成分分析算法（PCA）样例


from sklearn.decomposition import PCA    #在sklearn中调用PCA机器学习算法
import matplotlib.pyplot as plt
import GetData

#x = GetData.get_gene_matrix()

def PCA_sf(x):
    pca=PCA(n_components=2)                  #定义所需要分析主成分的个数n
    pca.fit(x)                               #对基础数据集进行相关的计算，求取相应的主成分
    #print(pca.components_)                    #输出相应的n个主成分的单位向量方向
    x_reduction=pca.transform(x)                    #进行数据的降维
    x_restore=pca.inverse_transform(x_reduction)  #对降维数据进行相关的恢复工作

    #plt.figure()
    #plt.scatter(x[:,0],x[:,1],color="g")
    #plt.scatter(x_restore[:,0],x_restore[:,1],color="r")
    #plt.scatter(x_reduction[:,0],x_reduction[:,1],color="b")
    #plt.show()
    #print(x_reduction)

    return x_reduction

PCA_sf(GetData.get_gene_matrix())