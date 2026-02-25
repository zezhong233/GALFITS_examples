
### Round 1
**1. 拟合所需的初始参数配置文件**

- 13347/results/nosed/s1/obj13347_s1.lyric

```bash
galfits 13347/results/nosed/s1/obj13347_s1.lyric --workplace 13347/results/nosed/s1
```

**2. 拟合输出文件名**

- obj13347_s1_nosedimage_fit.png
- obj13347_s1_nosed.gsssummary
- obj13347_s1_nosed.params
- obj13347_s1_nosed.constrain 

**3. overall Judgement**

- Bad fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - central excess and red/blue residual alternate in ratial direction.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no , all large than 1
  - Whether BIC indicates a better model (if comparison exists)
    -  no comparison
  - Whether the fitting process has converged
    - yes
  - Check whether parameters are physically reasonable
    - yes 
  - Check if parameters are close to min/max limits
    - no
              

**5. Next-Step Decision**: 

- Add a bulge-like Sérsic component

**6. reasons for next step**

- the question described in image question indicate an extended component.

- parameters changing 
  - new disk:
    - n: set 1 as the initial guess
  - bulge:
    - n: set 4 as initial guess 
    - Re: slightly reducing the Re(0.15) compared with disk(0.27)


### Round 2
**1. 拟合所需的初始参数配置文件**

- 13347/results/nosed/s2/obj13347_s2.lyric

```bash
galfits 13347/results/nosed/s2/obj13347_s2.lyric --workplace 13347/results/nosed/s2 --fit_method ES 
```

**2. 拟合输出文件名**

- obj13347_s2_nosedimage_fit.png
- obj13347_s2_nosed.gsssummary
- obj13347_s2_nosed.params
- obj13347_s2_nosed.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - no obvious remaining structure except for spiral arm with m=2.

- sed plot
  - Check whether model points are close to observed points overall
    - no sed 
  - Check whether systematic offsets exist across wavelengths
    - no sed 

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - no, all large than 1.
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

-  image: only spiral arm structure can be clearly distinguished and we don't care about it currently. / gssummary: parameters are reasonable and do not reach the boundary.


### Round 3
**1. 拟合所需的初始参数配置文件**

- 13347/mass_guess/total/13347_total_pure_sed.lyric

```bash
galfits 13347/mass_guess/total/13347_total_pure_sed.lyric --workplace 13347/mass_guess/total/results --fit_method ES --prior 13347/mass_guess/total/obj13347.prior 
```

**2. 拟合输出文件名**

- 13347SED_model.png
- 13347.gsssummary
- 13347.params
- 13347.constrain 

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

- sed plot: model points fit well with data points / gssummary: parameters are reasonable and do not reach the boundary.
- parameter changing
  - update and fix geo parameters (using best fitting value of round 2)
  - free sed parameters
    - f_cont/A_v/Z: using the best value of this steps as initial guess
    - mass: using best mass - ~0.3 mass as the initial guess of disk and bulge.

### Round 4
**1. 拟合所需的初始参数配置文件**

- 13347/results/sed/ES_fix/obj13347_s2_ES_fix.lyric

```bash
galfits 13347/results/sed/ES_fix/obj13347_s2_ES_fix.lyric --workplace 13347/results/sed/ES_fix --fit_method ES --prior 13347/obj13347.prior
```

**2. 拟合输出文件名**

- obj13347_s2_ES_fiximage_fit.png
- obj13347_s2_ES_fixSED_model.png
- obj13347_s2_ES_fix.gsssummary
- obj13347_s2_ES_fix.params
- obj13347_s2_ES_fix.constrain 

**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - only spiral arm structure can be clearly distinguished and all bands' residual images get worse for the sed constraint.

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - acceptable...
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

- image: though image residual get worse for sed constraint, i think it's acceptable. / sedplot: model points fit well with data points/ gssummary: parameters are reasonable and no reach the boundary.


### Round 5
**1. 拟合所需的初始参数配置文件**

- 13347/results/sed/ES_free/obj13347_s2_ES_free.lyric

```bash
galfits 13347/results/sed/ES_free/obj13347_s2_ES_free.lyric --workplace 13347/results/sed/ES_free --fit_method ES --prior 13347/obj13347.prior 
```

**2. 拟合输出文件名**

- obj13347_s2_ES_freeimage_fit.png
- obj13347_s2_ES_freeSED_model.png
- obj13347_s2_ES_free.gsssummary
- obj13347_s2_ES_free.params
- obj13347_s2_ES_free.constrain 


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
    - acceptable
  - Whether BIC indicates a better model (if comparison exists)
    - no model comparison(but BIC slightly reduced compared with round 4)
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

- optimizer method can find a better set of parameters than ES.


### Round 6
**1. 拟合所需的初始参数配置文件**

- 13347/results/sed/opt_free/obj13347_s2_opt_free.lyric

```bash
galfits 13347/results/sed/opt_free/obj13347_s2_opt_free.lyric --workplace 13347/results/sed/opt_free --fit_method ES --prior 13347/obj13347.prior --readsummary 13347/results/sed/opt_free
```

**2. 拟合输出文件名**

- obj13347_s2_opt_freeimage_fit.png
- obj13347_s2_opt_freeSED_model.png
- obj13347_s2_opt_free.gsssummary
- obj13347_s2_opt_free.params
- obj13347_s2_opt_free.constrain 


**3. overall Judgement**

- Good fit

**4. fitting problems**:

- image 
  - Check whether there are obvious remaining structures (e.g., central excess, rings, bars, asymmetric patterns)
    - same situation as round 4

- sed plot
  - Check whether model points are close to observed points overall
    - yes
  - Check whether systematic offsets exist across wavelengths
    - no

- gssummary
  - Whether the reduced chi-square is within a reasonable range
    - large than 1 but i think its acceptable.
  - Whether BIC indicates a better model (if comparison exists)
    - no comparison( slightly better than round 5)
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