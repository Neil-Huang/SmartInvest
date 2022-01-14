import numpy as np

#一维
a = np.array([1,2,3])
print(a)

#二维
a2 = np.array([[1,2],[3,4]])
print(a2)

#三维
a3 = np.array([[
                [0,1,2],
                [4,5,6],
                [7,8,9]
               ]])

#三维
a4 = np.array([[[
                 [0,1,2],
                 [4,5,6],
                 [7,8,9],
                 [7,8,9]
               ]]])
print(a4)

print(a.ndim)
print(a2.ndim)
print(a3.ndim)
print(a4.ndim)
print("-------------")
print(a.shape)
print(a2.shape)
print(a3.shape)
print(a4.shape)

al = np.linspace(1,10,10)
print(al)

aa = np.logspace(0,9,10,base=2)
print(aa)

new_a = al[slice(1,8,2)]

print("-------------")
a=np.arange(10)
print(a)
print(a[2:5])
print(a[4:])
print(a[...])


def cal_sun_height(h, l, A):
    """
    计算光照问题
    公式: H = h - l * tan(A)
    H:遮挡高度
    h:对面楼高
    l:楼间距
    A:太阳高度角  在线工具 https://www.osgeo.cn/app/s1904

    冬至日太阳高度角= 90 -（广州纬度+23.26）

    numpy 默认情况下角度以弧度而非角度表示,为此可使用 numpy.radians() 函数可使用角度为度的三角函数
    """
    H = h - l * np.tan(np.radians(A))
    return H


print(np.tan(np.radians(47.97)))
H = cal_sun_height(97, 66, 47.97)
print("高度:{}".format(H))
