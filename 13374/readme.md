### Round 1
**1. 拟合所需的初始参数配置文件**

- results/nosed/s1/obj13374_s1.lyric

```bash 
galfits obj13374_s1.lyric --workplace results/nosed/s1 --num_steps 15000
```

**2. 拟合输出文件名**

- obj13374_s1image_fit.png
- obj13374_s1.gsssummary
- obj13374_s1.params
- obj13374_s1.constrain 


**3. 本轮观察到的问题**

- 短波外围存在延展辐射

**4. 采取的动作**

- 添加一个bulge

**5. 调整理由**

- bulge 是sersic 成分，和初始的disk一起可以拟合更延展辐射

### Round 2
**1. 拟合所需的初始参数配置文件**

- results/nosed/s2/obj13374_s2.lyric
```bash 
galfits obj13374_s2.lyric --workplace results/nosed/s2/ --num_steps 20000 
```

**2. 拟合输出文件名**


- obj13374_s2image_fit.png
- obj13374_s2.gsssummary
- obj13374_s2.params
- obj13374_s2.constrain 

**3. 本轮观察到的问题**

- 外围延展辐射被拟合完毕

**4. 采取的动作**

- 认为nosed 拟合完成。进行下一步sed拟合

**5. 调整理由**

- xxx

### Round 3

**1. 拟合所需的初始参数配置文件**

- mass_guess/total/13374_total_pure_sed.lyric
```bash 
galfits 13374_total_pure_sed.lyric --workplace mass_guess/total/results --num_steps 20000 --prior obj13374.prior
```
**2. 拟合输出文件名**

- 13374image_fit.png
- 13374SED_model.png
- 13374.gsssummary
- 13374.params
- 13374.constrain  

**3. 本轮观察到的问题**

- sed模型点和数据点无明显偏差。

**4. 采取的动作**

- mass: disk+bulge的总质量是best value, 初始值各设置成-0.3dex 
- f_cont/Av 设置成best fit_value.
- fix geometry参数

**5. 调整理由**

- 这里测量的是总的流量，所以认为是disk和bulgesed性质的平均。
- 减少自由度方便拟合

### Round 4
**1. 拟合所需的初始参数配置文件**

- results/sed/s2_ES_fix/obj13374_s2.lyric

```bash 
galfits obj13374_s2.lyric --workplace results/sed/s2_ES_fix --fit_method ES --num_generations 10000 --popsize 10 --prior obj13374.prior 
```

**2. 拟合输出文件名**

- obj13374_s2_fix_sed_ESimage_fit.png
- obj13374_s2_fix_sed_ESSED_model.png
- obj13374_s2_fix_sed_ES.gsssummary
- obj13374_s2_fix_sed_ES.params
- obj13374_s2_fix_sed_ES.constrain 

**3. 本轮观察到的问题**

- 残差相比于nosed变差

**4. 采取的动作**

- 更新参数，并做optmizer拟合

**5. 调整理由**

- 直接optimizer不容易收敛，可以先做ES垫一步。


### Round 5
**1. 拟合所需的初始参数配置文件**
- results/sed/s2_opt_fix/obj13374_s2.lyric

```bash 
galfits  obj13374_s2.lyric --workplace results/sed/s2_opt_fix --num_steps 20000 --prior obj13374.prior 
```

**2. 拟合输出文件名**

- obj13374_s2_fix_sed_optimage_fit.png
- obj13374_s2_fix_sed_opt.gsssummary
- obj13374_s2_fix_sed_opt.params
- obj13374_s2_fix_sed_opt.constrain 
- obj13374_s2_fix_sed_optSED_model.png

**3. 本轮观察到的问题**

- 残差相对前一步下降。

**4. 采取的动作**

- free geometry参数

**5. 调整理由**

- 残差下降
- gssummary里面参数正常变化，未触碰到边界。


### Round 6
**1. 拟合所需的初始参数配置文件**

- results/sed/s2_opt/obj13374_s2.lyric

```bash 
galfits  obj13374_s2.lyric --workplace results/sed/s2_opt --num_steps 20000 --prior obj13374.prior 
```

**2. 拟合输出文件名**

- obj13374_s2_fix_sed_optimage_fit.png
- obj13374_s2_fix_sed_optSED_model.png
- obj13374_s2_fix_sed_opt.gsssummary
- obj13374_s2_fix_sed_opt.params
- obj13374_s2_fix_sed_opt.constrain 

**3. 本轮观察到的问题**

- 参数合理，没碰到边界。

**4. 采取的动作**

- finish

**5. 调整理由**

