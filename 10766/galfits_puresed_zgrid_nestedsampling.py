import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
os.environ["XLA_PYTHON_CLIENT_PREALLOCATE"] = "false"
import sys
import numpy as np
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy.table import Table
from astropy import units as u
from galfits import gsutils
from galfits.sed_interp import cosmo_age
from astropy.cosmology import Planck18 as cosmo

from jax.lax import clamp
import jax.numpy as jnp
from astropy.wcs import WCS
import pandas as pd
import pickle

def fnu2flambada(lc): #ergs/cm2/Angstrom/s
    """
    Convert flux density in Fnu to flux density in Flambda
    """
    # fnu: MJy/sr
    # flambada: erg/cm2/s/Angstrom
    # MJy/sr to MJy/pixel^2 : pixarsr
    # MJy to erg/cm2/s: 1e-17
    c = 2.99792458e18 # Angstrom/s
    # lc: wavelength in Angstrom
    pixarsr = 2.11539874851881e-14
    conversionfactor = pixarsr * 1e-17 * c / (lc**2)    # MJy/sr to erg/cm2/s/Angstrom
    return conversionfactor 


def genlyric(cat_file, galid,lyric_file,scipath,mockpath, z_fit=4.0):
    '''
    galid: int
        galaxy index of your target.
    lyric_file: str
        the output path of lyric file.
    '''
    #Images
    # scipath = '/mnt/data/JWST/SMACS0723/cutout_all/'+str(galid)+'/' ## sci path change 
    # mockpath = '/home/lailimin/GalfitS/2steps/puresed/nested_sampling/'+str(galid)+'/data/' ## mock path change 

    #JWST
    bands = ['115w', '150w', '200w', '277w', '356w', '410m', '444w']
    imagels = ['a','b','c','d','e','f','g']

    lcs = [11500,15000, 20000, 27700, 35600, 41000, 44400]
    fluxcat = Table.read(cat_file, format='ascii') ## how to get flux catalog ?
    object_flux = fluxcat[fluxcat['id']==galid] ## find index 
    imgatlas = []
    
    header = fits.getheader(os.path.join(scipath,"f277w.fits")) ## name change 
    shape = fits.getdata(os.path.join(scipath, "f277w.fits")).shape ## name change 
    ra,dec = WCS(header).all_pix2world((shape[0]+1)/2, (shape[1]+1)/2, 1)

    param_file = open(lyric_file,'w')
    param_file.write("# This is a galfitS configuration file for galaxy "+str(galid)+"\n")
    param_file.write("# The config file provide a galfitS setup to perform a single sersic SED fitting with multi-band images.\n")

    # Region information
    param_file.write("# Region information\n")
    param_file.write('R1) '+str(galid)+'\n')  # name of the target
    param_file.write('R2) ['+str(ra)+','+str(dec)+']\n')  # sky coordinate of the target [RA, Dec]
    param_file.write('R3) '+str(z_fit)+' \n\n') # redshift of the target

    for idx in [0,1,2]:
        # NIRCam
        band = bands[idx]
        imagel = imagels[idx]
        if object_flux[f"nircam_f{band}_flux"] > -90:
            imgatlas.append(imagel)
        else:
            continue
        #print('band:', band)
        scifile = os.path.join(scipath,f'f{band}.fits') ## name change
        mockfile = os.path.join(mockpath, 'nircam_f' + band + '.fits') # mock path ?
        # conversionfact = 1/fnu2flambada(lcs[idx])
        #print('conversionfact:', conversionfact)
        param_file.write('# Image '+imagel.upper()+' \n')
        param_file.write('I'+imagel+'1)  [' + mockfile + ',0] \n') #sci image
        param_file.write('I'+imagel+'2)  nircam_f'+band+'\n') # band name
        param_file.write('I'+imagel+'3)  [' + mockfile + ',2] \n') # sigma image
        param_file.write('I'+imagel+'4)  [' + mockfile + ',3]\n') #psf image
        param_file.write('I'+imagel+'5)  1\n') # PSF fine sampling factor relative to data
        param_file.write('I'+imagel+'6)  [Noimg,0]\n') #mask image
        param_file.write('I'+imagel+'7)  cR\n') # unit of the image
        param_file.write('I'+imagel+'8)  -1 \n') # size to make cutout image region for fitting, unit arcsec
        param_file.write('I'+imagel+'9)  1 \n') # Conversion from image unit to flambda, -1 for default                 ## why ? for pure sed fitting, it must be specified as 1.
        param_file.write('I'+imagel+'10) 28.96697568756239\n') # Magnitude photometric zeropoint                                 ## mag zp calculate
        param_file.write('I'+imagel+'11) uniform\n') # sky model
        param_file.write('I'+imagel+'12) [[0,-0.5,0.5,0.1,0]]\n') # sky parameter, (value, min, max, step)
        param_file.write('I'+imagel+'13) 0\n') # allow relative shifting
        param_file.write('I'+imagel+'14) [[0,-5,5,0.1,0],[0,-5,5,0.1,0]]\n') # [shiftx, shifty]
        param_file.write('I'+imagel+'15) 1\n\n') # Use SED information

    for idx in [3,4,5,6]:
        # NIRCam
        band = bands[idx]
        imagel = imagels[idx]
        if object_flux[f"nircam_f{band}_flux"] > -90:
            imgatlas.append(imagel)
        else:
            continue
        #print('band:', band)
        scifile = os.path.join(scipath,f'f{band}.fits')
        mockfile = os.path.join(mockpath, 'nircam_f' + band + '.fits')
        # conversionfact = 1/fnu2flambada(lcs[idx])
        #print('conversionfact:', conversionfact)
        param_file.write('# Image '+imagel.upper()+' \n')
        param_file.write('I'+imagel+'1)  [' + mockfile + ',0] \n') #sci image
        param_file.write('I'+imagel+'2)  nircam_f'+band+'\n') # band name
        param_file.write('I'+imagel+'3)  [' + mockfile + ',2] \n') # sigma image
        param_file.write('I'+imagel+'4)  [' + mockfile + ',3]\n') #psf image
        param_file.write('I'+imagel+'5)  1\n') # PSF fine sampling factor relative to data
        param_file.write('I'+imagel+'6)  [Noimg,0]\n') #mask image
        param_file.write('I'+imagel+'7)  cR\n') # unit of the image
        param_file.write('I'+imagel+'8)  -1 \n') # size to make cutout image region for fitting, unit arcsec
        param_file.write('I'+imagel+'9)  1 \n') # Conversion from image unit to flambda, -1 for default
        param_file.write('I'+imagel+'10) 27.461825709242483\n') # Magnitude photometric zeropoint                          ## mag zp calculate
        param_file.write('I'+imagel+'11) uniform\n') # sky model
        param_file.write('I'+imagel+'12) [[0,-0.5,0.5,0.1,0]]\n') # sky parameter, (value, min, max, step)
        param_file.write('I'+imagel+'13) 0\n') # allow relative shifting
        param_file.write('I'+imagel+'14) [[0,-5,5,0.1,0],[0,-5,5,0.1,0]]\n') # [shiftx, shifty]
        param_file.write('I'+imagel+'15) 1\n\n') # Use SED information

    # Image atlas
    

    age= round(cosmo.age(z_fit).value,2)-0.2 
    age_list = [0] + list(np.logspace(-1, np.log10(age), 5))


    param_file.write("# Image atlas\n")
    param_file.write("Aa1) 'all'\n") # name of the image atlas
    param_file.write("Aa2) "+str(imgatlas)+"\n") # images in this atlas
    param_file.write('Aa3) 0\n') # whether the images have same pixel size
    param_file.write('Aa4) 0\n') # link relative shiftings
    param_file.write('Aa5) []\n') # spectra
    param_file.write('Aa6) []\n') # aperture size
    param_file.write('Aa7) []\n\n') # references images
    
    param_file.write("# Profile A\n")
    param_file.write('Pa1) total\n') # name of the component
    param_file.write('Pa2) sersic\n') # profile type
    param_file.write('Pa3) [0,-0.3,0.3,0.1,0]\n') # x-center [arcsec]
    param_file.write('Pa4) [0,-0.3,0.3,0.1,0]\n') # y-center [arcsec]
    param_file.write('Pa5) [0.2,0.1,1.7,0.1,0]\n') # effective radius [arcsec]
    param_file.write('Pa6) [2,0.5,6,0.1,0]\n') # Sersic index
    param_file.write('Pa7) [0,-90,90,1,0]\n') # position angle (PA) [degrees: Up=0, Left=90]
    param_file.write('Pa8) [0.8,0.5,1,0.01,0]\n') # axis ratio (b/a) [0.1=round, 1=flat]
    param_file.write(f'Pa9) [[-2,-8,0,0.1,1],[-2,-8,0,0.1,1],[-2,-8,0,0.1,1],[-2,-8,0,0.1,1],[-2,-8,0,0.1,1]]\n') # contemporary log star formation fraction         ## sfr
    param_file.write(f'Pa10) [{round(age_list[0],2)}, {round(age_list[1],2)}, {round(age_list[2], 2)}, {round(age_list[3],2)}, {round(age_list[4],2)}, {round(age_list[5],2)}]\n') # burst stellar age [Gyr]          ## age 
    param_file.write('Pa11) [[0.02,0.001,0.04,0.001,1]]\n') # metallicity [Z=0.02=Solar]
    param_file.write('Pa12) [[0.7,0.3,5.1,0.1,1]]\n') # Av dust extinction [mag]
    param_file.write('Pa13) [100,40,200,1,0]\n') # stellar velocity dispersion
    param_file.write('Pa14) [9,6,12,0.1,1]\n') # log stellar mass
    param_file.write('Pa15) bins \n') # star formation history type: burst/conti                    ## change to bins 
    param_file.write('Pa16) [-2,-4,-2,0.1,0]\n') # logU nebular ionization parameter
    param_file.write('Pa26) [3,0,5,0.1,0]\n') # amplitude of the 2175A bump on extinction curve
    param_file.write('Pa27) 0\n') # SED model, 0: full; 1: stellar only; 2: nebular only; 3: dust only
    param_file.write('Pa28) [8.14,4.5,10,0.1,0]\n') # log dust mass
    param_file.write('Pa29) [1.0, 0.1, 50, 0.1, 0]\n') # Umin, minimum radiation field
    param_file.write('Pa30) [1.0, 0.47, 7.32, 0.1, 0]\n') # qPAH, mass fraction of PAH
    param_file.write('Pa31) [1.0, 1.0, 3.0, 0.1, 0]\n') # alpha, powerlaw slope of U
    param_file.write('Pa32) [0.1, 0, 1.0, 0.1, 0]\n\n') # gamma, fraction illuminated by star forming region

    # Galaixes
    param_file.write("# Galaxy A\n")
    param_file.write('Ga1) mygal\n') # name of the galaxy
    param_file.write("Ga2) ['a']\n") # profile component
    param_file.write('Ga3) ['+str(z_fit)+',0.01,12.0,0.01,0]\n') # galaxy redshift
    param_file.write('Ga4) 0.01\n') # the EB-V of Galactic dust reddening 
    param_file.write('Ga5) [1.0,0.5,2,0.05,0]\n') # normalization of spectrum when images+spec fitting
    param_file.write('Ga6) []\n') # narrow lines in nebular
    param_file.write('Ga7) 1\n\n') # number of components for narrow lines

    param_file.close()

