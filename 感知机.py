import numpy as np
import time


class ganzhiji(object):
    def __init__(self):
        self.datearr = []
        self.labelarr = []
        self.accr = 0
        self.quality = []
        self.w = []
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

    def train(self):
        w = np.zeros(len(self.datearr[0]))
        print(self.quality)
        b = 0.0
        h = 0.0001
        datearr = np.mat(self.datearr)
        labelarr = self.labelarr


        for i in range(50):
            print('已完成 %d/50' % i)
            for j in range(len(self.datearr)):
                xi = datearr[j]
                yi = labelarr[j]

                if  yi*(w*xi.T+b) <= 0:
                    w = w + h * yi * xi
                    b = b + h * yi
        self.w = w
        self.b = b


    def test(self):
        right = 0

        for i in range(len(self.datearr)):
            xi = np.mat(self.datearr[i])
            yi = self.labelarr[i]

            if yi*(self.w *xi.T +self.b) > 0:
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


