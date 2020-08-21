import numpy as np
import time

class KNN(object):
    def __init__(self):
        self.datearr = []
        self.labelarr = []
        self.quality = []




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

    # def build_kdtree(self):
    #     var = []
    #     m = len(self.datearr[0])
    #
    #     for i in range(m):
    #         temp = []
    #         for j in range(len(self.datearr)):
    #             temp.append(self.datearr[j][i])
    #         vari = np.var(temp)
    #         var.append((vari,i))

    def test(self,predata,prelabel):
        right = 0

        for j in range(len(self.datearr)):
            print(j,'/',len(self.datearr))
            dictlist = []
            for i in range(len(predata)):
                t = np.mat(predata[i])-np.mat(self.datearr[j])
                t =t*t.T
                dictlist.append((t,i))
            dictlist.sort()
            label = 0
            for k in dictlist[-10:-1]:
                label += k[1]

            if label > 0:
                y = 1
            else:
                y = -1
            if y == self.labelarr[j]:
                right+=1

        return float(right)/float(len(self.datearr))








if __name__ =='__main__':
    start = time.time()
    a = KNN()

    a.loaddate('redwine_train.csv')

    predata = a.datearr
    prelabel = a.labelarr
    a.loaddate('redwine_test.csv')

    print('准确率:',a.test(predata,prelabel))
    print('耗时：',time.time()-start)
