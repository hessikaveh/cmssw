import FWCore.ParameterSet.Config as cms

# import CMS geometry
from Configuration.Geometry.GeometryExtended2023D1Reco_cff import XMLIdealGeometryESSource

# add our custom detector grouping to DDD
XMLIdealGeometryESSource.geomXMLFiles.extend(['SimTracker/TrackerMaterialAnalysis/data/trackingMaterialGroups_ForPhaseII.xml'])
