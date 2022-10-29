from geo.Geoserver import Geoserver
geo = Geoserver('http://127.0.0.1:8080/geoserver', username='admin', password='geoserver')
# geo.create_workspace(workspace='demo')
geo.create_coveragestore(layer_name='layer1', path=r'path\to\raster\file.tif', workspace='demo')