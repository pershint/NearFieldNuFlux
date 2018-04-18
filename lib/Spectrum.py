#######Classes used to build the reactor antineutrino spectrum########

MWHTOMEV = 2.247E22

class ReactorSpectrumCalculator(object):
    def __init__(self,isofracs=None, isoparams=None, P_th = 0.0,erange=[1.8,9.0],ebinwidth=0.2):
        self.isofracs = isofracs
        self.isoparams = isoparams
        self.energy = np.arange(erange[0],erange[1], ebinwidth)
        self.P_th = P_th

    def setIsofracs(self,isofracs):
        '''Sets the calculator's isotope fraction dictionary'''
        self.isofracs = isofracs

    def setIsoParams(self,isoparams):
        '''Sets the calculator's isotope parameter dictionary'''
        self.isoparams = isoparams

    def setThermalPower(self,P_th):
        '''Sets the thermal power to use for calculation (in Megawatts)'''
        self.P_th = P_th

    def CalculateSpectrum(self):
       '''Returns the reactor antineutrino flux as a function of energy'''
       BigLambda = self.__CalculateLambda()
       PowPerFission = 0.0
       for isotope in self.isofracs:
           PowPerFission+=self.isofracs[isotope]*self.isoparams[isotope]["EPerFission"]
        #Convert from MeV to Megawatts
        PowPerFission = PowPerFission/MWHTOMEV
        return BigLambda * (P_th/PowPerFission)

    #######Functions internally used########
    def __CalculateLambda(self):
       '''Calculates the big lambda function spectrum, which is a sum
       of the smaller lambdas times the fission fractions'''
       BigLambda = []
       for isotope in self.isofracs:
           #Calculate the small lambda for this isotope
           poly_terms = []
           for i in np.arange(0,len(iso.poly_coeff)):
               term = self.__polyTerm(iso.poly_coeff[i], self.E_array, i)
               poly_terms.append(term)
           exp_term = np.sum(poly_terms,axis=0)
           lamb_k = np.exp(exp_term)
           if BigLambda is None:
               BigLambda = self.isofracs[isotope] * lamb_k
           else:
               BigLambda = BigLambda + (self.isofracs[isotope] * lamb_k)
       return BigLambda

    def __polyTerm(self, a, e, c):
        return a * (e**c)

