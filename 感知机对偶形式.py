import numpy as np
import time


class ganzhiji(object):
    def __init__(self):
        self.datearr = []
        self.labelarr = []
        self.accr = 0
        self.quality = []
        self.a = []
        self.G = np.mat([0])
        self.b = 0

    def loaddate(self,path):
        with open(path,encoding='UTF-8-sig') as file:
            for line in file:
                curline = line.strip().split(',')
                # print(a.quality)
                if len(self.quality) == 0:
                    for i  in curline:
                        self.quality.append(i)

                else:
                    if int(curline[0]) >= 5:
                        self.labelarr.append(1.0)
                    else:
                        self.labelarr.append(-1.0)

                    self.datearr.append([float(i) for i in curline[1:]])
        N = len(self.datearr)
        datearr = np.mat(self.datearr)
        G = np.mat(np.zeros((N,N)))
        for i in range(N):
            for j in range(N):
                G[i,j] = np.mat(datearr[i])*np.mat(datearr[j]).T

        self.G = G




    def train(self):
        w = np.zeros(len(self.datearr[0]))

        b = 0.0
        h = 0.0001
        datearr = np.mat(self.datearr)
        labelarr = self.labelarr
        a = np.zeros((len(self.datearr)))
        print(self.G)
        for i in range(50):
            print('已完成 %d/50' % i)
            for j in range(len(self.datearr)):
                xi = datearr[j]
                yi = labelarr[j]
                sum = 0
                for k in range(len(self.datearr)):
                    sum += self.G[j,k]*a[k]*labelarr[k]

                sum=(sum+b)*yi
                if  sum <= 0:
                    a[j] = a[j] +h
                    b = b + h * yi
        self.a = a
        self.b = b


    def test(self):
        right = 0

        for i in range(len(self.datearr)):
            xi = np.mat(self.datearr[i])
            yi = self.labelarr[i]

            sum = 0
            for k in range(len(self.datearr)):
                sum += self.G[i, k] * self.a[k] * self.labelarr[k]

            sum = (sum + self.b) * yi


            if sum > 0:
                right += 1


        self.accr = float(right)/float(len(self.labelarr))







if __name__ == '__main__':
    a = ganzhiji()
    start = time.time()
    a.loaddate('redwine_train.csv')
    a.train()
    a.labelarr.clear()
    a.datearr.clear()
    a.loaddate('redwine_test.csv')
    a.test()
    print('-----------------------------')
    print('准确率:',a.accr)

    print('用时：',time.time()-start)


