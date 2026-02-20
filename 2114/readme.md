### Round 1
**1. 拟合所需的初始参数配置文件**

- 2114/results/nosed/s1/obj2114_s1.lyric

```bash 
galfits 2114/results/nosed/s1/obj2114_s1.lyric --workplace 2114/results/nosed/s1 --fit_method ES --num_generations 10000
```

**2. 拟合输出文件名**

- obj2114_s1_nosed_1image_fit.png
- obj2114_s1_nosed_1.gsssummary
- obj2114_s1_nosed_1.params
- obj2114_s1_nosed_1.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - There is obvious bar-like structure in y axis in the data column and the single sersic component is trying to fitting it so it's reddish in horizontal irection and bluish in the vertical direction.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - BIC is larger than 1 overall, not a good fit
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Add a bar-like Sérsic component

**6. reasons for next step**

- obvious bar-like structure in data.
  
- parameters changing
  - new disk:
    - changing n to 1 
    - slightly enlarging q to 0.6
    - set the initial PA to 0.(for the guess from galfitX if biased by bar)
  - bar 
    - fix n as 0.5
    - slightly decreasing q to 0.3
    - using the PA best value of s1 fitting as initial guess.(the s1 is trying to fit bar)



### Round 2
**1. 拟合所需的初始参数配置文件**

- 2114/results/nosed/s2/obj2114_s2_dbar.lyric

```bash 
galfits 2114/results/nosed/s2/obj2114_s2_dbar.lyric --workplace 2114/results/nosed/s2 --fit_method ES --num_generations 10000
```

**2. 拟合输出文件名**

- obj2114_s2_dbarimage_fit.png
- obj2114_s2_dbar.gsssummary
- obj2114_s2_dbar.params
- obj2114_s2_dbar.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - obvious spiral arm and central component.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - better than s1 fitting 
  - Whether BIC indicates a better model (if comparison exists)
    - better than s1 fitting 
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Add a bulge-like Sérsic component


**6. reasons for next step**

- obvious compact structure(for the degeneracy of compact bulge and agn, we will using agn only when we've already known there is a agn or the bulge fitting's R_e is very small)

- parameters changing
  - bulge 
    - very small initial R_e (0.04) and give a reasonable changing range(0.01-0.20).
    - setting initial n as 4.
    - setting PA as 0.(for no enough info to guess PA)
    - setting q as same as disk 


### Round 3
**1. 拟合所需的初始参数配置文件**

- 2114/results/nosed/s3/obj2114_s3_dbbar.lyric

```bash 
galfits 2114/results/nosed/s3/obj2114_s3_dbbar.lyric --workplace 2114/results/nosed/s3 --fit_method ES --num_generations 20000
```

**2. 拟合输出文件名**

- obj2114_s3_dbbarimage_fit.png
- obj2114_s3_dbbar.gsssummary
- obj2114_s3_dbbar.params
- obj2114_s3_dbbar.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - obvious spiral structure

- sed plot
  - Check whether model points are close to observed points overall
    - no sed
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - all lower than 1, better than s2. 
  - Whether BIC indicates a better model (if comparison exists)
    - better than s2
  - Whether the fitting process has converged
    - yes 
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no 
              

**5. Next-Step Decision**: 

- Ready for SED Fitting


**6. reasons for next step**
-  don't consider spiral arm structure currently



### Round 4
**1. 拟合所需的初始参数配置文件**

- 2114/mass_guess/total/2114_total_pure_sed.lyric

```bash 
galfits 2114/mass_guess/total/2114_total_pure_sed.lyric --workplace 2114/mass_guess/total/results --fit_method ES --num_generations 10000 --prior 2114/mass_guess/total/2114.prior 
```

**2. 拟合输出文件名**

- 2114.png
- 2114.gsssummary
- 2114.params
- 2114.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no image. 

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - not physical(for over-simplified error estimation)
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
- sed plot doesn't show significant offset; parameters in gssummary are reasonable.

- parameters changing 
  - using pure sed fitting best results as the initial guess of sed+image fitting.
  - fix geo parameters and free sed params 




### Round 5
**1. 拟合所需的初始参数配置文件**

- 2114/results/sed/ES_fix/obj2114_s3_dbbar_sed_ES_fix.lyric

```bash 
galfits 2114/results/sed/ES_fix/obj2114_s3_dbbar_sed_ES_fix.lyric --workplace 2114/results/sed/ES_fix --fit_method ES --num_generations 10000 --prior 2114/prior.prior
```

**2. 拟合输出文件名**

- obj2114_s3_dbbar_sed_ES_fix.png
- obj2114_s3_dbbar_sed_ES_fix.gsssummary
- obj2114_s3_dbbar_sed_ES_fix.params
- obj2114_s3_dbbar_sed_ES_fix.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure except for spiral arm; no significant depravation in comparison with nosed fitting.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
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

  - update parameters(just --readsummary xxx.gssuuamry)
  - free geo parameters


**6. reasons for next step**

- image no significant depravation in comparison with nosed fitting / sed plot doesn't show significant offset / parameters in gssummary is reasonable and don't reach the boundary.


### Round 6
**1. 拟合所需的初始参数配置文件**

- 2114/results/sed/ES_free/obj2114_s3_dbbar_sed_ES.lyric

```bash 
galfits 2114/results/sed/ES_free/obj2114_s3_dbbar_sed_ES.lyric --workplace 2114/results/sed/ES_free --fit_method ES --num_generations 10000 --prior 2114/prior.prior --readsummary 2114/results/sed/ES_fix/obj2114_s3_dbbar_sed_ES_fix.gssummary
```

**2. 拟合输出文件名**

- obj2114_s3_dbbar_sed_ES_free.png
- obj2114_s3_dbbar_sed_ES_free.gsssummary
- obj2114_s3_dbbar_sed_ES_free.params
- obj2114_s3_dbbar_sed_ES_free.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure except for spiral arm; no significant depravation in comparison with nosed fitting.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes
  - Whether BIC indicates a better model (if comparison exists)
    - BIC reduced in comparison with ES_fix fitting.
  - Whether the fitting process has converged
    - yes 
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - no 
              

**5. Next-Step Decision**: 

- update parameters 
- using optimizer method to go further on.

**6. reasons for next step**

- optimizer method would be better in finding best-fit values.





### Round 7
**1. 拟合所需的初始参数配置文件**

- 2114/results/sed/opt_free/obj2114_s3_dbbar_sed_opt.lyric

```bash 
galfits 2114/results/sed/opt_free/obj2114_s3_dbbar_sed_opt.lyric --workplace 2114/results/sed/opt_free --fit_method ES --num_generations 10000 --prior 2114/prior.prior --readsummary 2114/results/sed/ES_free/obj2114_s3_dbbar_sed_ES_free.gssummary
```

**2. 拟合输出文件名**

- obj2114_s3_dbbar_sed_opt_free.png
- obj2114_s3_dbbar_sed_opt_free.gsssummary
- obj2114_s3_dbbar_sed_opt_free.params
- obj2114_s3_dbbar_sed_opt_free.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure except for spiral arm; no significant depravation in comparison with nosed fitting.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes
  - Whether BIC indicates a better model (if comparison exists)
    - BIC reduced in comparison with ES_free fitting.
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













