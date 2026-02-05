### Round 1
**1. 拟合所需的初始参数配置文件**

- obj10735_s1.lyric 

```bash
galfits obj10735_s1.lyric --workplace results --num_steps 16000

```

**2. 拟合输出文件名**

- obj10735_s1_nosed_1image_fit.png
- obj10735_s1_nosed_1.gsssummary
- obj10735_s1_nosed_1.params
- obj10735_s1_nosed_1.constrain 

**3. 本轮观察到的问题**

- 模型和cut image 的大小不匹配，残差存在径向上的椭圆形状红蓝交替。

**4. 采取的动作**

- 添加一个component, 变成双成分bulge + disk拟合
  - R_e:相比于单成分拟合，设置初始disk R_e较大，bulge R_e较小；
  - n: disk n = 1, bulge n = 4;
  - q: disk 设置不变， bulge稍大

**5. 调整理由**

- 出model 和cut image的大小不匹配，径向上的椭圆形状红蓝交替，说明整体的轮廓无法被单sersic 描述，需要加一个sersic 
  - disk较为延展而bulge较为紧密
  - 标准模型上disk n = 1, bulge n = 4
  - GalfitX的几何参数描述的大部分是disk，不变，bulge 的较为圆，故调大一点轴比。

### Round 2
**1. 拟合所需的初始参数配置文件**

- obj10735_s2.lyric

```bash
galfits obj10735_s2.lyric --workplace results --num_steps 16000

```

**2. 拟合输出文件名**

- obj10735_s2_nosed_1image_fit.png
- obj10735_s2_nosed_1.gsssummary
- obj10735_s2_nosed_1.params
- obj10735_s2_nosed_1.constrain 

**3. 本轮观察到的问题**

- 残差图上，中心primary 基本被拟合，观察到左上角存在另一个源。

**4. 采取的动作**

- 尝试用sersic 模型去拟合。
  - 初始的参数可以通过对局部的cut image 跑 GalfitX 得到。


**5. 调整理由**

- xxx


### Round 3
**1. 拟合所需的初始参数配置文件**

- obj10735_s2_com.lyric 

```bash
galfits  obj10735_s2_com.lyric --workplace results --num_steps 20000
```

**2. 拟合输出文件名**

- obj10735_s2_com_nosed_1image_fit.png
- obj10735_s2_com_nosed_1.gsssummary
- obj10735_s2_com_nosed_1.params
- obj10735_s2_com_nosed_1.constrain 

**3. 本轮观察到的问题**

- nosed 基本拟合成功。

**4. 采取的动作**

- 修改sed fitting初始几何参数为这一步的best fit.
- 读取此步模型测光来做pure sed 拟合。

**5. 调整理由**

- 正常update
- 估算质量、金属丰度、消光和恒星形成率等物理参数

### Round 4 
**1. 拟合所需的初始参数配置文件**

- ./mass_guess/total/10735_total_pure_sed.lyric 

  - 首先修改guess_mass.py中的路径，运行
  ```bash
  python ./mass_guess/guess_mass.py
  ```
  - 得到10735_total_flux_err.cat、文件和lyric。

```bash
galfits ./mass_guess/total/10735_total_pure_sed.lyric  --workplace  ./mass_guess/total/results --num_steps 10000
```

**2. 拟合输出文件名**

- ./mass_guess/total/results/10735SED_model.png
- ./mass_guess/total/results/10735.gsssummary
- ./mass_guess/total/results/10735.params
- ./mass_guess/total/results/10735.constrain 

**3. 本轮观察到的问题**

- 得到galaxy_1(bulge+disk) 和 galaxy_2(com_1)的总质量、平均sfr、z和Av。

**4. 采取的动作**

- sed 拟合的时候：
  - 认为bulge + disk 的总质量在10**10.5 solar mass 左右  (分别设置成总质量-0.3dex,因为10**0.3 = 2)， 金属风度、消光和sfr设置成平均的。
  - com_1同理

**5. 调整理由**

- 暂时先这样估计sed拟合的物理参数。

### Round 5
**1. 拟合所需的初始参数配置文件**

- obj10735_s2_com_sed_fix.lyric 

```bash
galfits obj10735_s2_com_sed_fix.lyric  --workplace results --num_steps 25000 --prior obj107735.prior 
```
  - 这里加prior 是因为直接拟合的话金属丰度会非常低，sed参数出现兼并，所以加Z-Mass relation 来限制一下金属丰度。

**2. 拟合输出文件名**

- obj10735_s2_com_sed_fiximage_fit.png
- obj10735_s2_com_sed_fixSED_model.png
- obj10735_s2_com_sed_fix.gsssummary
- obj10735_s2_com_sed_fix.params
- obj10735_s2_com_sed_fix.constrain 

**3. 本轮观察到的问题**

- 从图像上看相比于no sed fitting, 出现更多的残差(如F150W,F200W, F444W)，但是仍然属于可接受范围内。
- sed上数据点和模型点基本对得上，offset的和图像也能对应。
- gssummary 没有触碰到boundary的参数。

**4. 采取的动作**

- 更新下一步free sed 参数为这一步的best fitting value.

**5. 调整理由**

- 认为是好拟合，正常更新。


### Round 6

**1. 拟合所需的初始参数配置文件**

- obj10735_s2_com_sed.lyric

```bash
galfits obj10735_s2_com_sed.lyric --workplace results --num_steps 25000 --prior obj10735.prior
```

**2. 拟合输出文件名**


- obj10735_s2_com_sed_1image_fit.png
- obj10735_s2_com_sed_1SED_model.png
- obj10735_s2_com_sed_1.gsssummary
- obj10735_s2_com_sed_1.params
- obj10735_s2_com_sed_1.constrain 

**3. 本轮观察到的问题**

- reduced chiq 相比fix geometry拟合下降。
- 图像残差相对nosed 仍有较为明显的残差，但是可以接受。
- 注意到代表sfh的参数(f_cont)有一些bin触碰到了边界，这是因为sed 参数兼并的问题，目前没有什么好办法，但是理论上也不期望能从sed拟合上面严格限制sfh，所以暂且作罢。

**4. 采取的动作**

- 认为是好拟合，finished.

**5. 调整理由**

- xxx