#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'Administrator'


from scipy.optimize import fsolve
from matplotlib.font_manager import FontProperties
from matplotlib import pyplot
import matplotlib

import sys


Area = 163.6       #56m3内容器外表面积 m2
Qgls1 = 33        #前支撑玻璃钢漏热
Qgls2 = 37.1           #后支撑玻璃钢漏热
Qpip = 2.93            #管路漏热

sigma = 5.67*10**(-8)   # 黑体辐射常数 w/m2.K4
epsilon_b = 0.1         # 铝箔表面发射率
epsilon_s = 0.8         # 不锈钢表面发射率

A = 0.016               # 经验常数
N = 0.03                # N、k材料稀松程度
k = 1
lamda = 0.04            # 绝热纸热导率
delta_x = 0.0005        # 绝热纸厚度 m

alpha = 0.9             # 综合热适应系数
K = 1.2001              # 空气k值
P = 10**(-3)            # 层间气体压强

A0 = sigma / (1/epsilon_b + 1/epsilon_s -1)     # 第一层：壳体与铝箔辐射
A1 = sigma / (1/epsilon_b + 1/epsilon_b -1)     # 铝箔与铝箔辐射
A2 = A * N ** k * lamda / delta_x               # 固体导热
A3 = alpha * K * P                              # 气体导热

# print A0, A1, A2, A3

def solver(_x0, _q0):
    def func(_x):
        _x1 = float(_x)
        return A1 * (_x0**4 - _x1**4) + (A2 + A3) * (_x0 - _x) - _q0
    x = fsolve(func, _x0-0.01)
    return x[0]

