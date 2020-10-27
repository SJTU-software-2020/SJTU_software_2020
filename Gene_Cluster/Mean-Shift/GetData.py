import numpy as np


def get_gene_matrix():
    #file_name = ".\DataFile\TestData.txt"       #这里测试文件数据来源于GeneFamPAV.matrix.txt（基因家族的PAV）
    #file_name = ".\DataFile\GenePAV.matrix.txt"
    file_name = ".\DataFile\GeneFamPAV.matrix.txt"
    f = open(file_name,'r')

    sample_num = len(f.readline().split()) - 1  #读一共有多少个样本(列数减一)

    #以矩阵形式读取txt文件
    data = np.loadtxt(file_name,
                      #skiprows= gene_num - n,      #忽略前gene_num - n行
                      skiprows=1,                   #忽略第一行
                      dtype=np.int,
                      usecols=(range(1, sample_num+1))
                      )
    gene_num = len(data)            #读一共有多少基因或基因家族（行数减一）,

    #function1
    #gene_matrix = data.T * 1000     #给的数据是个体为列，基因或基因家族为行。所以需要转置
    #gene_matrix = np.maximum(gene_matrix, 1)

    #function2
    gene_matrix = data.T   # 给的数据是个体为列，基因或基因家族为行。所以需要转置

    #print("data is:", data)
    #print("gene_matrix is:", gene_matrix)
    #print(sample_num)
    #print(gene_num)

    #gene_matrix: 选取的矩阵 453x100
    #sample_num：样本个数，向量个数
    #gene_num：基因个数，向量维数
    return gene_matrix
    #return gene_matrix, sample_num, gen_num

get_gene_matrix()
