import sys,os

def tryFindSpDir():
    if sys.platform.startswith("win"):
        p = os.path.abspath(os.path.join(os.getenv("APPDATA"),"..\\LocalLow\Jundroo\SimplePlanes\AircraftDesigns")) + "\\"
        if os.path.isdir(p): return p
    elif sys.platform.startswith("darwin"): # MacOS - not tested
        p = os.path.abspath("~/Library/Application Support/Jundroo/SimplePlanes/AircraftDesigns") + "/"
        if os.path.isdir(p): return p
    return input("SP aircraft directory> ") # failed to auto detect

from xml.etree.ElementTree import ElementTree as et
path = os.path.join(tryFindSpDir(), input("Name> ") + ".xml")
tree = et(file=path)
root = tree.getroot()
prop = input("Property> ")
val = input("Value> ")
for part in root.findall("Assembly/Parts/Part"):
    part.set(prop, val)
tree.write(path)