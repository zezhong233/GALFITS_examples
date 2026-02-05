
### Round 1
**1. 拟合所需的初始参数配置文件**

- obj6414_s1.lyric

```bash 
galfits obj6414_s1.lyric --workplace results --num_steps 10000
```

**2. 拟合输出文件名**

- obj6414_s1_nosedimage_fit.png
- obj6414_s1_nosed.gsssummary
- obj6414_s1_nosed.params
- obj6414_s1_nosed.constrain 

**3. 本轮观察到的问题**

- 中心出现明显亮斑
- 外围出现径向椭圆形状的红蓝交替残差。


**4. 采取的动作**

- 添加一个bulge
  - R_e调小(0.08)
  - disk的n设置成1；bulge设置成4 

**5. 调整理由**

- 中心亮斑和径向椭圆形状的红蓝交替残差特征说明存在bulge
  - bulge 有效半径较小
  - 标准模型disk = 1;bulge = 4



### Round 2

**1. 拟合所需的初始参数配置文件**

- obj6414_s2.lyric 

```bash
galfits obj6414_s2.lyric  --workplace results  --num_steps 15000
```


**2. 拟合输出文件名**

- obj6414_s2_nosedimage_fit.png
- obj6414_s2_nosed.gsssummary
- obj6414_s2_nosed.params
- obj6414_s2_nosed.constrain 


**3. 本轮观察到的问题**

- 残差基本被完全拟合
- gssummary里面的所有波段的reduced chiq 均接近0.6


**4. 采取的动作**

- 下一步做sed拟合

**5. 调整理由**

- 非常好的nosed拟合

### Round 3
**1. 拟合所需的初始参数配置文件**

- ./mass_guess/total/6414_total_pure_sed.lyric

  - 先跑guess_mass.py得到初始质量和sed参数的估计
```bash 
galfits ./mass_guess/total/6414_total_pure_sed.lyric --workplace ./mass_guess/total/results --num_steps 20000 --prior obj6414.prior
```

**2. 拟合输出文件名**

- ./mass_guess/total/results/6414image_fit.png
- ./mass_guess/total/results/6414.gsssummary
- ./mass_guess/total/results/6414.params
- ./mass_guess/total/results/6414.constrain 

**3. 本轮观察到的问题**

- sed拟合的较好，没有较大偏差。

**4. 采取的动作**

- 采取 Mass - 0.3 dex的质量作为disk和bulge 的初始质量估算
- 采用sed 拟合的f_cont, Av, Z作为disk+bulge的初始估计


**5. 调整理由**

- 质量分给两个成分(10**0.3 \approx 2)
- sed拟合因为是对整个星系拟合，所以这个结果类似某种平均结果，可作为初始估计。

### Round 4 
**1. 拟合所需的初始参数配置文件**

- obj6414_s2_sed_fix.lyric 

```bash 
galfits obj6414_s2_sed_fix.lyric  --workplace results --fit_method ES --num_generations 10000 --popsize 10
```

**2. 拟合输出文件名**

- obj6414_s2_sed_fix_ESimage_fit.png
- obj6414_s2_sed_fix_ESSED_model.png
- obj6414_s2_sed_fix_ES.gsssummary
- obj6414_s2_sed_fix_ES.params
- obj6414_s2_sed_fix_ES.constrain 

**3. 本轮观察到的问题**

- 拟合出来的质量相比于pure sed 拟合得到的质量偏小，尚不明确原因（以sed+image拟合的结果为准）
- 某些波段出现明显偏差，如F277W的蓝色残差，F444W的红色偏差。

**4. 采取的动作**

- 放开geometry 参数

**5. 调整理由**

- 认为是因为sed限制导致的残差，认为拟合较好，进行下一步


### Round 5
**1. 拟合所需的初始参数配置文件**

- obj6414_s2_sed.lyric 

```bash 
galfits obj6414_s2_sed.lyric  --workplace results --fit_method ES --num_generations 10000 --popsize 10
```

**2. 拟合输出文件名**

- obj6414_s2_sed_ESimage_fit.png
- obj6414_s2_sed_ESSED_model.png
- obj6414_s2_sed_ES.gsssummary
- obj6414_s2_sed_ES.params
- obj6414_s2_sed_ES.constrain 

**3. 本轮观察到的问题**

- 参数可以收敛到和上一步类似位置，认为拟合较好
**4. 采取的动作**

- 结束

**5. 调整理由**

- 残差图和上一步差不多。


