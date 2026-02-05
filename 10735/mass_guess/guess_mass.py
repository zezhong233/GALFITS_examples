import os
os.environ['XLA_PYTHON_CLIENT_PREALLOCATE']='false'
import numpy as np
from astropy.table import Table, vstack
from astropy.io import ascii
import sys
sys.path.append("/home/zhongyi/work/GALFITS/GalfitS/code/GalfitS/src/galfits")
sys.path.append("/home/zhongyi/work/GALFITS")
from galfits import gsutils
from string_functions import store_flux_err_tocat
from galfits_puresed_zgrid_nestedsampling import genomckdata, run_galfits, genlyric

idx_name = 10735



## read galfits results 
root_dir = "/home/zhongyi/work/GALFITS/DATA/ZHIJIANG/P6" ## path change 

config_path = os.path.join(root_dir, f"{idx_name}/obj10735_s2_com.lyric")
workplace = os.path.join(root_dir, f"{idx_name}/results")
band_lists = ["115w", "150w", "200w", "277w", "356w", "410m", "444w"]

Myfitter, targ, fs = gsutils.read_config_file(config_path, workplace)

smfile = ascii.read(f"{workplace}/{targ}.gssummary")


for loopx in range(len(smfile)):
    Myfitter.lmParameters[smfile['pname'][loopx]].value = smfile["best_value"][loopx] ## load the best fitting results

Myfitter.loose_fix_pars()
Myfitter.cal_model_image()

## read the model flux 



fluxs_total = np.array([0.]*7)

model_idx = 0 ## model index of profiles, like galaxy_1, galaxy_2, agn, in which there may be multi components, like disk, bulge etc.
model_name = "galaxy_1" ## the name of this {model idx} model.
# model_subcom_name = "com_1" ## the component of this {model_idx} model.
dir_name = "total"

for model_subcom_name in Myfitter.model_list[model_idx].subnames:
    fluxs = []
    for idx_band in range(len(band_lists)):

        im = Myfitter.GSdata.get_image(idx_band)
        zp = im.magzp
        logNorm = Myfitter.pardict[f"logNorm_{model_subcom_name}_nircam_f{band_lists[idx_band]}"]
        logMass = Myfitter.pardict[f"logM_{model_subcom_name}"]

        mag_best_2 = zp - 2.5*(logNorm + logMass) ## key 

        flux_uJy = 3631*10**( - mag_best_2 / 2.5) * 10**3 ## from magnitude to flux (m Jy)
        print("the mag read from gssummary is ", mag_best_2, "flux(muJy) is ", flux_uJy)
        fluxs.append(flux_uJy)
    fluxs = np.array(fluxs)
    fluxs_total += fluxs
    


# print(Myfitter.pardict)
fluxs_err = 0.1 * fluxs_total ## for simplicity, we just assume err is 0.1 * flux.

cat_content = []

for i in range(len(fluxs_total)):
    cat_content.append(fluxs_total[i])
    cat_content.append(fluxs_err[i])


mass_guess_dir = os.path.join(root_dir, f"{idx_name}/mass_guess")
cat_file = f"{mass_guess_dir}/{idx_name}_{dir_name}_flux_err.cat"


store_flux_err_tocat(cat_file, idx_name, cat_content)


z_fix = Myfitter.pardict[f"z_{model_name}"]
print(z_fix)


sci_paths = os.path.join(root_dir, f"{idx_name}") ## path change
mockpath = os.path.join(root_dir, f"{idx_name}/mass_guess/{dir_name}") ## path change 
lyric_file = os.path.join(mockpath, f"{idx_name}_{dir_name}_pure_sed.lyric")
workplace = os.path.join(mockpath, f"results")

os.makedirs(workplace, exist_ok=True)


genomckdata(cat_file = cat_file, galid = idx_name, mockpath = mockpath)

genlyric(cat_file=cat_file, galid = idx_name, lyric_file = lyric_file, scipath = sci_paths, 
         mockpath = mockpath, z_fit=z_fix)

# run_galfits(galid = idx_name, lyric_file = lyric_file, workplace = workplace)



