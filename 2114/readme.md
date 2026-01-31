### Round 1

**1. 拟合所需的初始参数配置文件**
- obj2114_s1.lyric 

```bash
galfits obj2114_s1.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 20
```

**2. 拟合输出文件名**

- obj2114_s1_nosed_1image_fit.png
- obj2114_s1_nosed_1.gsssummary
- obj2114_s1_nosed_1.params
- obj2114_s1_nosed_1.constrain 

**3. 本轮观察到的问题**

- 图像残差属于竖直方向偏蓝，水平方向偏红

**4. 采取的动作**

- 添加一个bar, 固定n=0.5(通常用来描述bar)的模型。   
  - 中心设置成和disk一致的估计，半径r_e设置较小(0.15),轴比设置0.3方向角，
- 修改disk参数：r_e变大(0.38)，重制并放大方向角的范围([-180,180]),轴比设置变大（0.6） 

**5. 调整理由**

- 存在竖直方向的过度拟合而水平方向没有被拟合，说明disk被很强的竖直方向特征带走，从cut image上面也可以看出有bar的特征。
  - 中心假设同一个星系有着相近的中心，半径相比与disk肯定会比较小，轴比因为是棒状结构，肯定会比较小。
- disk：r_e因为中心多了一个bar成分，所以半光半径应该会变大，第一次和GalfitX给出的初始值会受到bar的影响，所以重制并扩大范围比较合适；轴比同理也应稍微变大。

### Round 2
**1. 拟合所需的初始参数配置文件**

- obj2114_s2_dbar.lyric

```bash
galfits obj2114_s2_dbar.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 15
```

**2. 拟合输出文件名**

- obj2114_s2_dbar_nosed_1image_fit.png
- obj2114_s2_dbar_nosed_1.gsssummary
- obj2114_s2_dbar_nosed_1.params
- obj2114_s2_dbar_nosed_1.constrain 

**3. 本轮观察到的问题**

- 观察到整体轮廓大体拟合完成，无明显延展成分。
- 中心出现一个核状区域，说明存在agn或者compact bulge, 可以尝试添加AGN 和Bulge。
- 出现旋臂结构

**4. 采取的动作**

- 添加一个agn或者bulge
- 暂时不管旋臂

**5. 调整理由**

- 旋臂对于质量和半径的测量影响不大。

### Round 3
**1. 拟合所需的初始参数配置文件**

- obj2114_s3_dbdbar.lyric 

```bash
galfits obj2114_s3_dbdbar.lyric  --workplace --fit_method ES --num_generations 10000 --popsize 15
```

**2. 拟合输出文件名**

- obj2114_s3_bdbar_nosed_1image_fit.png
- obj2114_s3_bdbar_nosed_1.gsssummary
- obj2114_s3_bdbar_nosed_1.params
- obj2114_s3_bdbar_nosed_1.constrain 

**3. 本轮观察到的问题**

- 看见中间可以一定程度上被拟合(BIC显著降低)，不过观察到轴比非常小，我认为是收到了旋臂的影响，不过这没什么办法。

**4. 采取的动作**

- 无

**5. 调整理由**

- 这一步是为了给sed fitting 寻找成分的几何参数.

### Round 4
**1. 拟合所需的初始参数配置文件**

- obj2114_s2_dbar_agn.lyric 

```bash
galfits obj2114_s2_dbar_agn.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 15
```

**2. 拟合输出文件名**

- obj2114_s2_dbar_agn_nosed_1image_fit.png
- obj2114_s2_dbar_agn_nosed_1.gsssummary
- obj2114_s2_dbar_agn_nosed_1.params
- obj2114_s2_dbar_agn_nosed_1.constrain 

**3. 本轮观察到的问题**

- 中心的成分只有很小一部分被覆盖，

**4. 采取的动作**

- 放弃agn

**5. 调整理由**

- 说明是AGN的概率不大，这里认为用更延展的bulge 去拟合。

### Round 6
**1. 拟合所需的初始参数配置文件**

- obj2114_s1_sed.lyric 

```bash
galfits obj2114_s1_sed.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 15
```

**2. 拟合输出文件名**

- obj2114_s1_sed_1image_fit.png
- obj2114_s1_sed_1SED_model.png
- obj2114_s1_sed_1.gsssummary
- obj2114_s1_sed_1.params
- obj2114_s1_sed_1.constrain 


**3. 本轮观察到的问题**

- 无

**4. 采取的动作**

- 星系总质量在10**9.5 solar mass量级

**5. 调整理由**

- 因为星系的亮度和质量相关，用单成分拟合可以获得基本的亮度，进而基本的质量信息。
  - 之后这一步和下一步会变成从多成分 pure sed fitting 进行测光点的光谱拟合来确定不同成分的质量。


### Round 7
**1. 拟合所需的初始参数配置文件**

- obj2114_s2_dbar_sed.lyric
```bash 
galfits obj2114_s2_dbar_sed.lyric --workplace results --fit_method ES --num_generations 10000 --popsize 15
```

**2. 拟合输出文件名**

- obj2114_s2_dbar_sed_1image_fit.png
- obj2114_s2_dbar_sed_1SED_model.png
- obj2114_s2_dbar_sed_1.gsssummary
- obj2114_s2_dbar_sed_1.params
- obj2114_s2_dbar_sed_1.constrain 

**3. 本轮观察到的问题**

- 拟合结果和双成分nosed 拟合相似，说明还行。 中心仍然有亮源。
- disk的质量在9.5左右， bar的质量在9左右，和round 6的结论吻合

**4. 采取的动作**

- 添加一个compact bulge 成分

**5. 调整理由**

- round 5,6的对比结果


### Round 8
**1. 拟合所需的初始参数配置文件**

- obj2114_s3_dbdbar_sed.lyric

```bash
galfits obj2114_s3_dbdbar_sed.lyric --workplace results --fit_method ES --num_generations 20000 --popsize 15
```

**2. 拟合输出文件名**


- obj2114_s3_bdbar_sed_1image_fit.png
- obj2114_s3_bdbar_sed_1SED_model.png
- obj2114_s3_bdbar_sed_1.gsssummary
- obj2114_s3_bdbar_sed_1.params
- obj2114_s3_bdbar_sed_1.constrain 

**3. 本轮观察到的问题**

- 残差基本消除，和nosed fitting 残差图相差不大，chi^2略大可以理解，认为拟合完毕.


**4. 采取的动作**

**5. 调整理由**

