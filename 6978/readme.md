
### Round 1
**1. 拟合所需的初始参数配置文件**

- 6978/results/nosed/s1/obj6978_s1.lyric
```bash
galfits 6978/results/nosed/s1/obj6978_s1.lyric --workplace 6978/results/nosed/s1 --fit_method ES
```

**2. 拟合输出文件名**

- obj6978_s1_nosedimage_fit.png
- obj6978_s1_nosed.gsssummary
- obj6978_s1_nosed.params
- obj6978_s1_nosed.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - obvious central excess and red/blue residuals alternate in ratial direction.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, reduced chi-2 of all bands are large than 1 heacily.
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

- the problem described in image part indicate an extended component.

- parameters changing
  - new disk:
    - n: set initial guess as 1
  - bulge: 
    - n: set initial guess as 4
    - R_e: slightly reducing the re(0.15) compared with disk(0.23)



### Round 2
**1. 拟合所需的初始参数配置文件**

- 6978/results/nosed/s2/obj6978_s2.lyric
```bash
galfits 6978/results/nosed/s2/obj6978_s2.lyric --workplace 6978/results/nosed/s2 --fit_method ES 
```

**2. 拟合输出文件名**

- obj6978_s2_nosedimage_fit.png
- obj6978_s2_nosed.gsssummary
- obj6978_s2_nosed.params
- obj6978_s2_nosed.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - in the central region, there are two symmetric spiral arms.
    - in the out region, there is a ring-like red residual.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed
  - Check whether systematic offsets exist across wavelengths
    - no sed 
- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, still large than 1, but have been better than singe sersic
  - Whether BIC indicates a better model (if comparison exists)
    - yes 
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
              

**5. Next-Step Decision**: 

- Add a ring component

**6. reasons for next step**

- the image questions indicate a ring-like component and spiral arm component with m=2, but we don't care about spiral arm currently.

- parameters changing:
  - it's hard to estimate the geo scale of ring. 
  - so we can give a relatively large range and check if the ring structure is fitted gradually.

### Round 3
**1. 拟合所需的初始参数配置文件**

- 6978/results/nosed/s2r/obj6978_s2r_1.lyric

```bash
galfits 6978/results/nosed/s2r/obj6978_s2r_1.lyric --workplace 6978/results/nosed/s2r --fit_method ES --readsummary 6978/results/nosed/s2/obj6978_s2_nosed.gssummary
```

**2. 拟合输出文件名**

- obj6978_s2r_nosed_1image_fit.png
- obj6978_s2r_nosed_1.gsssummary
- obj6978_s2r_nosed_1.params
- obj6978_s2r_nosed_1.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - the ring structure has been fitted basically.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - accepable
  - Whether BIC indicates a better model (if comparison exists)
    - yes
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - the n of disk reach the low boundary.
              

**5. Next-Step Decision**: 


- Adjust existing component parameters


**6. reasons for next step**

- the n of disk reach the low boundary(0.2), so enlarge the range and fit again.


### Round 4
**1. 拟合所需的初始参数配置文件**

- 6978/results/nosed/s2r/obj6978_s2r_2.lyric

**2. 拟合输出文件名**

- obj6978_s2r_nosed_2image_fit.png
- obj6978_s2r_nosed_2.gsssummary
- obj6978_s2r_nosed_2.params
- obj6978_s2r_nosed_2.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - ring structure has been fitted basically.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - accepatble
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

- image: no obvious remaining structure / gssummary: the rediced chi-2 is accepable for the complexity of galaxy morphology and all parameters are reasonable and not reach the boundary.


### Round 5
**1. 拟合所需的初始参数配置文件**

- 6978/mass_guess/total/6978_total_pure_sed.lyric

```bash
galfits 6978/mass_guess/total/6978_total_pure_sed.lyric --workplace 6978/mass_guess/total/results --fit_method ES --prior 6978/mass_guess/total/obj6978.prior
```

**2. 拟合输出文件名**

- 6978SED_model.png
- 6978.gsssummary
- 6978.params
- 6978.constrain 


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

- sed plot: model points fit well with data points /gssummary:parameters are reasonable and not reach the boundary 



### Round 6
**1. 拟合所需的初始参数配置文件**

- 6978/results/sed/ES_fix/obj6978_s2r_ES_fix.lyric

```bash
galfits 6978/results/sed/ES_fix/obj6978_s2r_ES_fix.lyric --workplace 6978/results/sed/ES_fix --fit_method ES --prior 6978/obj6978.prior
```

**2. 拟合输出文件名**


- obj6978_s2r_sed_ES_fiximage_fit.png
- obj6978_s2r_sed_ES_fixSED_model.png
- obj6978_s2r_sed_ES_fix.gsssummary
- obj6978_s2r_sed_ES_fix.params
- obj6978_s2r_sed_ES_fix.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious remaining structure, while there new residual in residual map for SED comstraint, like central red residual in f277w and blue residual in f410m. but it can be acceptable.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - Av of disk and bulge reach the low boundary 0
              
**5. Next-Step Decision**: 

- Adjust existing component parameters

**6. reasons for next step**

- image:  no obvious structure and is not too bad compared with no sed fitting; sed plot: model points and data points fit well; gssummary: reduced chi-2 is acceptable and parameters are reasonable(the A_v reach the low boundary is not a big deal.)

### Round 7
**1. 拟合所需的初始参数配置文件**

- 6978/results/sed/ES_free/obj6978_s2r_ES_free.lyric

```bash
galfits 6978/results/sed/ES_free/obj6978_s2r_ES_free.lyric --workplace 6978/results/sed/ES_free --fit_method ES --prior 6978/obj6978.prior --readsummary 6978/results/sed/ES_fix/obj6978_s2r_sed_ES_fix.gssummary
```

**2. 拟合输出文件名**


- obj6978_s2r_sed_ES_freeimage_fit.png
- obj6978_s2r_sed_ES_freeSED_model.png
- obj6978_s2r_sed_ES_free.gsssummary
- obj6978_s2r_sed_ES_free.params
- obj6978_s2r_sed_ES_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - basically same as round 6

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - accepatble 
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison (improved a little in comparison with round 6)
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - still A_v of disk and bulge.
              

**5. Next-Step Decision**: 


- Adjust existing component parameters
  - using optimizer to go further 

**6. reasons for next step**

- optimizer method can find better results compared with ES 




### Round 8
**1. 拟合所需的初始参数配置文件**

- 6978/results/sed/opt_free/obj6978_s2r_opt_free.lyric

```bash
galfits 6978/results/sed/opt_free/obj6978_s2r_opt_free.lyric --workplace 6978/results/sed/opt_free --fit_method optimizer --num_steps 25000 --prior 6978/obj6978.prior --readsummary 6978/results/sed/ES_free/obj6978_s2r_sed_ES_free.gssummary
```

**2. 拟合输出文件名**


- obj6978_s2r_sed_opt_freeimage_fit.png
- obj6978_s2r_sed_opt_freeSED_model.png
- obj6978_s2r_sed_opt_free.gsssummary
- obj6978_s2r_sed_opt_free.params
- obj6978_s2r_sed_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - basically same as round 6

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths   
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison(improved a little compared with round 7)
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




