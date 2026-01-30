#### 6978  (拟合对象)

### Round 1

**1. 拟合所需的初始参数配置文件**

- obj6978_s1.lyric
  
```bash 
galfits obj6978_s1.lyric --workplace results --num_steps 20000  
```

**2. 拟合输出文件名**

- obj6978_s1_nosed_1image_fit.png
- obj6978_s1_nosed_1.gssummary
- obj6978_s1_nosed_1.params
- obj6978_s1_nosed_1.constrain

**3. 本轮观察到的问题**

- 残差存在椭圆形状径向红蓝交替分布。

**4. 采取的动作** (配置文件具体修改动作)

- 添加延展成分 bulge 
- disk 成分 n 初始设置成1, bulge n 初始设置成4
- disk 的r_e设置成galfitx 的输出（0.25）稍大的数(0.30)， bulge 设置成galfitx输出稍小(0.15)
- PA 两成分一致
- q: 轴比disk 和galfitX输出（0.25）差不多，bulge稍大(0.55) 

**5. 调整理由** (与上述动作一一对应)

- 残差存在椭圆形状径向红蓝交替分布。
- 标准模型disk n = 1， bulge n = 4
- disk 比较平坦/延展， bulge相对来说比较小/紧致
- PA 只是几何结构，所以
- disk 的轴比会偏小，bulge比较偏圆，轴比偏大


### Round 2

**1. 拟合所需的初始参数配置文件**
- obj6978_s2.lyric 
```bash 
galfits obj6978_s2.lyric --workplace results --num_steps 15000
```

**2. 拟合输出文件名**

- obj6978_s2_nosed_1image_fit.png
- obj6978_s2_nosed_1.gssummary
- obj6978_s2_nosed_1.params 
- obj6978_s2_nosed_1.constrain 

**3. 本轮观察到的问题**


- 整体结构已被拟合好，但是出现环状结构

**4. 采取的动作**

- 更新disk 和bulge 的几何参数为s2的输出。
- 尝试添加环状模型ring 来拟合。
  - 注意估计图像上ring的最亮地方和中心的距离

**5. 调整理由**

- 正常数据update。
- 从形状上来讲明显存在环状结构。
  - 对应的参数是P5) r0和P6) sigma 


### Round 3

**1. 拟合所需的初始参数配置文件**
- obj6978_s2r.lyric

```bash 
galfits obj6978_s2r.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 20
```
(亲测ES fitting 方法对于目前的样本源来说表现优于optimizer! 如有optimizer无法拟合，比如某成分参数输出相比于输入参数不变，可以尝试ES)

**2. 拟合输出文件名**

- obj6978_s2r_nosed_2image_fit.png
- obj6978_s2r_nosed_2.gssummary
- obj6978_s2r_nosed_2.params 
- obj6978_s2r_nosed_2.constrain

**3. 本轮观察到的问题**

- 环状结构被拟合去掉。

**4. 采取的动作**

- 认为no sed 拟合基本成功。
- 下一步进行single sersic 的sed fitting来估算整体星系的质量
  
**5. 调整理由**

- 没有明显其他结构的特征。

### Round 4

**1. 拟合所需的初始参数配置文件**

- obj6978_s1_sed.lyric 

```bash
galfits obj6978_s1_sed.lyric  --workplace results --fit_method ES --num_generations 10000 --popsize 20
```

**2. 拟合输出文件名**

- obj6978_s1_sed_3image_fit.png
- obj6978_s1_sed_3.gssummary 
- obj6978_s1_sed_3.params
- obj6978_s1_sed_3.constrain 

**3. 本轮观察到的问题**

- 星系的质量大概在10**10.5 solar mass左右

**4. 采取的动作**

- 下一步星系的多成分总体质量基本在这个水平（后续可能会加一步得到了测光做pure spectrum fitting 来代替这一步。） 
- 添加bulge 和 ring 成分，并且初始值参数设置成no sed fitting best fit value,
- sfr： disk 采用 [-1.75,-1,0,-3,-3,-3]，而bulge 采用[-3,-1.5,-1,-0.5,-3]的设计，ring和bulge 同样。
- 质量: disk 10, bulge 10.5, ring: 9.5

**5. 调整理由**

- 星系的质量和亮度存在正相关关系。
- 正常update
- sfr： 认为disk 星族比较年轻，故P9采用 [-1.75,-1,0,-3,-3,-3]较为年轻的设计，而bulge 星族比较老，采用[-3,-1.5,-1,-0.5,-3]的设计，ring和bulge 同样。
- bulge 我理解会稍微重一点，disk轻一点,ring 是次结构，当然最轻

### Round 5

**1. 拟合所需的初始参数配置文件**

- obj6978_s2r_sed.lyric 

```bash
galfits obj_6978_s2r_sed.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 20 
```

**2. 拟合输出文件名**

- obj6978_s2r_sed_ES_1image_fit.png
- obj6978_s2r_sed_ES_1.gssummary
- obj6978_s2r_sed_ES_1.params 
- obj6978_s2r_sed_ES_1.constrain 

**3. 本轮观察到的问题**

- 结果和image fitting十分接近

**4. 采取的动作**

- 认为是好的拟合，结束。

**5. 调整理由**

- 图像和pure image fitting 接近，很不错的拟合。
