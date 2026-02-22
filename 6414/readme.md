
### Round 1
**1. 拟合所需的初始参数配置文件**

- 6414/results/nosed/s1/obj6414_s1.lyric

```bash 
galfits 6414/results/nosed/s1/obj6414_s1.lyric --workplace 6414/results/nosed/s1 --fit_method ES 
```

**2. 拟合输出文件名**

- obj6414_s1_nosedimage_fit.png
- obj6414_s1_nosed.gsssummary
- obj6414_s1_nosed.params
- obj6414_s1_nosed.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - obvious central excess and red/blue alternate in ratial direction 

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes, but definitely could be better.
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    -  no
              

**5. Next-Step Decision**: 

- Add a bulge-like Sérsic component

**6. reasons for next step**

- the image problem indicates a bulge-like component needed to be added.

- parameters changing
  - new disk:
    - n: change initial guess to 1
  - bulge:
    - n: change initial guess to 4
    - R_e: slightly reduce the effective radius of bulge.



### Round 2
**1. 拟合所需的初始参数配置文件**

- 6414/results/nosed/s2/obj6414_s2.lyric

```bash 
galfits 6414/results/nosed/s2/obj6414_s2.lyric --workplace 6414/results/nosed/s2 --fit_method ES
```

**2. 拟合输出文件名**

- obj6414_s2_nosedimage_fit.png
- obj6414_s2_nosed.gsssummary
- obj6414_s2_nosed.params
- obj6414_s2_nosed.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - central excess disappear and the ratial alternative color is eased.
    - small clump in about (90,100) pixel coordinate. Most obvious in f115w.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    -  no
              

**5. Next-Step Decision**: 

- Ready for SED Fitting

**6. reasons for next step**

- main structure has been good fitted though some small clumps exist but we don't care about it currently / parameters in gssummary are reasonable and not reach the boundary.




### Round 3
**1. 拟合所需的初始参数配置文件**

- 6414/mass_guess/total/6414_total_pure_sed.lyric 

```bash 
galfits 6414/mass_guess/total/6414_total_pure_sed.lyric  --workplace results --fit_method ES --prior 6414/mass_guess/total/obj6414.prior
```

**2. 拟合输出文件名**


- 6414SED_model.png
- 6414.gsssummary
- 6414.params
- 6414.constrain 


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
    - because the error is oversimplified, the reduced chi-2 is not physical.
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

- no strong offset in sed plot though f444w show relatively large deviation / parameters in gssummary are reasonable and not reach the boundary.

- parameters changing 
  - disk:
    - fix geo parameters
    - free sed parameters and set the best fitting value of this step as initial guess of sed parameters.
    - stellar mass: set mass as half of the best fit mass of pure sed fitting.
  - bulge 
    - fix geo parameters
    - free sed parameters and set the best fitting value of this step as initial guess of sed parameters.
    - stellar mass: set mass as half of the best fit mass of pure sed fitting.




### Round 4
**1. 拟合所需的初始参数配置文件**

- 6414/results/sed/ES_fix/obj6414_s2_sed_ES_fix.lyric

```bash 
galfits 6414/results/sed/ES_fix/obj6414_s2_sed_ES_fix.lyric --workplace 6414/results/sed/ES_fix --fit_method ES --prior 6414/obj6414.prior
```

**2. 拟合输出文件名**

- obj6414_s2_sed_ES_fiximage_fit.png
- obj6414_s2_sed_ES_fixSED_model.png
- obj6414_s2_sed_ES_fix.gsssummary
- obj6414_s2_sed_ES_fix.params
- obj6414_s2_sed_ES_fix.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - In comparison with no sed fitting, there are obvious blue redisual (f200w, f277w) and red residual(f356w, f410m, f444w) in residual map, which is caused by physical sed addition.

- sed plot
  - Check whether model points are close to observed points overall
    - yes, except for f444w, which can be indicated by image too.
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes
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
  - update parameters (using --readsummary xxx.gssummary)
  - free sed parameters.

**6. reasons for next step**

- Though in some bands, the residual map show obvious flux offset, we think it's caused by sed constrain and accept it / sed plot doesn't show systematic offset / gssummary parameters are reasonable and don't reach the boundary.



### Round 5
**1. 拟合所需的初始参数配置文件**

- 6414/results/sed/ES_free/obj6414_s2_sed_ES_free.lyric

```bash 
galfits 6414/results/sed/ES_free/obj6414_s2_sed_ES_free.lyric --workplace 6414/results/sed/ES_free --fit_method ES --prior 6414/obj6414.prior --readsummary 6414/results/sed/ES_fix/obj6414_s2_sed_ES_fix.gssummary 
```

**2. 拟合输出文件名**

- obj6414_s2_sed_ES_freeimage_fit.png
- obj6414_s2_sed_ES_freeSED_model.png
- obj6414_s2_sed_ES_free.gsssummary
- obj6414_s2_sed_ES_free.params
- obj6414_s2_sed_ES_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - same question as round 4

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - yes

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes 
  - Whether BIC indicates a better model (if comparison exists)
    - no significant change.
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes 
  - Check if parameters are close to min/max limits
    - no 
              

**5. Next-Step Decision**: 

- Adjust existing component parameters
  - update parameters (--readsummary xxx.gssummary)
  -  using optimizer method to go further on.
**6. reasons for next step**

- optimizer method would be better in finding best-fit values.



### Round 6
**1. 拟合所需的初始参数配置文件**

- 6414/results/sed/opt_free/obj6414_s2_sed_opt_free.lyric

```bash 
galfits 6414/results/sed/opt_free/obj6414_s2_sed_opt_free.lyric --workplace 6414/results/sed/opt_free --fit_method ES --prior 6414/obj6414.prior --readsummary 6414/results/sed/ES_free/obj6414_s2_sed_ES_free.gssummary
```


**2. 拟合输出文件名**

- obj6414_s2_sed_opt_freeimage_fit.png
- obj6414_s2_sed_opt_freeSED_model.png
- obj6414_s2_sed_opt_free.gsssummary
- obj6414_s2_sed_opt_free.params
- obj6414_s2_sed_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - same as round 4

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no
- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes 
  - Whether BIC indicates a better model (if comparison exists)
    - no significant change in comparison with round 5.
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

