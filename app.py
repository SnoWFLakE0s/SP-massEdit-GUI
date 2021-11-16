import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
import Pmw
import os
from os import *
from tkinter import filedialog
from tkinter.filedialog import Directory
import xml.etree.ElementTree as ET

root = tk.Tk()
root.title("SimpleTools - Mass Edit")
root.resizable(width=False, height=False)
Pmw.initialise(root)

img_infoicon = (Image.open("infoicon.png"))
img_infoicon_resized = img_infoicon.resize((12,12), Image.ANTIALIAS)
img_info_icon = ImageTk.PhotoImage(img_infoicon_resized)

aircraftFileDirectory = []
#For Windows Build
simplePlanesDirectory = str(os.environ['USERPROFILE'] + "\AppData\LocalLow\Jundroo\SimplePlanes\AircraftDesigns")

#File dialog protocol
def addFile():
    #clearDirectory called first to reset selection
    clearDirectory()
    #Open the file selection dialog
    fileDirectory = filedialog.askopenfilename(initialdir=simplePlanesDirectory, title="Select Aircraft File", filetypes=(("Aircraft Files (.xml)","*.xml"), ("All Files", "*.*")))
    #Add the file directory to the file directory array
    aircraftFileDirectory.append(fileDirectory)
    #Print the file directory array to the entry field
    ent_fileDirectory.insert(0, aircraftFileDirectory[0])

def clearDirectory():
    #Empty entry field
    ent_fileDirectory.delete(0, END)
    #Empty file directory array
    aircraftFileDirectory.clear()

frm_main = tk.Frame(master=root, bg="#2f3136", padx=20, pady=20)

frm_selectFile = tk.Frame(master=frm_main, bg="#2f3136")
frm_selectFile.grid(row=0, column=0, sticky="news")
btn_selectFile = tk.Button(master=frm_selectFile, text="Select Aircraft File", padx=10, pady=5, width=20, bg="#375a7f", fg="white", command=addFile)
btn_selectFile.grid(row=0, column=0)
ent_fileDirectory = tk.Entry(master=frm_selectFile, width=82, bg="white")
ent_fileDirectory.insert(0, "  Choose your XML save file or paste the file directory...")
ent_fileDirectory.grid(row=0, column=1, sticky="news", padx=(10,0))

# Set of common choices that should be easy to access
frm_commonChoices = tk.Frame(master=frm_main, bg="#2f3136", borderwidth=2, relief=GROOVE)
frm_commonChoices.grid(row=1, column=0, sticky="nws", pady=20)
lbl_commonChoices = tk.Label(master=frm_commonChoices, text="Basic Options", bg="#2f3136", fg="white").grid(row=0, column=0, sticky="nws", pady=(0,10))
# Tooltip
lbl_commonChoices_info = tk.Label(master=frm_commonChoices, bg="#2f3136", image=img_info_icon)
lbl_commonChoices_info.grid(row=0, column=0, sticky="w", padx=(75,0), pady=(0,8))
tooltip_commonChoices_info = Pmw.Balloon(root)
tooltip_commonChoices_info.bind(lbl_commonChoices_info,"Commonly used, basic options for projects. Click the options to enable any particular one.")

# Option: set massScale = 0
# Make options mutually exclusive
def doMassZero():
    if massScaleZero.get() == 1:
        chkbtn_commonChoices_massScaleOne.deselect()
def doMassOne():
    if massScaleOne.get() == 1:
        chkbtn_commonChoices_massScaleZero.deselect()
massScaleZero = tk.IntVar()
chkbtn_commonChoices_massScaleZero = tk.Checkbutton(master=frm_commonChoices, text="Set mass scale to 0", variable=massScaleZero, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doMassZero)
chkbtn_commonChoices_massScaleZero.grid(row=1, column=0, sticky="nws", padx=(0,10))
# Option: set massScale = 1
massScaleOne = tk.IntVar()
chkbtn_commonChoices_massScaleOne = tk.Checkbutton(master=frm_commonChoices, text="Set mass scale to 1", variable=massScaleOne, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doMassOne)
chkbtn_commonChoices_massScaleOne.grid(row=2, column=0, sticky="nws", padx=(0,10))

