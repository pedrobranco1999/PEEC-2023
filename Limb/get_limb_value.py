import numpy as np
import pandas as pd
from scipy.interpolate import interpn

Tabela1=pd.read_csv("values_limbo.csv")
Temperature=np.arange(3500,7000,100)
Logg=np.arange(3.0,5.0,0.1)
FeH=np.arange(-0.5,0.6,0.1)
Variables=(Temperature,Logg,FeH)
Values_limbo=np.array(Tabela1["Limbo"])

VL=np.zeros((len(Temperature),len(Logg),len(FeH)))
zz=0

for i in range(len(Temperature)):
    for j in range(len(Logg)):
        for k in range(len(FeH)):
            VL[i][j,k]=Values_limbo[zz]
            zz+=1

def interpolation_function(T,logg,feh):
    """
    This function calculates the limb darkening coefficient using interpolation
    The ranges of values that the imput parameters use are:
    -T: Range=[3500.0,8750.0]
    -logg: Range=[3,5]
    -feh: Range=[-0.5,0.5]
    """
    return interpn(Variables, VL,np.array([T,logg,feh]))[0]

