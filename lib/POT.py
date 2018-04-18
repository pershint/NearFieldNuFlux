import DBUtils as du

class DetectorVolume(object):
    def __init__(self,material=None,volume=None):
        self.material = material
        self.volume = volume

    def setMaterial(self,material):
        '''Define which material to look up from the MaterialDB'''
        self.material = material

    def setVolume(self,volume):
        '''Define your active detector volume in cubic meters'''
        self.volume = volume

    def CalculatePOT(self):
        '''Calculates the total proton targets in detector volume
        (assumes hydrogen in material composition is all free protons)'''
        material_specs = du.GetMaterialInfo(self.material)
        POT = material_specs["density"] * volume * \
                material_specs["element_fracs"]["Hydrogen"]
        return POT