# Option: turn drag off
# Make options mutually exclusive
def doNoDrag():
    if dragCalcOff.get() == 1:
        chkbtn_commonChoices_dragCalcOn.deselect()
def doYesDrag():
    if dragCalcOn.get() == 1:
        chkbtn_commonChoices_dragCalcOff.deselect()
dragCalcOff = tk.IntVar()
chkbtn_commonChoices_dragCalcOff = tk.Checkbutton(master=frm_commonChoices, text="Disable drag calculation", variable=dragCalcOff, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doNoDrag)
chkbtn_commonChoices_dragCalcOff.grid(row=1, column=1, sticky="nws", padx=(0,10))
# Option: turn drag on
dragCalcOn = tk.IntVar()
chkbtn_commonChoices_dragCalcOn = tk.Checkbutton(master=frm_commonChoices, text="Enable drag calculation", variable=dragCalcOn, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doYesDrag)
chkbtn_commonChoices_dragCalcOn.grid(row=2, column=1, sticky="nws", padx=(0,10))

# Make options mutually exclusive
def doDragZero():
    if dragScaleZero.get() == 1:
        chkbtn_commonChoices_dragScaleOne.deselect()
def doDragOne():
    if dragScaleOne.get() == 1:
        chkbtn_commonChoices_dragScaleZero.deselect()
# Option: set drag scale 0
dragScaleZero = tk.IntVar()
chkbtn_commonChoices_dragScaleZero = tk.Checkbutton(master=frm_commonChoices, text="Set drag scale to 0", variable=dragScaleZero, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doDragZero)
chkbtn_commonChoices_dragScaleZero.grid(row=1, column=2, sticky="nws", padx=(0,10))
# Option: set drag scale 1
dragScaleOne = tk.IntVar()
chkbtn_commonChoices_dragScaleOne = tk.Checkbutton(master=frm_commonChoices, text="Set drag scale to 1", variable=dragScaleOne, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doDragOne)
chkbtn_commonChoices_dragScaleOne.grid(row=2, column=2, sticky="nws", padx=(0,10))

# Option: turn collisions off
# Make options mutually exclusive
def doDisableCollisions():
    if disableCollisions.get() == 1:
        chkbtn_commonChoices_enableCollisions.deselect()
def doEnableCollisions():
    if enableCollisions.get() == 1:
        chkbtn_commonChoices_disableCollisions.deselect()
disableCollisions = tk.IntVar()
chkbtn_commonChoices_disableCollisions = tk.Checkbutton(master=frm_commonChoices, text="Disable part collisions", variable=disableCollisions, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doDisableCollisions)
chkbtn_commonChoices_disableCollisions.grid(row=1, column=3, sticky="nws", padx=(0,10))
# Option: turn collisions on
enableCollisions = tk.IntVar()
chkbtn_commonChoices_enableCollisions = tk.Checkbutton(master=frm_commonChoices, text="Enable part collisions", variable=enableCollisions, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doEnableCollisions)
chkbtn_commonChoices_enableCollisions.grid(row=2, column=3, sticky="nws", padx=(0,10))

