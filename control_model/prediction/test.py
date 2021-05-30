#coding:utf-8
import numpy as np
from keras import models, optimizers, layers
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

train_x = []
train_y = []  # 0:Init 1:CPU 2:GPU

test_x = []
test_y = []  # as same as above

SELECT_DEVICE = 2
TIME_PART = 10


def one_hot(labels, dimension=TIME_PART + 1):
    result = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        result[i, label] = 1.
    return result


def loadData():
    data = []
    maxi = [0, 0, 0, 0, 0, 0]
    x_num = 3
    y_num = 3
    cnt = 0
    global train_x, train_y, test_x, test_y

    for i in range(y_num):
        train_y.append([])
        test_y.append([])

    with open("Runtime Data.txt", "r") as file:  # extract  info from txt
        for line in file:
            line = line[0:-1]
            line = line.split(" ")
            for item in range(len(line)): line[item] = float(line[item])
            data.append(line)

            if cnt % 5 != 0:
                train_x.append(line[0:x_num])
                for i in range(y_num):
                    train_y[i].append(line[x_num + i])
            else:
                test_x.append(line[0:x_num])
                for i in range(y_num):
                    test_y[i].append(line[x_num + i])

            for i in range(x_num + y_num):
                maxi[i] = max(maxi[i], line[i])

            cnt += 1

    for i in range(len(train_x)):  # normalization and  tagging
        for j in range(x_num):
            train_x[i][j] /= maxi[j]
            continue
        for j in range(y_num):
            train_y[j][i] = int(train_y[j][i] / maxi[x_num + j] * TIME_PART)

    for i in range(len(test_x)):
        for j in range(x_num):
            test_x[i][j] /= maxi[j]
            continue
        for j in range(y_num):
            test_y[j][i] = int(test_y[j][i] / maxi[x_num + j] * TIME_PART)

    for i in range(y_num):  # list to np
        test_y[i] = one_hot(test_y[i])
        train_y[i] = one_hot(train_y[i])

    train_x = np.array(train_x)
    test_x = np.array(test_x)


loadData()

model = models.Sequential()
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(TIME_PART+1, activation = 'softmax'))
model.compile(optimizer='rmsprop',loss='categorical_crossentropy',metrics=['accuracy'])

history = model.fit(train_x,train_y[SELECT_DEVICE],epochs=100,batch_size=8,validation_data=(test_x,test_y[SELECT_DEVICE]))
print("x_train:")
print(train_x)
print("y_train:")
print(train_y[SELECT_DEVICE])

acc = history.history['accuracy']
val_acc = history.history['val_accuracy']

epochs = range(1,len(acc)+1)
plt.plot(epochs,acc,'bo',label='训练集准确率')
plt.plot(epochs,val_acc,'b',label='测试集准确率')
plt.xlabel('迭代次数(次)', fontdict={'size'   : 16})
plt.ylabel('准确率（%）', fontdict={'size'   : 16})
plt.legend()
plt.show()

predict_result = model.predict(test_x)
epochs = range(1,len(predict_result[0])+1)
print(predict_result)
for i in range(len(test_x)):
    plt.plot(epochs,predict_result[i],'b',label='预测概率')
    for j in range(0,len(test_y[SELECT_DEVICE])):
        if test_y[SELECT_DEVICE][i][j] == 1:
            plt.plot(j+1,predict_result[i][j],'ro',label="实际标签")
    plt.xlabel('标签序号', fontdict={'size'   : 16})
    plt.ylabel('预测概率(%)', fontdict={'size'   : 16})
    plt.legend()
    plt.show()