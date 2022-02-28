import gpxpy
import gpxpy.gpx
import numpy
import OSMPythonTools

from OSMPythonTools.api import Api

api = Api()
way = api.query('way/5887599')

