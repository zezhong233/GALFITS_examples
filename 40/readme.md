
### Round 1
**1. 拟合所需的初始参数配置文件**

- 40/results/nosed/s1/obj40_s1.lyric
```bash 
galfits 40/results/nosed/s1/obj40_s1.lyric --workplace 40/results/nosed/s1 --fit_method ES 
```


**2. 拟合输出文件名**

- obj40_s1image_fit.png
- obj40_s1.gsssummary
- obj40_s1.params
- obj40_s1.constrain 


**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - obvious central excess and blue/red residual alternate in ratial direction.
    - several small companions around the primary source.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed
  - Check whether systematic offsets exist across wavelengths
    - no sed 
- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, all chi-2 is larger than 1, especially 277w and 356w.
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

- features mentioned in image question part indicate a bulge-like component to be added.

- parameters changing:
  - new disk:
    - n: change initial guess as 1
  - bulge:
    - n: set initial guess as 4
    - R_e(0.20): slightly reducing it compared with disk(0.33).



### Round 2
**1. 拟合所需的初始参数配置文件**

- 40/results/nosed/s2/obj40_s2.lyric

```bash 
galfits 40/results/nosed/s2/obj40_s2.lyric --workplace 40/results/nosed/s2 --fit_method ES 
```
  

**2. 拟合输出文件名**

- obj40_s2image_fit.png
- obj40_s2.gsssummary
- obj40_s2.params
- obj40_s2.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - residual is very asymmetric and no obvious structure pattern indicating a new component, though residual is not good enough.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, but improves a lot in comparison with single sersic
  - Whether BIC indicates a better model (if comparison exists)
    - yes.
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - disk axis ratio reach the boundary (1).
              

**5. Next-Step Decision**: 

- Ready for SED Fitting


**6. reasons for next step**

- though the residual is not good enough, but there isn't obvious signiture indicating a certain component / gssummary parameters are reasonable(axis ratio = 1 i think is not a big problem.)


### Round 3
**1. 拟合所需的初始参数配置文件**

- 40/mass_guess/total/40_total_pure_sed.lyric

```bash 
galfits 40/mass_guess/total/40_total_pure_sed.lyric --workplace 40/mass_guess/total/results --fit_method ES --prior 40/mass_guess/total/40.prior 
```

**2. 拟合输出文件名**


- 40_SED_model.png
- 40.gsssummary
- 40.params
- 40.constrain 


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
    - cause error is estimated very simply, so here's chi-2 is not meaningful 
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison 
  - Whether the fitting process has converged
    - yes 
  - Check whether parameters are physically reasonable
    - yes 
  - Check if parameters are close to min/max limits
    - f_cont_bin4 reach the boundary (0)
              

**5. Next-Step Decision**: 

- Ready for Image-SED Fitting

**6. reasons for next step**

- sed plot tells us it's a good fit for all model points are  close to observed points and no systematic offset / gssummary parameters are reasonable(i think f_cont reaching the limit doesn't a big deal).

- parameters chaning 
  - fix geo parameters 
  - free sed parameters
    - f_cont/A_v/Z: using the best fit value of this step as initial guess.
    - mass: using best_fit mass of this step minus ~0.3 dex as initial guess of tow components.

### Round 4
**1. 拟合所需的初始参数配置文件**

- 40/results/sed/ES_fix/obj40_s2_sed.lyric

```bash 
galfits 40/results/sed/ES_fix/obj40_s2_sed.lyric --workplace 40/results/sed/ES_fix --fit_method ES --prior 40/40.prior 
```

**2. 拟合输出文件名**


- obj40_s2_sedimage_fit.png
- obj40_s2_sedSED_model.png
- obj40_s2_sed.gsssummary
- obj40_s2_sed.params
- obj40_s2_sed.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - almost same asymmetric patterns as round 2.

- sed plot
  - Check whether model points are close to observed points overall
    - yes 
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, but for this very complex source it can be accepted.
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison (increased in comparison with nosed fitting for sed constrain addition.)
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no

**5. Next-Step Decision**: 

- Adjust existing component parameters

**6. reasons for next step**

- free geo parameters 
- update parameters(using --readsummary xxx.gssummary)

### Round 5
**1. 拟合所需的初始参数配置文件**

- 40/results/sed/ES_free/obj40_s2_sed_ES_free.lyric

```bash 
galfits 40/results/sed/ES_free/obj40_s2_sed_ES_free.lyric --workplace 40/results/sed/ES_free --fit_method ES --prior 40/40.prior --readsummary 40/results/sed/ES_free/obj40_s2_sed_ES_free.gssummary 
```

**2. 拟合输出文件名**


- obj40_s2_sed_ES_freeimage_fit.png
- obj40_s2_sed_ES_freeSED_model.png
- obj40_s2_sed_ES_free.gsssummary
- obj40_s2_sed_ES_free.params
- obj40_s2_sed_ES_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - almost same asymmetric patterns as round 2.

- sed plot
  - Check whether model points are close to observed points overall
    - yes 
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, but for this very complex source it can be accepted.
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

- using optimizer method to fit again



### Round 6
**1. 拟合所需的初始参数配置文件**

- 40/results/sed/opt_free/obj40_s2_sed_opt_free.lyric 

```bash 
galfits 40/results/sed/opt_free/obj40_s2_sed_opt_free.lyric --workplace 40/results/sed/opt_free --fit_method optimizer --num_steps 20000 --prior 40/40.prior --readsummary 40/results/sed/ES_free/obj40_s2_sed_ES_free.lyric
```

**2. 拟合输出文件名**


- obj40_s2_sed_opt_freeimage_fit.png
- obj40_s2_sed_opt_freeSED_model.png
- obj40_s2_sed_opt_free.gsssummary
- obj40_s2_sed_opt_free.params
- obj40_s2_sed_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - almost same asymmetric patterns as round 2.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, but for this very complex source it can be accepted.  
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
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

