### Round 1
**1. 拟合所需的初始参数配置文件**

- results/nosed/s1/obj13347_s1.lyric

```bash 
galfits obj13347_s1.lyric --workplace results/nosed/s1 --num_steps 15000 
```

**2. 拟合输出文件名**

- obj13347_s1_nosedimage_fit.png
- obj13347_s1_nosed.gsssummary
- obj13347_s1_nosed.params
- obj13347_s1_nosed.constrain 

**3. 本轮观察到的问题**

- 中心存在致密的核
- 外围存在径向椭圆形状红蓝交替的残差

**4. 采取的动作**

- 添加一个bulge
  - Re: disk 不变，bulge调小一点(0.1)
  - n：disk n = 1; bulge n = 4
  - q: 稍微调大一点bulge的轴比。

**5. 调整理由**

- 问题处描述的正是需要添加一个bulge的特征。
  - Re:bulge 有效半径比disk小。
  - n： 理论模型。
  - q： bulge会比较圆。

### Round 2
**1. 拟合所需的初始参数配置文件**

- results/nosed/s2/obj13347_s2.lyric

```bash
galfits obj13347_s2.lyric --workplace results/nosed/s2 --num_steps 15000 
```
  
**2. 拟合输出文件名**

- obj13347_s2_nosedimage_fit.png
- obj13347_s2_nosed.gsssummary
- obj13347_s2_nosed.params
- obj13347_s2_nosed.constrain 

**3. 本轮观察到的问题**

- 外围残差基本被拟合完
- 出现旋臂结构

**4. 采取的动作**

- 认为nosed拟合完毕

**5. 调整理由**

- spiral arm暂时不考虑

### Round 3 

**1. 拟合所需的初始参数配置文件**

- mass_guess/total/13347_total_pure_sed.lyric

(运行python guess_mass.py 得到mockdata 和 lyricfile)

```bash 
galfits 13347_total_pure_sed.lyric --workplace results --num_steps 20000 --prior obj13347.prior 
```

**2. 拟合输出文件名**

- 13347SED_model.png
- 13347.gsssummary
- 13347.params
- 13347.constrain 

**3. 本轮观察到的问题**

- sed 图上黑点和红点没有大的offset

**4. 采取的动作**

- 认为disk+bulge 的总质量为此步测量得到的质量，各自的质量初始值估计位总质量-0.3dex， 各自的f_cont和Av是此步测量的Av
- 固定几何参数先拟合sed参数

**5. 调整理由**

- pure sed的测量结果理解为disk和bulge各物理量的平均。
- 减少拟合的自由度

### Round 4

**1. 拟合所需的初始参数配置文件**

- results/sed/s2_ES_fix/obj13347_s2_ES.lyric

```bash 
galfits obj13347_s2_ES.lyric --workplace results/sed/s2_ES_fix --fit_method ES --num_generations 10000 --popsize 20
```

**2. 拟合输出文件名**

- obj13347_s2_sed_ES_fiximage_fit.png
- obj13347_s2_sed_ES_fix.gsssummary
- obj13347_s2_sed_ES_fix.params
- obj13347_s2_sed_ES_fix.constrain 
- obj13347_s2_sed_ES_fixSED_model.png


**3. 本轮观察到的问题**

- 残差图相对nosed变差
- 有明显的旋臂特征

**4. 采取的动作**

- 更新mass和sed参数。
- free几何参数，并对disk做扰动（将n调成1）

**5. 调整理由**

- 正常更新
- 因为如果直接拟合，disk的参数输入和输出一样。。改了n之后能拟合好


### Round 5
**1. 拟合所需的初始参数配置文件**

- results/sed/s2_opt/obj13347_s2_sed_opt.gssummary

**2. 拟合输出文件名**

- obj13347_s2_sed_opt_1image_fit.png
- obj13347_s2_sed_opt_1.gsssummary
- obj13347_s2_sed_opt_1.params
- obj13347_s2_sed_opt_1.constrain 
- obj13347_s2_sed_opt_1SED_model.png


**3. 本轮观察到的问题**

- chiq降低，残差图变好。

**4. 采取的动作**

- finish

**5. 调整理由**

- 物理参数合理，也没有触碰到boundary。