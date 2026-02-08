### Round 1
**1. 拟合所需的初始参数配置文件**

- results/nosed/s1/obj8021_s1.lyric

```bash
galfits obj8021_s1.lyric --workplace results/nosed/s1 --num_steps 10000
```

**2. 拟合输出文件名**

- obj8021_s1_nosedimage_fit.png
- obj8021_s1_nosed.gsssummary
- obj8021_s1_nosed.params
- obj8021_s1_nosed.constrain 

**3. 本轮观察到的问题**

- 短波外围存在额外的延展辐射，长波中间部分存在核部分。

**4. 采取的动作**

- 添加一个sersic 成分/bulge 成分。

**5. 调整理由**

- **问题**描述的正是另一个延展辐射的特征。

### Round 2
**1. 拟合所需的初始参数配置文件**

- results/nosed/s2/obj8021_s2.lyric

```bash
galfits obj8021_s2.lyric --workplace results/nosed/s2 --num_steps 15000 
```

**2. 拟合输出文件名**

- obj8021_s2_nosedimage_fit.png
- obj8021_s2_nosed.gsssummary
- obj8021_s2_nosed.params
- obj8021_s2_nosed.constrain 

**3. 本轮观察到的问题**

- 延展辐射被拟合完毕
- 短波部分还有一些clump

**4. 采取的动作**

- 认为nosed拟合完毕。

**5. 调整理由**

- 这个例子比较简单。
- 残差图较为平坦， 小型clump 是可以接受的
- gssummary 上各波段的reduced chiq都在0.55附近， 参数合理且没有到边界。

### Round 3
**1. 拟合所需的初始参数配置文件**

- mass_guess/total/8021_total_pure_sed.lyric
```bash 
galfits 8021_total_pure_sed.lyric --workplace results --num_steps 20000 --prior obj8021.prior 
```

(先运行guess_mass.py得到mass_guess dir得到mock数据)

**2. 拟合输出文件名**

- 8021SED_model.png
- 8021.gsssummary
- 8021.params
- 8021.constrain 

**3. 本轮观察到的问题**

- 数据点和模型点没有出现明显偏离。

**4. 采取的动作**

- bulge + disk总质量、AV、f_cont设置成pure sed拟合的结果。
- fix住几何参数

**5. 调整理由**

- pure sed拟合是将两成分流量加起来进行的拟合，所以拟合结果是两成分的某种平均。
- 减少自由度，先拟合sed参数。

### Round 4
**1. 拟合所需的初始参数配置文件**

- results/sed/fix_ES/obj8021_s2_ES.lyric

```bash 
galfits obj8021_s2_ES.lyric --workplace results/sed/fix_ES --fit_method ES --num_generations 10000 --popsize 10 --prior obj8021.prior 
```

**2. 拟合输出文件名**

- obj8021_s2_sed_fiximage_fit.png
- obj8021_s2_sed_fixSED_model.png
- obj8021_s2_sed_fix.gsssummary
- obj8021_s2_sed_fix.params
- obj8021_s2_sed_fix.constrain 

**3. 本轮观察到的问题**

- 残差图几乎没有变化。
- BIC略有上升。
- sed图上数据点和模型点无严重偏差。

**4. 采取的动作**

- 用此步的gssummary作为下一步optimizer 的拟合初始值

**5. 调整理由**

- optimizer往往能给出更好的拟合结果。

### Round 5
**1. 拟合所需的初始参数配置文件**

- obj8021_s2_opt.lyric

```bash 
galfits obj8021_s2_opt.lyric --workplace results/sed/fix_opt --num_steps 20000 --prior obj8021.prior --readsummary results/sed/fix_ES/obj8021_s2_sed_fix_ES.gssummary
```
(之前讲的可以采用的初始参数更新方式)

**2. 拟合输出文件名**

- obj8021_s2_sed_fix_optimage_fit.png
- obj8021_s2_sed_fix_optSED_model.png
- obj8021_s2_sed_fix_opt.gsssummary
- obj8021_s2_sed_fix_opt.params
- obj8021_s2_sed_fix_opt.constrain 

**3. 本轮观察到的问题**

- 残差图无明显变化
- BIC略有下降
- sed图同样无明显变化

**4. 采取的动作**

- free 所有的几何参数

**5. 调整理由**

### Round 6
**1. 拟合所需的初始参数配置文件**

- results/sed/opt/obj8021_s2_opt.lyric

```bash 
galfits obj8021_s2_opt.lyric --workplace results/sed/opt/ --num_steps 20000 --prior obj8021.prior --readsummary 8021/results/sed/fix_opt/obj8021_s2_sed_fix_opt.gssummary 
```

**2. 拟合输出文件名**

- obj8021_s2_sed_optimage_fit.png
- obj8021_s2_sed_optSED_model.png
- obj8021_s2_sed_opt.gsssummary
- obj8021_s2_sed_opt.params
- obj8021_s2_sed_opt.constrain 

**3. 本轮观察到的问题**

- 残差图无明显变化
- summary 文件reduced chiq略有降低
- sed图没有明显变化

**4. 采取的动作**

- finihsed

**5. 调整理由**

- xxx