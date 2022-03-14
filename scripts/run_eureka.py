import sys, os, time
from importlib import reload
import eureka.S3_data_reduction.s3_reduce as s3
import eureka.S4_generate_lightcurves.s4_genLC as s4

eventlabel = 'wasp39b'

# reload(s3)
# ev3 = s3.reduceJWST(eventlabel)

reload(s4)
# ev4 = s4.lcJWST(ev3.eventlabel,ev3.workdir, md=ev3)
workdir = "/Users/catrionamurray/Documents/Postdoc/CUBoulder/JWST_hackathon/Spectra_to_Transit/NIRCam/Stage_3_Output_Eureka/"
ev4 = s4.lcJWST(eventlabel)
