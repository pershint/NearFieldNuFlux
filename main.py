##########NEAR-FIELD FLUX CALCULATOR############
## Written by: Teal Pershing (UC Davis) ########
######## Last updated: April 17, 2018 ##########
import lib.argparser as ap

basepath = os.path.dirname(__file__)
mainpath = os.path.abspath(basepath)
configpath = os.path.abspath(os.path.join(basepath,"config"))
dbpath = os.path.abspath(os.path.join(basepath,"db"))

args = ap.args

#args defining what files are used to run what kind of MVA
BUILD = args.BUILD

if __name__ == '__main__':
    #So, we have to do a couple things:
    #1.  Read in the Geometry.json to get the reactor type and detector material type
    #TODO: For now, just hardcode the distance between core and box
    #2.  Initialize a SpectrumCalculator class, and calculate the spectrum
    #3.  Initialize the class in POT.py and calculate the number of proton targets in water
    #4.  Calculate the expression in the box, and plot dat dN/dE
    #5.  Clean up the NuToPos script for converting the dNdEnu to dNdEpositron
    #6.  Get that smearer going again; we could apply the resolution seen
    #    in nucifer, and improve the resolution to see what kind of detector
    #    resolution you would need to see differences in the spectrum due to 
    #    Different fuel loadings! Eh?  Eh?  How fast to tell a PWR froma PHWR?
