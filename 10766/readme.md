##### you should find the files from results directory.

### Round 1
**1. 拟合所需的初始参数配置文件**

- resultsnosed/s1_nosed/obj10766_s1.lyric 

```bash
galfits obj10766_s1.lyric --workplace results/nosed/s1_nosed --num_steps 15000
```

**2. 拟合输出文件名**

- obj10766_s1_nosedimage_fit.png
- obj10766_s1_nosed.gsssummary
- obj10766_s1_nosed.params
- obj10766_s1_nosed.constrain 

**3. 本轮观察到的问题**

- 残差图上中心存在致密核，径向存在椭圆形状红蓝交替的残差
- 左上角存在另一个伴星系

**4. 采取的动作**

- 在中心的primary galaxy上加一个bulge 
  - n: disk = 1, bulge = 4。
  - Re: disk调大一点，bulge调小一点。


**5. 调整理由**

- “残差图上中心存在致密核，径向存在椭圆形状红蓝交替的残差”该特征意味着添加延展成分。
  - n: 理论模型
  - Re: disk 更为延展；bulge更为紧密

### Round 2

**1. 拟合所需的初始参数配置文件**

- results/nosed/s2_nosed/obj10766_s2.lyric

```bash 
galfits obj10766_s2.lyric --workplace results/nosed/s2_nosed --num_steps 15000 

```
**2. 拟合输出文件名**

- obj10766_s2_nosedimage_fit.png
- obj10766_s2_nosed.gsssummary
- obj10766_s2_nosed.params
- obj10766_s2_nosed.constrain 


**3. 本轮观察到的问题**

- primary galaxy基本被拟合
  - 中心残差看起来存在旋臂结构，暂时不去考虑
- 左上角存在伴星系

**4. 采取的动作**

- 添加一个companion galaxy
- 利用这一步的best fit value 固定primary galaxy 的成分。

**5. 调整理由**

- 左上角存在伴星系
  - 减少自由度先去拟合伴星系。

### Round 3
**1. 拟合所需的初始参数配置文件**

- results/nosed/s2_com_fix_nosed/obj10766_s2_com_fix.lyric 
```bash 
galfits obj10766_s2_com_fix.lyric --workplace results/nosed/s2_com_fix_nosed --num_steps 25000
```

**2. 拟合输出文件名**

- obj10766_s2_com_fiximage_fit.png
- obj10766_s2_com_fix.gsssummary
- obj10766_s2_com_fix.params
- obj10766_s2_com_fix.constrain 

**3. 本轮观察到的问题**

- 伴星系被拟合完毕。

**4. 采取的动作**

- 更新伴星系的best value到下一步的initial guess然后free primary galaxy的参数。

**5. 调整理由**

- 看是否能同时收敛。

### Round 4

**1. 拟合所需的初始参数配置文件**

- /results/nosed/s2_com_nosed/obj10766_s2_com.lyric

```bash
galfits obj10766_s2_com.lyric --workplace results/nosed/s2_com_nosed --num_steps 20000
```

**2. 拟合输出文件名**

- obj10766_s2_comimage_fit.png
- obj10766_s2_com.gsssummary
- obj10766_s2_com.params
- obj10766_s2_com.constrain 

**3. 本轮观察到的问题**

- free所有nosed参数可以收敛。

**4. 采取的动作**

- 修改路径和idx， 运行guess_mass.py得到catalog。

**5. 调整理由**

- 利用pure sed 拟合得到mass 和 f_cont 的初始参数。

### Round 5
**1. 拟合所需的初始参数配置文件**

- mass_guess/total/10766_total_pure_sed.lyric
- 10766/mass_guess/com/10766_com_pure_sed.lyric

```bash 
galfits 10766_total_pure_sed.lyric --workplace results --num_steps 20000 --prior obj10766.lyric
```

```bash 
galfits 10766_com_pure_sed.lyric --workplace results --num_steps 20000 --prior obj10766.lyric
```

**2. 拟合输出文件名**

total
- 10766SED_model.png
- 10766.gsssummary
- 10766.params
- 10766.constrain  

com
- 10766SED_model.png
- 10766.gsssummary
- 10766.params
- 10766.constrain  
 

**3. 本轮观察到的问题**

- sed image上面 红点和黑点无大偏离

