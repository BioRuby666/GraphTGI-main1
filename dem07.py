import torch
import numpy as np
import random


# 1 数据进行计算 eg：求均值 求方差 这个动作叫reduce，可以保持原来的维度，也可以不保持原来的维度
# 2 在2行3列的矩阵中, dim=0 dim=1分布代表的维度数值2和3 自然而然就知道行列了
def dm01_test_calfunc():
    data = torch.randint(0, 10, [2, 3], dtype=torch.float64)
    print(data)
    print('-' * 50)

    # 1. 计算均值
    # mydata2 = data.mean()
    # print('mydata2-->', mydata2, mydata2.shape)
    #
    # print('按照列计算均值', data.mean(dim = 0))  # 按列计算均值
    # print('按照行计算均值', data.mean(dim = 1))  # 按行计算均值
    #
    # print('按照列计算均值 keepdim为True', data.mean( dim=0, keepdim=True ) )  # 按列计算均值
    # print('按照行计算均值 keepdim为True', data.mean( dim=1, keepdim=True ) )  # 按行计算均值

    # 2. 计算总和
    print(data.sum())
    print(data.sum(dim=0))
    print(data.sum(dim=1))
    print('-' * 50)

    # # 3. 计算平方
    # print(data.pow(2))
    # print('-' * 50)
    #
    # # 4. 计算平方根
    # print(data.sqrt())
    # print('-' * 50)
    #
    # # 5. 指数计算, e^n 次方
    # print(data.exp())
    # print('-' * 50)
    #
    # # 6. 对数计算
    # print(data.log())  # 以 e 为底
    # print(data.log2())
    # print(data.log10())


if __name__ == '__main__':
    dm01_test_calfunc()
