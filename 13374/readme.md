
### Round 1
**1. 拟合所需的初始参数配置文件**

- 13374/results/nosed/s1/obj13374_s1.lyric

```bash
galfits 13374/results/nosed/s1/obj13374_s1.lyric --workplace 13374/results/nosed/s1 --fit_method ES 
```

**2. 拟合输出文件名**

- obj13374_s1image_fit.png
- obj13374_s1.gsssummary
- obj13374_s1.params
- obj13374_s1.constrain 



**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - there is obvious large scale red residuals in the outer region.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, generally larger than expected.
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

-  there is large scale residual not been fitted well, so need a extended component to fit it.
-  parameters changing 
   -  new disk:
      -  n: changing initial guess to 1
   -  bulge:
      -  n: setting initial guess as 4
      -  R_e: slightly reduceing Re compared with disk.



### Round 2
**1. 拟合所需的初始参数配置文件**
- 13374/results/nosed/s2/obj13374_s2.lyric
```bash
galfits 13374/results/nosed/s2/obj13374_s2.lyric --workplace 13374/results/nosed/s2 --fit_method ES 
```

**2. 拟合输出文件名**

- obj13374_s2image_fit.png
- obj13374_s2.gsssummary
- obj13374_s2.params
- obj13374_s2.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
  - there is a obvious clump in the right bottom corner and it was not detected by galfitx for the pollution of primary source and the physical nature itself (only can be distinguished in F277W and F356W). Because we don't know the redshift/nature of it currently, so ignore it.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - can be accepted because the worst bands (277w, 356w) is leaded to by the right bottom companion.
  - Whether BIC indicates a better model (if comparison exists)
    - yes.
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    -  disk(n~1) has a smaller radius and bulge (n~4) has a larger radius.it's rare, but not impossible.
  - Check if parameters are close to min/max limits.
    - no 
              

**5. Next-Step Decision**: 

- Ready for SED Fitting


**6. reasons for next step**

- though not good enough, it can be acceptable.

### Round 3
**1. 拟合所需的初始参数配置文件**
- 13374/mass_guess/total/13374_total_pure_sed.lyric
```bash
galfits 13374/mass_guess/total/13374_total_pure_sed.lyric --workplace 13374/mass_guess/total/results --fit_method ES --prior 13374/mass_guess/total/obj13374.prior
```

**2. 拟合输出文件名**

- 13374SED_model.png
- 13374.gsssummary
- 13374.params
- 13374.constrain 


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
    - yes

- gssummary
  - Whether the reduced chi-square is within a reasonable range\
    - there's not meaningful for the oversimplified error estimation.
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

- sed plot: the model points fit well with data points and no systematic offset / gssummary: the parameters are reasonable. 

- parameter changing:
  - fix geo parameters(update values as the best fitting value of round 2)
  - free sed parameters
    - A_v/f_cont/Z: using this steps best fitting value as initial guess
    - mass: using best fitting mass value - ~0.3 dex as initial guess of disk/bulge

### Round 4
**1. 拟合所需的初始参数配置文件**

- 13374/results/sed/ES_fix/obj13374_s2_ES_fix.lyric

```bash 
galfits 13374/results/sed/ES_fix/obj13374_s2_ES_fix.lyric --workplace 13374/results/sed/ES_fix --fit_method ES --prior 13374/obj13374.prior 
```

**2. 拟合输出文件名**

- obj13374_s2_ES_fiximage_fit.png
- obj13374_s2_ES_fixSED_model.png
- obj13374_s2_ES_fix.gsssummary
- obj13374_s2_ES_fix.params
- obj13374_s2_ES_fix.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure except for the right bottom clump and the primary source's residual caused by sed constraint.

- sed plot
  - Check whether model points are close to observed points overall
    - yes. 
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - it's acceptable for the companion pollution.
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison (BIC increased comparied with no sed fitting)
  - Whether the fitting process has converged
    - yes 
  - Check whether parameters are physically reasonable
    - yes 
  - Check if parameters are close to min/max limits
    - no 
              

**5. Next-Step Decision**: 

- Ready for Image-SED Fitting


**6. reasons for next step**

- image: no obvious structure of new component / residual is acceptable; sed plot: the model points fit well with data points generally. / gssummary: parameters are reasonable.

- parameters changing 
  - free geo parameters 
  - update parameters (--readsummary )

### Round 5
**1. 拟合所需的初始参数配置文件**

- 13374/results/sed/ES_free/obj13374_s2_ES_free.lyric

```bash
galfits 13374/results/sed/ES_free/obj13374_s2_ES_free.lyric --workplace 13374/results/sed/ES_free --fit_method ES --prior 13374/obj13374.prior --readsummary  13374/results/sed/ES_fix/obj13374_s2_ES_fix.gssummary
```

**2. 拟合输出文件名**

- obj13374_s2_ES_freeimage_fit.png
- obj13374_s2_ES_freeSED_model.png
- obj13374_s2_ES_free.gsssummary
- obj13374_s2_ES_free.params
- obj13374_s2_ES_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure except for the right bottom clumps.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - accepable for the companion pollution and slightly better than round 4.
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
  - using optimizer to go further 
  

**6. reasons for next step**

- optimizer can find better parameters than ES. 




### Round 6
**1. 拟合所需的初始参数配置文件**

- 13374/results/sed/opt_free/obj13374_s2_opt_free.lyric

```bash
galfits 13374/results/sed/opt_free/obj13374_s2_opt_free.lyric --workplace 13374/results/sed/opt_free --prior 13374/obj13374.prior --readsummary 13374/results/sed/ES_free/obj13374_s2_ES_free.gssummary
```

**2. 拟合输出文件名**


- obj13374_s2_opt_freeimage_fit.png
- obj13374_s2_opt_freeSED_model.png
- obj13374_s2_opt_free.gsssummary
- obj13374_s2_opt_free.params
- obj13374_s2_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure except for the right bottom clump.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - accepable and slight better than round 5
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes 
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- finished

**6. reasons for next step**

- xxx


