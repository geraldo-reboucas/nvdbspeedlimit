# How can you get Norwegian speed limit data?

How can you get Norwegian speed limit data from the Norwegian Road database (Nasjonal vegdatabank, shorthand NVDB)? This database is maintianed by a joint effort of the Norwegian Public Road administratin [NPRA](https://www.vegvesen.no/en/?lang=en)
and the [Norwegian Mapping Authority](https://kartverket.no/en)

Various distribution channels and products exists for NVDB data. Like any other data in NVDB, speed limits can be downloaded directly from the NVDB api. But the NPRA and the Norwegian Mapping authorities have a long history of delivering vendor-independent road network products (for, among other things,  routing applications). Speed limit data are of course included. 

The data are available through the [Norwegian Licence for Open Government Data](https://data.norge.no/nlod/en/). Please choose among the following options:

## Grabbing data directly from the NVDB api 

The [NVDB api](https://nvdbapiles-v3.atlas.vegvesen.no/dokumentasjon/) is a REST api where you can grab any data from NVDB, including speed limits, road networks and a bunch of other things. Unfortunately, the documentation is in Norwegian. We've written some English summaries [here](https://www.vegdata.no/2014/02/19/a-little-note-to-oor-our-international-fans/) and [here](https://nvdbtransportportal.vegdata.no/), we hope you'll find them helpful. 

[More details, caveats and quirks on the NVDB api](./grabbing-from-NVDBapi.md)

[Our python code exampe](./grab-from-nvdbapi-w-python.md)

## Downloading NPRA routing application data 

The NPRA runs its own routing application. Although the data structure is tailored to the specific quirks of that application, the network data we feed into it are in an open, not-too-obfuscated data structure. Speed limits are stored as attributes `speedfw` (speed forward) and `speedbw` (speed backwards) on the links themselves, in the table `ruttger_link_geom`. _Forward_ and _backward_ refer to the direction of travel along the link, so you can have different speed limits for different directions on the same link. 

The newest NPRA routing application data can be downloaded from the FTP server ftp://vegvesen.hostedftp.com/~StatensVegvesen/vegnett/ , or alternatively from the [geonorge portal](./dowloading-from-geonorge-portal.md)

The spatiaLite (sqlite) format is recommended, this is the one we use ourselves. The file geodatabase format is provided "as is", as a courtesy for Esri users.  

## Downloading Elveg road network data set (will be replaced by Elveg 2.0)

This data product has in fact a longer history than our road data base. The format is the norwegian text based format [SOSI dot notation](https://en.wikipedia.org/wiki/SOSI), which has a long history for data exchange within the Norwegian GIS community. See [downloading from geonorge portal](./dowloading-from-geonorge-portal.md) for instructions on how to get this data set. 

## Dowload Elveg 2.0 in GML format (experimental)

Moving away from the old trusty sosi dot text format, the NPRA and the Norwegian Mapping Authority are developing a new vendor independent network data set called Elveg 2.0. There are several improvement to the logic and structure of the data, finally available in the [OGC](https://www.ogc.org/)-compliant format [GML - Geograpy Markup Language](https://en.wikipedia.org/wiki/Geography_Markup_Language). 

See [downloading from geonorge portal](./dowloading-from-geonorge-portal.md) for instructions on how to get this data set. 

# Why can't you just give us a shapefile? How hard can it be? 

Not hard at all. But then the burden on keeping your system updated will be on NPRA. 

We at NPRA will happily provide extensive guidance on how you can make that happen - with special emphasis on the "you make it happen" - part. The NPRA and the Norwegian Mapping Authorities strives to continuosly improve NVDB-related services (NVDB api) and data products for free under the [NLOD license](https://data.norge.no/nlod/en/).   

We will do our outmost to ensure that the process of grabbing Norwegian speed limit data can be automated in a robust pipeline. We are happy to discuss any suggestion on how to improve our services and data products. 

# Do you have the right road numbers? 

Road numbers are automatically included in all data products and pipelines described here. 