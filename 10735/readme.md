
### Round 1
**1. 拟合所需的初始参数配置文件**

- 10735/results/nosed/s1/obj10735_s1.lyric
```bash
galfits 10735/results/nosed/s1/obj10735_s1.lyric --workplace 10735/results/nosed/s1 --fit_method ES 
```

**2. 拟合输出文件名**

- obj10735_s1_nosed_1image_fit.png
- obj10735_s1_nosed_1.gsssummary
- obj10735_s1_nosed_1.params
- obj10735_s1_nosed_1.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - primary galaxy:
      - in (115w, 150w, 200w, 277w), there are large scale red residuals in the outer region and blue residuals in inner region.
      - in (356w, 410m, 444w), there are central red residual and blue out region.
    - companion galaxy: in the left and upper corner of primary galaxy, there is a red clump, indicating a companion galaxy.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, reduced chi-2 of all bands except f115w is larger than expectation and f115w's low reduced chi-2 comes from the faint signal. all can be improved alot.
  - Whether BIC indicates a better model (if comparison exists)
    - no comprison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Add a bulge-like Sérsic component

**6. reasons for next step**

- the image residuals indicate a more extended component and a companion galaxy. step by step, a bulge-like component for primary galaxy.

- parameters changing 
  - new disk:
    - n: set initial guess as 1
  - new bulge:  
    - n: set initial guess as 4
    - slightly reducing R_e initial(0.05) compared with disk(0.10)



### Round 2
**1. 拟合所需的初始参数配置文件**

- 10735/results/nosed/s2/obj10735_s2.lyric

```bash 
galfits 10735/results/nosed/s2/obj10735_s2.lyric --workplace 10735/results/nosed/s2 --fit_method ES 
```

**2. 拟合输出文件名**

- obj10735_s2_nosedimage_fit.png
- obj10735_s2_nosed.gsssummary
- obj10735_s2_nosed.params
- obj10735_s2_nosed.constrain 


**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - the upper left corner has a obvious clump.  

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes, all reduced chi-2 are lower than 1. but from the image residual, it can be reduced further.
  - Whether BIC indicates a better model (if comparison exists)
    - yes, in comparison with single sersic component.
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Add a disk-like Sérsic component

**6. reasons for next step**

- we should add a single sersic component to fit the companion.

- parameters changing:
  - new com:
    - the initial position/R/PA/q/redshift can fetch from galfitX.
  - update primary galaxy parameters:
    - using --readsummary

### Round 3

**1. 拟合所需的初始参数配置文件**

- 10735/results/nosed/s2_com/obj10735_s2_com.lyric

```bash
galfits 10735/results/nosed/s2_com/obj10735_s2_com.lyric --workplace 10735/results/nosed/s2_com --fit_method ES --readsummary 10735/results/nosed/s2/obj10735_s2_nosed.gssummary
```

**2. 拟合输出文件名**

- obj10735_s2_comimage_fit.png
- obj10735_s2_com.gsssummary
- obj10735_s2_com.params
- obj10735_s2_com.constrain 


**3. overall Judgement**

- /Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes. 
  - Whether BIC indicates a better model (if comparison exists)
    - yes, in comparison with no companion.
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 


- Ready for SED Fitting

**6. reasons for next step**

- image: no obvious structure; gssummary: reduced chi-2 and parameters are reasonable.



### Round 4
**1. 拟合所需的初始参数配置文件**

- 10735/mass_guess/com_1/10735_com_1_pure_sed.lyric

```bash
galfits 10735/mass_guess/com_1/10735_com_1_pure_sed.lyric --workplace 10735/mass_guess/com_1/results --fit_method ES --prior 10735/mass_guess/com_1/obj10735_com.prior
```

- 10735/mass_guess/total/10735_total_pure_sed.lyric

```bash
galfits 10735/mass_guess/total/10735_total_pure_sed.lyric --workplace 10735/mass_guess/total/results --fit_method ES --prior 10735/mass_guess/total/obj10735_pri.prior
```

**2. 拟合输出文件名**

