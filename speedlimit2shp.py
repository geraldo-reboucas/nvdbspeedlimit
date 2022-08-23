import nvdbapiv3 
import geopandas as gpd
import pandas as pd 
from shapely import wkt 
from datetime import date, datetime 

if __name__ == '__main__': 

    # How much time do we use? 
    t0 = datetime.now()

    # Searching for 
    mySearchObject = nvdbapiv3.nvdbFagdata( 105 )

    # Do you prefer lat/lon coordinates, with the axis order lat - lon (y,x)? 
    # Specify spatial reference system (srid) epsg:4326 when fetching data from NVDB API 
    # mySearchObject.filter( {'srid' : 4326})

    # Bounding box for test area 
    # mySearchObject.filter( {'kartutsnitt' : '11.04189329,58.96015542,11.56670696,59.30649984' } )
    # mySearchObject.filter( {'kartutsnitt' : '283134.63352143,6554956.00500561,293507.29709016,6561801.31869616' } ) 

    #################### 
    ## Only fetching fresh data updates (in Norwegian time zone)
    # mySearchObject.filter( { 'endret_etter' : '2022-08-22T06:12:31' })
    ## PLEASE NOTE that this option will produce some false positives: Sometimes, speed 
    ## limit  data will be  flagged as "changed" because there are edits to the  
    ## underlying  road network or the the objects relating to the road reference system
    ## (or changes to any of the other objects used in our indexing procedure). 


    # Converting to Pandas DataFrame 
    myDataFrame = pd.DataFrame( mySearchObject.to_records( ))

    # Converting to Geopandas Geodataframe 
    myDataFrame['geometry'] = myDataFrame['geometri'].apply( wkt.loads )
    myGDF = gpd.GeoDataFrame( myDataFrame, geometry='geometry', crs=5973 )

    # Reprojecting into lon/lat coordinates (x,y). Note the axis order. 
    myGDF = myGDF.to_crs( 'epsg:4326' )

    # Attribute naming, translating long Norwegian names into short (10char) English abbreviations
    # This 10 char limit is one of the curses of the shape file
    myGDF['SpeedLim'] = myGDF['Fartsgrense'] 
    myGDF['RoadCat'] = myGDF['vegkategori'] 
    myGDF['RoadNum'] = myGDF['vegkategori'] + myGDF['vegnummer'].astype(str) 

    # These are linear references to the link sequences of NVDB, so that we can trace problems back to the NVDB network 
    myGDF['linkID']  = myGDF['veglenkesekvensid']
    myGDF['linkFrom'] = myGDF['startposisjon']
    myGDF['linkTo']   = myGDF['sluttposisjon'] 

    # We also include the ID and version number of the speed limit object in NVDB data base
    columns =  ['SpeedLim', 'RoadCat', 'RoadNum', 'linkID', 'linkFrom', 'linkTo', 'nvdbId', 'versjon', 'geometry']   

    # Writing data to esri shapefile
    myGDF[columns].to_file( 'nvdbspeedlimit.shp')

    # print( list( myGDF.columns ) )

    t1 = datetime.now()
    print( t1-t0 )