def genomckdata(cat_file, galid, mockpath, z_fit=4.0): ## generate mock data 

    # read flux catalog
    fluxcat = Table.read(cat_file, format='ascii') ## how to get flux catalog ?
    object_flux = fluxcat[fluxcat['id']==galid]
    # object_bands = ['115w','150w', '200w', '277w', '356w', '410m', '444w']
    Bands = ['nircam_f115w','nircam_f150w','nircam_f200w','nircam_f277w','nircam_f356w','nircam_f410m', 'nircam_f444w']
    
    if os.path.exists(mockpath):

        pass
    else:
        os.mkdir(mockpath)
    # Create a directory to store the output images
    for loop, band in enumerate(Bands):
        # nband = object_bands[loop]
        # flux_mjy = object_flux['f_' + nband]
        flux_mjy = object_flux[f"{band}_flux"].value
        if flux_mjy < -90.:
            continue
        # flux_err = object_flux['e_' + nband]
        flux_err = object_flux[f"{band}_fluxerr"].value 
        outputname = os.path.join(mockpath,f"{band}.fits")
        print(band, flux_mjy, flux_err)
        gsutils.photometry_to_img(band, flux_mjy, flux_err, z_fit, outputname, unit='mJy') ## create mock image !

def run_galfits(galid, lyric_file, workplace):

    Myfitter,targ,fs = gsutils.read_config_file(lyric_file,workplace)

    # add a new parameter to normalize the age
    Myfitter.lmParameters.add('normage_total', 0.1, min=0.001, max = 1, brute_step = 0.001,vary = True)
    Myfitter.loose_fix_pars()
    # define the constrain
    def Update_Constraints(pardictlc):
        age = pardictlc['normage_total']*cosmo_age(pardictlc['z_mygal']-0.2)
        pardictlc['total_age_value'] = clamp(0.01,age,13.6) ## 数值截断函数，把age 限制在0.01,13.6中间
    Myfitter.Set_Update_Constraints(Update_Constraints)
    # ES
    #fr = Myfitter.evolution_strategies_theta(num_generations=10000, popsize=20)
    #fr = Myfitter.optimizer_theta(num_steps=10000, learning_rate = 1e-4,optimizer='adamax')
    #fr = Myfitter.optimizer_zgrid([0.1,0.2,0.3,0.4,0.5,0.6,0.7],num_steps=3000, learning_rate = 5e-4)
    #pltwave, Sedcomp, Sedlabel, z = Myfitter.cal_model_image()
    fr = Myfitter.nested_sampling(nlive=100,maxiters=10000)

    result_dict = {
        'varnames': Myfitter.varnames,
        'samples': fr['samples'],
        'best_theta': fr['best_theta'],
        'uncertainty': fr['uncertainty'],
    }

    with open('/home/lailimin/GalfitS/2steps/puresed/nested_sampling/'+str(galid)+'/results_dict.pickle', 'wb') as file:
        pickle.dump(result_dict, file)


    pltwave, Sedcomp, Sedlabel, z = Myfitter.cal_model_image()


    wrange = [0.85,1.15]
    pltwave[0] = np.array(pltwave[0])
    pltwave[1] = np.array(pltwave[1])
    pltwave[3] = np.array(pltwave[3])
    waverange = [np.min(pltwave[0]),np.max(pltwave[0])]
    if np.max(pltwave[0])/np.min(pltwave[0]) > 10:
        wavegrid = np.logspace(np.log10(wrange[0]*waverange[0]),np.log10(wrange[1]*waverange[1]),1000)
    else:
        wavegrid = np.linspace(wrange[0]*waverange[0],wrange[1]*waverange[1],1000)
    fig = plt.figure(figsize=(9,6))
    ax = plt.gca()
    plt.xlim([wrange[0]*waverange[0],wrange[1]*waverange[1]])
    plt.errorbar(pltwave[0],pltwave[1]*pltwave[0],yerr=pltwave[2]*pltwave[0],fmt='o',color='k',label=r'$L_\mathrm{tot}$ cut image',alpha=0.7)
    plt.errorbar(pltwave[0],pltwave[3]*pltwave[0],fmt='o',color='r',label=r'$L_\mathrm{tot}$ model image',alpha=0.7)
    sedtot = np.zeros(len(wavegrid))
    for loop in range(len(Sedcomp)):
            plt.plot(wavegrid,wavegrid*Sedcomp[loop],label=Sedlabel[loop],lw=2,alpha=0.7)
            sedtot += Sedcomp[loop]
    plt.plot(wavegrid,wavegrid*sedtot,label='sed_total',lw=2,alpha=0.7,linestyle='--')  
    plt.xlabel(r'Observed Wavelength ($\mathring{\rm A}$)', fontsize=19)
    plt.ylabel(r'$\lambda L_\lambda \; (10^{38} \, \rm erg\,s^{-1})$', fontsize=19)
    plt.ylim([0.33*np.min(pltwave[3]*pltwave[0]),3*np.max(pltwave[3]*pltwave[0])])

    if np.max(pltwave[0])/np.min(pltwave[0]) > 10:
        plt.xscale('log')
        plt.yscale('log')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5), fontsize=12, numpoints=1, frameon=False)
    plt.text(1.05, 0.8, r'$\chi^2_{red}$ = %.2f' % (Myfitter.chisq), fontsize=16, transform=ax.transAxes)
    plt.text(1.05, 0.9, r'$z_{best}$ = %.2f' % (fr['best_theta'][result_dict['varnames'].index('z_mygal')]), fontsize=16, transform=ax.transAxes)
    # make a upper x-axis labeled by rest wavelength
    ax2 = plt.twiny()
    ax2.set_xlim([wrange[0]*waverange[0],wrange[1]*waverange[1]])
    if np.max(pltwave[0])/np.min(pltwave[0]) > 10:
        ax2.set_xscale('log')
    ax2.set_xticks(pltwave[0])
    ax2.set_xticklabels(np.array(pltwave[0]/(1.+z),dtype=np.int32))
    ax2.set_xlabel(r'Rest Wavelength ($\mathring{\rm A}$)', fontsize=19)
    plt.savefig('/home/lailimin/GalfitS/2steps/puresed/nested_sampling/'+str(galid)+'/sedfitting.png',dpi=100, bbox_inches='tight')

    return fr