class Multilayer(object):
    def __init__(self, num):
        self.tlayer0 = 333           # 外壳温度
        self.tlayer1 = 332.9         # 外壳温度
        self.tlayern = 20            # 内壁温度
        self.qrad = []               # 辐射传热
        self.qsld = []               # 固体传热
        self.qgas = []               # 气体传热
        self.qtot = []               # 总传热
        self.tttt = []               # 各层温度
        self.solver_count = 0        # 计算次数
        self.layer = num             # 层数
        self.q0 = 0                  # 热流密度
        self.lamda = 0               # 传热系数
        self.txt = ''                # 打印
        self.txt2 = ''               # 打印
        self.Qmti = 0                # 绝热层漏热量
        self.Qtot = 0                # 总漏热量
        self.tht1 = 0                # LNG日蒸发率
        self.tht2 = 0                # LN2日蒸发率

        layer_n = num + 1            #
        for ii in range(layer_n):
                if ii == 0:
                    self.q0 = A0 * (self.tlayer0**4 - self.tlayer1**4) + A3 * (self.tlayer0 - self.tlayer1)
                    self.tttt.append(self.tlayer1)
                if ii >= 1:
                    self.tttt.append(solver(self.tttt[ii-1], self.q0))
                    self.solver_count += 1

        while self.tttt[layer_n - 1] > self.tlayern:
            self.tlayer1 -= 0.05
            for ii in range(layer_n):
                if ii == 0:
                    self.q0 = A0 * (self.tlayer0**4 - self.tlayer1**4) + A3 * (self.tlayer0 - self.tlayer1)
                    self.tttt[ii] = self.tlayer1
                if ii >= 1:
                    self.tttt[ii] = solver(self.tttt[ii-1], self.q0)
                    self.solver_count += 1

        while self.tttt[layer_n - 1] < self.tlayern:
            self.tlayer1 += 0.0001
            for ii in range(layer_n):
                if ii == 0:
                    self.q0 = A0 * (self.tlayer0**4 - self.tlayer1**4) + A3 * (self.tlayer0 - self.tlayer1)
                    self.tttt[ii] = self.tlayer1
                if ii >= 1:
                    self.tttt[ii] = solver(self.tttt[ii-1], self.q0)
                    self.solver_count += 1

        self.qrad.append(A0 * (self.tlayer0**4 - self.tttt[0]**4))
        self.qsld.append(0 * (self.tlayer0 - self.tttt[0]))
        self.qgas.append(A3 * (self.tlayer0 - self.tttt[0]))
        self.qtot.append(self.qrad[0] + self.qsld[0] + self.qgas[0])

        for jj in range(layer_n - 1):
            self.qrad.append(float(A1 * (self.tttt[jj]**4 - self.tttt[jj + 1]**4)))
            self.qsld.append(float(A2 * (self.tttt[jj] - self.tttt[jj + 1])))
            self.qgas.append(float(A3 * (self.tttt[jj] - self.tttt[jj + 1])))
            self.qtot.append(float(self.qrad[0] + self.qsld[0] + self.qgas[0]))

        self.lamda = self.q0 * (layer_n) * delta_x / (self.tlayer0-self.tlayern)
        self.Qmti = self.q0 * Area
        self.Qtot = self.Qmti + Qgls1 + Qgls2 + Qpip
        self.tht1 = 24 * 3600 * self.Qtot / 100 / 70 / 460.5 /1000 * 100
        self.tht2 = 0

    def plt(self):
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        pyplot.figure(1, figsize=(6, 5))
        pyplot.xlabel(u'层数')
        pyplot.ylabel(u'温度(k)')
        pyplot.axis([0, self.layer, 0, self.tlayer0 * 1.1])
        pyplot.plot(range(self.layer + 1), self.tttt)

        pyplot.figure(2, figsize=(6, 5))
        pyplot.xlabel(u'层数')
        pyplot.ylabel(u'热流密度(w/m.k)')
        pyplot.plot(range(self.layer + 1), self.qrad, '--', label=u'辐射', linewidth=1.5)
        pyplot.plot(range(self.layer + 1), self.qsld, '-.', label=u'固体', linewidth=1.5)
        pyplot.plot(range(self.layer + 1), self.qgas, ':', label=u'气体', linewidth=1.5)
        # pyplot.plot(range(self.layer + 1), self.qtot)
        pyplot.legend(loc='upper')

        pyplot.figure(3, figsize=(6, 5))
        pyplot.pie([self.Qmti, Qgls1+Qgls2, Qpip],
                   labels=[u'绝热层', u'支撑', u'管道'],
                   colors=['0.90', '0.85', '0.80'],
                   autopct='%2.2f%%',
                   pctdistance=0.6, startangle=180,
                   shadow=False, labeldistance=1.1)

        pyplot.show()

    def des(self):
        self.txt = '===================================================='
        self.txt += '\n绝热层数为 %s 层时，热流密度为：\n    q0 = %s W/m2 \n' % (self.layer, self.q0)
        self.txt += '绝热层导热系数为：\n    lamda = %s W/(m.k) \n' % (self.lamda)
        self.txt += '        绝热层       前支撑       后支撑       管  路      总漏热\n'
        self.txt += '漏热量   %6.3f      %6.3f      %6.3f      %6.3f      %6.3f \n' \
                    % (self.Qmti, Qgls1, Qgls2, Qpip, self.Qtot)
        self.txt += '比  例  %5.3f%%     %5.3f%%     %5.3f%%      %5.3f%%   \n' \
                    % (self.Qmti/self.Qtot*100, Qgls1/self.Qtot*100, Qgls2/self.Qtot*100, Qpip/self.Qtot*100)

        self.txt += 'LH2日蒸发率为：\n    theta1 = %5.3f%%  \n' % (self.tht1)

    def prt(self):
        self.des()
        print self.txt

    def des2(self):
        self.des()
        self.txt += '\n层数     温度(K)     辐射导热     固体导热     气体导热     总导热(W/m2)\n'
        self.txt += '%2d    %8.5f    %8.5f    %8.5f    %8.5f    %8.5f \n' \
                            % (0, self.tlayer0, self.qrad[0], self.qsld[0], self.qgas[0], self.qtot[0])
        for kk in range(self.layer):
            self.txt += '%2d    %8.5f    %8.5f    %8.5f    %8.5f    %8.5f \n' \
                        % (kk+1, self.tttt[kk], self.qrad[kk+1], self.qsld[kk+1], self.qgas[kk+1], self.qtot[kk+1])

        self.txt += '%2d    %8.5f \n' % (self.layer+1, self.tttt[self.layer])
    def prt2(self):
        self.des2()
        print self.txt

    def sav(self):
        self.des2()
        f = file(sys.argv[0] + '.txt', 'w')
        f.write(self.txt)
        f.close()

    def sav2(self):
        self.des2()
        f = file(sys.argv[0] + '.txt', 'a')
        f.write(self.txt)
        f.close()



ml80 = Multilayer(80)
ml80.prt()
ml80.sav()