**4. 采取的动作**

- 将两个星系得到的质量、sed参数作为下一轮的初始参数.
  - primary galaxy质量对于bulge 和disk平均分，大概-0.3dex。
  - 因为未知原因，这里得到的质量会和真实稍微有点偏差，所以先fix住几何参数，用收敛更快的ES来估算总的质量和primary的disk/bulge的分别占比。

**5. 调整理由**

- xxx


### Round 6
**1. 拟合所需的初始参数配置文件**

- results/sed/s2_com_fix_ES/obj10766_s2_com_fix_ES.lyric

```bash 
galfits  obj10766_s2_com_fix_ES.lyric --workplace results/sed/s2_com_fix_ES --fit_method ES --num_generations 10000 --popsize 10 --prior obj10766.prior 
```

**2. 拟合输出文件名**

- obj10766_s2_com_fix_sed_ESimage_fit.png
- obj10766_s2_com_fix_sed_ES.gsssummary
- obj10766_s2_com_fix_sed_ES.params
- obj10766_s2_com_fix_sed_ES.constrain 
- obj10766_s2_com_fix_sed_ESSED_model.png


**3. 本轮观察到的问题**

- 残差图相对于nosed的图略差，但是无明显偏离。

**4. 采取的动作**

- 估算出来disk/bulge/com的大概质量，作为下一步optimizer的初始值。

**5. 调整理由**

- optimizer收敛比较困难但是最终拟合结果比ES好，再加一步optimizer.

### Round 7
**1. 拟合所需的初始参数配置文件**

- results/sed/s2_com_fix_opt/obj10766_s2_com_fix_opt.lyric

```bash 
galfits obj10766_s2_com_fix_opt.lyric --workplace results/sed/s2_com_fix_opt --num_steps 20000 --prior obj10766.lyric
```

**2. 拟合输出文件名**

- obj10766_s2_com_fix_sed_optimage_fit.png
- obj10766_s2_com_fix_sed_optSED_model.png
- obj10766_s2_com_fix_sed_opt.gsssummary
- obj10766_s2_com_fix_sed_opt.params
- obj10766_s2_com_fix_sed_opt.constrain 

**3. 本轮观察到的问题**

- 同样可以收敛，并且chiq相比于ES显著下降。

**4. 采取的动作**

- free 几何参数，更新sed参数为当前的best value.

**5. 调整理由**

- xxx


### Round 8

**1. 拟合所需的初始参数配置文件**

- results/sed/s2_com_opt/obj10766_s2_com_opt.lyric 

```bash 
galfits obj10766_s2_com_opt.lyric --workplace results/sed/s2_com_opt --num_steps 25000 --prior obj10766.prior
```

**2. 拟合输出文件名**

- obj10766_s2_com_sedimage_fit.png
- obj10766_s2_com_sedSED_model.png
- obj10766_s2_com_sed.gsssummary
- obj10766_s2_com_sed.params
- obj10766_s2_com_sed.constrain 

**3. 本轮观察到的问题**

- 残差图仍然可以收敛，chiq有所下降。
- 但是com_1输出和输入没有变化。


**4. 采取的动作**

- 经验性的方法是可以对com_1的一些参数做人为改变，比如n改成比较荒诞的4，拟合结果会更好。

**5. 调整理由**

- 也许是算法本身的问题，在初始参数比较接近的时候会不去优化。认为去偏一点会更好。


### Round 9
**1. 拟合所需的初始参数配置文件**

- results/sed/s2_com_opt2/obj10766_s2_com_opt2.lyric

```bash 
galfits obj10766_s2_com_opt2.lyric --workplace results/sed/s2_com_opt2 --num_steps 25000 --prior obj10766.prior 
```

**2. 拟合输出文件名**

- obj10766_s2_com_sed_opt2image_fit.png
- obj10766_s2_com_sed_opt2SED_model.png
- obj10766_s2_com_sed_opt2.gsssummary
- obj10766_s2_com_sed_opt2.params
- obj10766_s2_com_sed_opt2.constrain 

**3. 本轮观察到的问题**

- 仍然可以收敛，做出改变的n回到合理的数值，com的参数发生变化。chiq下降。

**4. 采取的动作**

- 认为拟合完成。

**5. 调整理由**

- xxx