######Functions for getting the Cross section as a function of########
######Energy for the electron antineutrino IBD                ########
#-----CROSS-SECTION CONSTANTS------#

DELTA = 1.293   #in MeV; neutron mass - proton mass
Me = 0.511 #in MeV
A1 = -0.07056
A2 = 0.02018
A3 = -0.001953

def XC(self, E):
    Ee = (E - DELTA)
    pe = np.sqrt((Ee**2) - (Me**2))
    poly = E**(A1 + (A2 * np.log(E)) + (A3 * ((np.log(E))**3)))
    return (1E-53) * pe * Ee * poly #1E-53, instead of -43, for km^2 units

#takes in an array of energies and returns the scattering angle-averaged
#cross-section for neutrino IBD interactions.
def XC_Vogel_0ord(self, E):
    Ee0 = (E - DELTA)
    pe0 = np.sqrt((Ee0**2 - Me**2))
#        f,g=1,1.26  #vector axial coupling constants
#        gFERM = 1.16639E-11  #in MeV ^ -2
#        cosTC = 0.974
#        RCinner = 0.024  #inner radiative correction
#        sig0 = (gFERM**2) * (cosTC**2) * (1 + RCinner) / np.pi
#        sigtot_0th = sig0 * (f**2 + 3*(g**2)) * pe0 * Ee0 * 1E-10 #cm^2->km^2
    sigtot_0th = 0.0952 * pe0 * Ee0 * 1E-52
    return sigtot_0th

