#Tools for loading any jsons from the DB directory

import os
import json


basepath = os.path.dirname(__file__)
dbpath = os.path.abspath(os.path.join(basepath,"..","db"))

def GetMaterialInfo(material):
    if material is None:
        print("Please input a material, come on...")
    with open("%s/MaterialDB.json"%dbpath,"r") as f:
        material_dat = json.load(f)
    try:
        return material_dat(material)
    except KeyError:
        print("Your material was not found in the materials dictionary.")
        return None
