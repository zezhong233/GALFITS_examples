
### Round 1
**1. 拟合所需的初始参数配置文件**

- 10766/results/nosed/s1/obj10766_s1.lyric

```bash
galfits 10766/results/nosed/s1/obj10766_s1.lyric --workplace 10766/results/nosed/s1 --fit_method ES 
```

**2. 拟合输出文件名**

- obj10766_s1_nosedimage_fit.png
- obj10766_s1_nosed.gsssummary
- obj10766_s1_nosed.params
- obj10766_s1_nosed.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - central excess and red/blue residual alternate in ratial direction 
    - a companion galaxy in the left up corner.
- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, all large than 1
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes 
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 


- Add a bulge-like Sérsic component


**6. reasons for next step**

- the image question indicate an extended component to fit the primary galaxy and a sersic to fit the companion galaxy. we will do it step by step

- parameter changing
  - new disk:
    - n: set initial guess as 1
  - bulge:
    - n: set initial guess as 4
    - R_e: slightly reducing Re (0.15) in comparison with 0.21.




### Round 2
**1. 拟合所需的初始参数配置文件**

- 10766/results/nosed/s2/obj10766_s2.lyric

```bash
galfits 10766/results/nosed/s2/obj10766_s2.lyric --workplace 10766/results/nosed/s2 --fit_method ES 
```

**2. 拟合输出文件名**

- obj10766_s2_nosedimage_fit.png
- obj10766_s2_nosed.gsssummary
- obj10766_s2_nosed.params
- obj10766_s2_nosed.constrain 


**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - there is spiral arm structure with m=2.
    - a companion galaxy in the left and up corner,

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, all large than 1
  - Whether BIC indicates a better model (if comparison exists)
    - yes
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 


- Add a disk-like Sérsic component
  
**6. reasons for next step**

- we don't care about the spiral arm currently.
- adding a sersic model to fit the companion.
  - we could get the geo estimation from the residual map


### Round 3
**1. 拟合所需的初始参数配置文件**

- 10766/results/nosed/s2_com/obj10766_s2_com.lyric

```bash
galfits 10766/results/nosed/s2_com/obj10766_s2_com.lyric --workplace 10766/results/nosed/s2_com --fit_method ES --readsummary 10766/results/nosed/s2/obj10766_s2_nosed.gssummary
```

**2. 拟合输出文件名**

- obj10766_s2_com_nosedimage_fit.png
- obj10766_s2_com_nosed.gsssummary
- obj10766_s2_com_nosed.params
- obj10766_s2_com_nosed.constrain  

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - only spiral arm structrue can be distinguished clearly.
- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable.
  - Whether BIC indicates a better model (if comparison exists)
    - yes 
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no 

**5. Next-Step Decision**: 

- Ready for SED Fitting


**6. reasons for next step**

-  image :we don't care about spiral arm currently and i think the residual in this content is accepatble. / gssummary: the parameters are reasonable and do not reach the boundary.

### Round 4
**1. 拟合所需的初始参数配置文件**

- 10766/mass_guess/com/10766_com_pure_sed.lyric
```bash
galfits 10766/mass_guess/com/10766_com_pure_sed.lyric --fit_method ES --workplace 10766/mass_guess/com/results --prior 10766/mass_guess/com/obj10766.prior 
```

- 10766/mass_guess/total/10766_total_pure_sed.lyric

```bash
galfits 10766/mass_guess/total/10766_total_pure_sed.lyric --workplace 10766/mass_guess/total/results --fit_method ES --prior 10766/mass_guess/total/obj10766.prior
```

**2. 拟合输出文件名**

- 10766SED_model.png
- 10766.gsssummary
- 10766.params
- 10766.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no image
- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no physical meaning for the oversimplied error estimation.
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Ready for Image-SED Fitting

**6. reasons for next step**

-  sed plot: model points fit well with data points / gssummary parameters are reasonable and do not reach the boundary.
  

-  parameter changing:
   -  fix the geo parameter (using round 3 best fitting value as initial guess)
   -  free geo parameter
      -  f_cont/A_v/Z: using this steps best fitting value as initial guess.
      -  mass: using best mass - ~0.3dex as initial guess of bulge and disk/ best mass as initial guess of companion.


### Round 5
**1. 拟合所需的初始参数配置文件**

- 10766/results/sed/ES_fix/obj10766_s2_com_ES_fix.lyric

```bash
galfits 10766/results/sed/ES_fix/obj10766_s2_com_ES_fix.lyric --workplace 10766/results/sed/ES_fix --fit_method ES --prior 10766/obj10766.prior 
```

**2. 拟合输出文件名**


- obj10766_s2_com_ES_fiximage_fit.png
- obj10766_s2_com_ES_fixSED_model.png
- obj10766_s2_com_ES_fix.gsssummary
- obj10766_s2_com_ES_fix.params
- obj10766_s2_com_ES_fix.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structures except for spiral arm and all band residual image get worse for sed constraint.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptbale 
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Adjust existing component parameters

**6. reasons for next step**

- image: the content of residual getting worse is acceptbale in my opinion / sed plot: the model points fit well with data points / gssummary: parameters are reasonable and do not reach the boundary.





### Round 6
**1. 拟合所需的初始参数配置文件**

- 10766/results/sed/ES_free/obj10766_s2_com_ES_free.lyric

```bash
galfits 10766/results/sed/ES_free/obj10766_s2_com_ES_free.lyric --fit_method ES --workplace 10766/results/sed/ES_free --prior 10766/obj10766.prior --readsummary 10766/results/sed/ES_fix/obj10766_s2_com_ES_fix.gssummary
```

**2. 拟合输出文件名**

- obj10766_s2_com_ES_freeimage_fit.png
- obj10766_s2_com_ES_freeSED_model.png
- obj10766_s2_com_ES_free.gsssummary
- obj10766_s2_com_ES_free.params
- obj10766_s2_com_ES_free.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - same question as round 5

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable (slightly better than round 6)
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison (slightly better than round 6)
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Adjust existing component parameters
  - using optimizer method to go further

**6. reasons for next step**

- optimizer can find better parameters compared with ES.



### Round 7
**1. 拟合所需的初始参数配置文件**

- 10766/results/sed/opt_free/obj10766_s2_com_opt_free.lyric
```bash
galfits 10766/results/sed/opt_free/obj10766_s2_com_opt_free.lyric --workplace 10766/results/sed/opt_free --fit_method optimizer --num_steps 25000 --prior 10766/obj10766.prior --readsummary 10766/results/sed/ES_free/obj10766_s2_com_ES_free.gssummary
```

**2. 拟合输出文件名**


- obj10766_s2_com_opt_freeimage_fit.png
- obj10766_s2_com_opt_freeSED_model.png
- obj10766_s2_com_opt_free.gsssummary
- obj10766_s2_com_opt_free.params
- obj10766_s2_com_opt_free.constrain 

**3. overall Judgement**

    Bad fit/Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - basically same as round 7

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable 
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison (but BIC significantly reduced compared with round 6)
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 


- Stop fitting


**6. reasons for next step**

- xxx


