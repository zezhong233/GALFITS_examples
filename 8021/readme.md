
### Round 1
**1. 拟合所需的初始参数配置文件**

- 8021/results/nosed/s1/obj8021_s1.lyric
```bash 
galfits 8021/results/nosed/s1/obj8021_s1.lyric --workplace 8021/results/nosed/s1 --fit_method ES 
```

**2. 拟合输出文件名**

- obj8021_s1_nosedimage_fit.png
- obj8021_s1_nosed.gsssummary
- obj8021_s1_nosed.params
- obj8021_s1_nosed.constrain 


**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - There are obvious central in long wavelength bands(277w, 356w, 410m, 444w) and blue/red residual alternate in ratial direction in 115w, 150w, 200w, 277w.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes. all are below 1, but in experience, it can be smaller.
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

- the image residual feature indicates a bulge-like component.
- parameters changing
  - new disk:
    - n: changing initial guess as 1
  - bulge:
    - n: set initial guess as 4
    - R_e: slightly reducing it(0.1) compared with that of disk(0.2)




### Round 2
**1. 拟合所需的初始参数配置文件**

-  8021/results/nosed/s2/obj8021_s2.lyric

```bash 
galfits 8021/results/nosed/s2/obj8021_s2.lyric --workplace 8021/results/nosed/s2 --fit_method ES 
```

**2. 拟合输出文件名**

- obj8021_s2_nosedimage_fit.png
- obj8021_s2_nosed.gsssummary
- obj8021_s2_nosed.params
- obj8021_s2_nosed.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious structure's feature except for some small clump.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes
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

- there is no obvious features in the residual map. small clumps are the sub-structure of galaxy and we don't want to care currently.


### Round 3
**1. 拟合所需的初始参数配置文件**

- 8021/mass_guess/total/8021_total_pure_sed.lyric

```bash 
galfits 8021/mass_guess/total/8021_total_pure_sed.lyric --workpalce 8021/mass_guess/total/results --fit_method ES --prior 8021/mass_guess/total/obj8021.prior
```

**2. 拟合输出文件名**

- 8021SED_model.png
- 8021.gsssummary
- 8021.params
- 8021.constrain 


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
    - It's not meaningful for the oversimplified error estimation.
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

- all bands' model points and data points fit very well.

- parameters changing
  - fix geo parameters 
    - using round 2's best fitting value as initial guess.
  - free sed parameters
    - f_cont/A_v/Z: using best fitting value of this step as initial guess.
    - mass: using best fitting value - ~0.3dex as initial guess of disk/bulge.



### Round 4
**1. 拟合所需的初始参数配置文件**

- 8021/results/sed/ES_fix/obj8021_s2_ES_fix.lyric

```bash 
galfit 8021/results/sed/ES_fix/obj8021_s2_ES_fix.lyric --workpalce 8021/results/sed/ES_fix --fit_method ES --prior 8021/obj8021.prior 
```

**2. 拟合输出文件名**

- obj8021_s2_ES_fiximage_fit.png
- obj8021_s2_ES_fixSED_model.png
- obj8021_s2_ES_fix.gsssummary
- obj8021_s2_ES_fix.params
- obj8021_s2_ES_fix.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious remaining structures. 

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

- Adjust existing component parameters

**6. reasons for next step**

- image residual is relatively clear / sed plot data points and model points fit well / gssummary parameters are reasonable.

- parameters changing
  - free geo parameters 
  - update the parameters (using --readsummary xxx.gssummary)


### Round 5
**1. 拟合所需的初始参数配置文件**

- 8021/results/sed/ES_free/obj8021_s2_ES_free.lyric

```bash 
galfits 8021/results/sed/ES_free/obj8021_s2_ES_free.lyric --workplace 8021/results/sed/ES_free --fit_method ES --prior 8021/obj8021.prior --readsummary 8021/results/sed/ES_fix/obj8021_s2_ES_fix.gssummary
```

**2. 拟合输出文件名**


- obj8021_s2_ES_freeimage_fit.png
- obj8021_s2_ES_freeSED_model.png
- obj8021_s2_ES_free.gsssummary
- obj8021_s2_ES_free.params
- obj8021_s2_ES_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious remaining structures.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable ranges
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
  - using optimizer method to g further.


**6. reasons for next step**

- image residual is clear / sed plot data points and model points fit well / gssummary parameters seems reasonable.


### Round 6
**1. 拟合所需的初始参数配置文件**

- 8021/results/sed/opt_free/obj8021_s2_opt_free.lyric

```bash
galfits 8021/results/sed/opt_free/obj8021_s2_opt_free.lyric --workplace 8021/results/sed/opt_free --fit_method optimizer --num_steps 20000 --prior 8021/obj8021.prior --readsummary 8021/results/sed/opt_free/obj8021_s2_opt_free.gssummary
```

**2. 拟合输出文件名**

- obj8021_s2_opt_freeimage_fit.png
- obj8021_s2_opt_freeSED_model.png
- obj8021_s2_opt_free.gsssummary
- obj8021_s2_opt_free.params
- obj8021_s2_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious remaining structures.

- sed plot
  - Check whether model points are close to observed points overall
    - yes 
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - yes
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison(but BIC reduced a bit in comparison with ES method)
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes
  - Check if parameters are close to min/max limits
    - some f_cont bins reach boundary(bulge_f_cont_bin2/5), but it's not a big deal.
              

**5. Next-Step Decision**: 

- Stop fitting

**6. reasons for next step**

- xxx