- 10735SED_model.png
- 10735.gsssummary
- 10735.params
- 10735.constrain (in two results dir: 10735/mass_guess/com_1/results and 10735/mass_guess/total/results)


**3. overall Judgement**

    Bad fit/Good fit

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
    - it's not meaningful for the oversimplified error estimation. 
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

- sed plot: model point fitting well with data pointings / gssummary: parameters seem reasonable and do not reach the boundary.
  
- parameters changing 
  - fix geo parameters(using best fit value of round 3)
  - free sed parameters 
    - f_cont/A_v/Z: using the best fit value of this step as initial guess 
    - mass: using best fit mass - ~0.3 dex as mass guess of disk/bulge and best fit mass for companion.



### Round 5
**1. 拟合所需的初始参数配置文件**

- 10735/results/sed/ES_free/obj10735_s2_com_ES_fix.lyric

```bash
galfits 10735/results/sed/ES_free/obj10735_s2_com_ES_fix.lyric --workplace 10735/results/sed/ES_fix --fit_method ES --prior  10735/obj10735.prior
```

**2. 拟合输出文件名**

- obj10735_s2_com_ES_fiximage_fit.png
- obj10735_s2_com_ES_fixSED_model.png
- obj10735_s2_com_ES_fix.gsssummary
- obj10735_s2_com_ES_fix.params
- obj10735_s2_com_ES_fix.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - In comparison with no sed fitting, there are obvious residual for sed fitting, like central red residual for primary galaxy in f200w and blue residual in f410m and f444w

- sed plot
  - Check whether model points are close to observed points overall
    - model points are generally close to data points, except the obvious under-estimation for f200w.
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable. Besides that reduced chi-2 of f356w and f444w are lightly large than 1, other bands are smaller than 1.
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

- I think the residual/sed and gssummary is acceptable. 

- parameters changing
  - free geo parameters
  - update parameters using (--readsummary )



### Round 6
**1. 拟合所需的初始参数配置文件**

- 10735/results/sed/ES_fix/obj10735_s2_com_ES_fix.lyric

```bash
galfits 10735/results/sed/ES_fix/obj10735_s2_com_ES_fix.lyric --workplace 10735/results/sed/ES_free --fit_method ES --prior 10735/obj10735.prior --readsummary 10735/results/sed/ES_fix/obj10735_s2_com_ES_fix.gssummary 
```

**2. 拟合输出文件名**


- obj10735_s2_com_ES_freeimage_fit.png
- obj10735_s2_com_ES_freeSED_model.png
- obj10735_s2_com_ES_free.gsssummary
- obj10735_s2_com_ES_free.params
- obj10735_s2_com_ES_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - same questions as round 5, no obvious improvement.

- sed plot
  - Check whether model points are close to observed points overall
    - yes except f200w
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable. Besides that reduced chi-2 of f356w and f444w are lightly large than 1, other bands are smaller than 1.
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison but improved a little compared with round 5
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
        

**5. Next-Step Decision**: 

- Adjust existing component parameters
  - using optimizer to go further.

**6. reasons for next step**

- optimizer can find better solution than ES generally.


### Round 7
**1. 拟合所需的初始参数配置文件**

- 10735/results/sed/ES_free/obj10735_s2_com_ES_free.lyric

```bash
galfits 10735/results/sed/ES_free/obj10735_s2_com_ES_free.lyric --workplace 10735/results/sed/opt_free --fit_method optimizer --num_steps 20000 --prior 10735/obj10735.prior --readsummary 10735/results/sed/ES_free/obj10735_s2_com_ES_free.gssummary
```

**2. 拟合输出文件名**


- obj10735_s2_com_opt_freeimage_fit.png
- obj10735_s2_com_opt_freeSED_model.png
- obj10735_s2_com_opt_free.gsssummary
- obj10735_s2_com_opt_free.params
- obj10735_s2_com_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - same questions as round 5, no obvious improvement.

- sed plot
  - Check whether model points are close to observed points overall
    - yes except f200w
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable. Besides that reduced chi-2 of f356w and f444w are lightly large than 1, other bands are smaller than 1.
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison but improved a little compared with round 6
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Stop fitting

**6. reasons for next step**

