# %%

import gpxpy
import gpxpy.gpx
import numpy
import OSMPythonTools
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

from OSMPythonTools.api import Api
from OSMPythonTools.overpass import Overpass


api = Api()
overpass = Overpass()
way = api.query('way/5887599')

# %%
print("hellp")

# %%