def plot_prob(galid):
    with open('/home/lailimin/GalfitS/2steps/puresed/nested_sampling/'+str(galid)+'/results_dict.pickle', 'rb') as file:
        result_dict = pickle.load(file)

    z_sample = np.array(result_dict['samples'])[:, result_dict['varnames'].index('z_mygal')]

    fig = plt.figure(figsize=(8, 6))
    plt.hist(z_sample, bins=100, density=True, histtype='step', color='black', lw=2)
    
    filename = '/home/lailimin/smacs0723_photoz/eazy_photz/merge.smacs0723.miri.v05'
    NUMBERs = pd.read_table(filename, sep='\s+')['#NUMBER'].values
    z_best = pd.read_table(filename, sep='\s+')['zbest'].values
    specz = z_best[np.where(NUMBERs == galid)[0][0]]

    plt.axvline(x=specz, color='red', linestyle='--', label='Spec z = '+str(specz) )
    plt.legend(fontsize=14)
    plt.xlabel('Redshift', fontsize=16)
    plt.ylabel('Probability', fontsize=16)
    plt.xlim(0.01,12)
    #plt.xscale('log')
    plt.xticks(fontsize=14)
    plt.yticks(fontsize=14)
    plt.savefig('/home/lailimin/GalfitS/2steps/puresed/nested_sampling/'+str(galid)+'/puresed_zgrid.png', bbox_inches='tight')
    plt.close()
