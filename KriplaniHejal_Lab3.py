#part1 
import numpy as np


def physconstant(x):
    '''
returns the numerical value of the specified physical constant.
the constants
    c  : speed of light in vacuum 
    h  : planck constant 
    k  : boltzmann constant 
    me : electron mass 
    u  : atomic mass unit 
    e  : elementary charge 
    a0 : bohr radius 
    G  : gravitational constant 
    σ  : stefan boltzmann constant 
    
    '''
    
    # constants in a dictionary
    constants = {
        'c': 2.99792458 * 10**8,      # speed of light 
        'h': 6.62606896 * 10**-34,    # planck constant 
        'k': 1.3806504 * 10**-23,     # boltzmann constant 
        'me': 9.10938215 * 10**-31,   # electron mass 
        'u': 1.660538782 * 10**-27,   # atomic mass unit 
        'e': 1.602176487 * 10**-19,   # elementary charge 
        'a0': 5.2917720859 * 10**-11, # bohr radius 
        'g': 6.67428 * 10**-11,       # gravitational constant 
        'σ': 5.670400 * 10**-8        # stefan boltzmann constant 
    }
    
    # check if the input constant is in the dictionary
    if type(x) in constants != str:
        print("this is not a number")
    else:
        xl = x.lower()
    if xl not in constants.keys():
        print('number must be one of ', list(constants.keys()))
        return
    else:
        return(constants[xl])

#part2
def planck_function(f, t):
    '''
    computes the planck radiation function Bv(T) for given frequencies and temperatures.
    
    the planck function Bν(t) is given by:
    Bν(t) = (2h ν^3/c^2) * (exp(h ν/kT) − 1)^-1
    '''  
    
    hc2 = 2 * physconstant('h') * physconstant('c')**-2 
    hk = physconstant('h') / physconstant('k')
    if type(f) != np.ndarray:
        f = np.array([f]) 
    if type(t) != np.ndarray:
        t = np.array([t])
    bnu = hc2* f[np.newaxis,:]**3 * (np.exp(hk*f[np.newaxis,:]/t[:,np.newaxis])-1)**-1
    return(bnu)
    
#part3

import numpy as np
import matplotlib.pyplot as plt

# define wavelengths in nanometers and convert to meters
wavelengths_nm = np.arange(10.0, 2000, 10.0)  # wavelengths from 10 to 2000 nm
wavelengths_nm = wavelengths_nm * 1e-9         # convert to meters

# convert wavelengths to frequencies
frequencies = physconstant("c")/wavelengths_nm
# define the temperatures
temperatures = np.array[(5e3,1e4,1.5e4)]  
bnu= planck_function(frequencies, temperatures)
fig, ax = plt.subplots()
for i, T in enumerate(temperatures):
    lab = 'T = %d K' % T
    ax.plot(wavelengths_nm, bnu[i], label = lab)
ax.legend()
ax.set_xlabel('Wavelength [m]')
ax.set_ylabel(r'$B_{\nu}$ [J s$^{-1}$ Hz$^{-1}$ m^$^{-2}$ sr$^{-1}$]') 
#ax.set_yscale('log') 
ax.set_xscale('log') 
plt.show()

#part4

freqs = np.arange(1e13,1e16,1e13) 
bnu_10000 = planck_function(freqs,10000) 
print(bnu_10000)

integral = np.trapz(bnu_10000,freqs) 
print(integral)
stefan = physconstant('sigma')* 10000**4/np.pi #Stefan-Boltzmann radiation
frac_diff = (integral-stefan)/stefan 
print("integral result = {}, stefan result = {}, difference = {}".format(integral[0],stefan,frac_diff[0])) #print the results