# Option: add 5 more colors
addColors = tk.IntVar()
chkbtn_commonChoices_addColors = tk.Checkbutton(master=frm_commonChoices, text="Add 5 more color slots", variable=addColors, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white")
chkbtn_commonChoices_addColors.grid(row=3, column=0, sticky="nws", padx=(0,10), pady=(10,0))

# Option: collision response
collisionResponse = tk.IntVar()
chkbtn_commonChoices_collisionResponse = tk.Checkbutton(master=frm_commonChoices, text="Set collision behavior to None", variable=collisionResponse, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white")
chkbtn_commonChoices_collisionResponse.grid(row=3, column=1, sticky="nws", padx=(0,10), pady=(10,0))

# Option: lots of health
largeHealth = tk.IntVar()
chkbtn_commonChoices_largeHealth = tk.Checkbutton(master=frm_commonChoices, text="Set part HP to 1E8", variable=largeHealth, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white")
chkbtn_commonChoices_largeHealth.grid(row=3, column=2, sticky="nws", padx=(0,10), pady=(10,0))

# Option: inertia tensors
inertiaTensors = tk.IntVar()
chkbtn_commonChoices_intertiaTensors = tk.Checkbutton(master=frm_commonChoices, text="Enable diffuseInertiaTensors", variable=inertiaTensors, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white")
chkbtn_commonChoices_intertiaTensors.grid(row=3, column=3, sticky="nws", padx=(0,10), pady=(10,0))

frm_advancedOptions = tk.Frame(master=frm_main, bg="#2f3136", borderwidth=2, relief=GROOVE)
frm_advancedOptions.grid(row=2, column=0, sticky="news")
lbl_advancedOptions = tk.Label(master=frm_advancedOptions, text="Advanced Options", bg="#2f3136", fg="white").grid(row=0, column=0, sticky="nws", pady=(0,10))
# Tooltip
lbl_advancedOptions_info = tk.Label(master=frm_advancedOptions, bg="#2f3136", image=img_info_icon)
lbl_advancedOptions_info.grid(row=0, column=0, sticky="w", padx=(102,0), pady=(0,8))
tooltip_advancedOptions_info = Pmw.Balloon(root)
tooltip_advancedOptions_info.bind(lbl_advancedOptions_info,"Mass edit any attribute using the fields below. Click whitelist/blacklist to enable the option.")

# Attr setting
lbl_advancedOptions_attribute = tk.Label(master=frm_advancedOptions, text="Property", anchor="w", bg="#2f3136", fg="white")
lbl_advancedOptions_attribute.grid(row=1, column=0, sticky="nws", padx=(5,0))
# Tooltip
lbl_advancedOptions_attribute_info = tk.Label(master=lbl_advancedOptions_attribute, bg="#2f3136", image=img_info_icon)
lbl_advancedOptions_attribute_info.grid(row=0, column=0, sticky="w", padx=(47,0), pady=(2,0))
tooltip_advancedOptions_attribute_info = Pmw.Balloon(root)
tooltip_advancedOptions_attribute_info.bind(lbl_advancedOptions_attribute_info,"Enter a property to mass edit.")
# Entry for attr
ent_advancedOptions_attribute = tk.Entry(master=frm_advancedOptions, bg="white", width=25)
ent_advancedOptions_attribute.grid(row=2, column=0, sticky="nws", padx=(7,0), pady=(5,5))

# Everything is screwed here. I don't know what happened, but 
# the positioning and layout of elements here is just terrible
# this should be redone at some point in the future. 
# The master-slaving here is really bad. For now it's this way
# to prevent the weird placement-shifting issue with the value
# setting bit. It does "look" ok, but the backend is just hell.

# Value setting
lbl_advancedOptions_value = tk.Label(master=lbl_advancedOptions_attribute, text="Value", anchor="w", bg="#2f3136", fg="white")
lbl_advancedOptions_value.grid(row=0, column=0, sticky="nws", padx=(170,0))
lbl_advancedOptions_value_info = tk.Label(master=lbl_advancedOptions_value, bg="#2f3136", image=img_info_icon)
lbl_advancedOptions_value_info.grid(row=0, column=0, sticky="w", padx=(32,0), pady=(1,0))
tooltip_advancedOptions_value_info = Pmw.Balloon(root)
tooltip_advancedOptions_value_info.bind(lbl_advancedOptions_value_info,"Enter the value of the specified property.")
# Entry for value
ent_advancedOptions_value = tk.Entry(master=frm_advancedOptions, bg="white", width=25)
ent_advancedOptions_value.grid(row=2, column=0, sticky="nws", padx=(180,150), pady=(5,5))

# Option: whitelist/blacklist
# Make options mutually exclusive
def doWhiteList():
    checkHiding()
    if whiteList.get() == 1:
        chkbtn_advancedOptions_blackList.deselect()

def doBlackList():
    checkHiding()
    if blackList.get() == 1:
        chkbtn_advancedOptions_whiteList.deselect()

# This function is to check if any of the list options
# are selected, and if so turn the related widgets on,
# otherwise if both are deselected turn them off. It
# runs once in the beginning, and any other time that
# the checkboxes are used, so ensure that nothing goes
# wrong with the toggle status.
def checkHiding():
    if (whiteList.get() == 1 or blackList.get() == 1):
        lbl_advancedOptions_exceptions.grid()
        ent_advancedOptions_exceptions.grid()
        chkbtn_advancedOptions_usePartId.grid()
        chkbtn_advancedOptions_usePartType.grid()
    if (whiteList.get() == 0 and blackList.get() == 0):
        lbl_advancedOptions_exceptions.grid_remove()
        ent_advancedOptions_exceptions.grid_remove()
        chkbtn_advancedOptions_usePartId.grid_remove()
        chkbtn_advancedOptions_usePartType.grid_remove()

whiteList = tk.IntVar()
chkbtn_advancedOptions_whiteList = tk.Checkbutton(master=frm_advancedOptions, text="Whitelist", variable=whiteList, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doWhiteList)
chkbtn_advancedOptions_whiteList.grid(row=2, column=2, sticky="nes", padx=10)
blackList = tk.IntVar()
chkbtn_advancedOptions_blackList = tk.Checkbutton(master=frm_advancedOptions, text="Blacklist", variable=blackList, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doBlackList)
chkbtn_advancedOptions_blackList.grid(row=2, column=3, sticky="nes", padx=10)

lbl_advancedOptions_exceptions = tk.Label(master=frm_advancedOptions, text="Whitelist/Blacklist Parts", anchor="w", width=20, bg="#2f3136", fg="white")
lbl_advancedOptions_exceptions.grid(row=3, column=0, sticky="w", padx=(5,0), pady=(10,5))
lbl_advancedOptions_exceptions_info = tk.Label(master=lbl_advancedOptions_exceptions, bg="#2f3136", image=img_info_icon)
lbl_advancedOptions_exceptions_info.grid(row=0, column=0, sticky="w", padx=(125,0), pady=(1,0))
tooltip_advancedOptions_exceptions_info = Pmw.Balloon(root)
tooltip_advancedOptions_exceptions_info.bind(lbl_advancedOptions_exceptions_info,"Whitelisting will only allow the specifed objects to be edited.\nBlacklisting will prevent specified objects from being edited.\nSelect \"Use Part ID\" to white/blacklist a specific group of parts using their partIds.\nSelect \"Use Part Type\" to white/blacklist a specific group of parts using their part type.")

def doUsePartId():
    if usePartId.get() == 1:
        chkbtn_advancedOptions_usePartType.deselect()
def doUsePartType():
    if usePartType.get() == 1:
        chkbtn_advancedOptions_usePartId.deselect()
usePartId = tk.IntVar()
usePartType = tk.IntVar()
chkbtn_advancedOptions_usePartId = tk.Checkbutton(master=lbl_advancedOptions_exceptions, text="Use Part ID", variable=usePartId, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doUsePartId)
chkbtn_advancedOptions_usePartId.grid(row=0, column=0, sticky="nws", padx=(140,5))
chkbtn_advancedOptions_usePartType = tk.Checkbutton(master=lbl_advancedOptions_exceptions, text="Use Part Type", variable=usePartType, bg="#2f3136", activebackground="#2f3136", selectcolor="#141414", fg="white", command=doUsePartType)
chkbtn_advancedOptions_usePartType.grid(row=0, column=1, sticky="nws")
ent_advancedOptions_exceptions = tk.Entry(master=frm_advancedOptions, bg="white", width=54)
ent_advancedOptions_exceptions.grid(row=4, column=0, sticky="nws", padx=(7,0), pady=(0,7))
# Call checkHiding once to initialize the screen properly
checkHiding()

frm_execute = tk.Frame(master=frm_main, bg="#2f3136")
frm_execute.grid(row=3, column=0, sticky="news", pady=20)
btn_execute = tk.Button(master=frm_execute, text="Apply all selected changes", padx=10, pady=5, bg="#375a7f", fg="white")
btn_execute.pack(fill='x')

frm_footer = tk.Frame(master=frm_main, bg="#2f3136")
frm_footer.grid(row=4, column=0, sticky="news")
lbl_footer = tk.Label(master=frm_footer, text="Published under MIT License\nOriginal massEdit.py script built by Nicky \"WNP78\" Pike\nCopyright (c) 2021 Joshua \"SnoWFLakE0s\" Eah\nVersion 0.1 Alpha", bg="#2f3136", fg="white")
lbl_footer.pack()

frm_main.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

root.mainloop()