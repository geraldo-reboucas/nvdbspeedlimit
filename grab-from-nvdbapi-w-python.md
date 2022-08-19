# Python code - grab data from the NVDB api 

The python script `speedlimit2shp.py` will download speed limit data from NVDB api and produce a shapefile with speed limit data, as well as road numbers and some other details. The shape file contains these attributes: 


| Attribute | Type | Description |
|-----------|------|-------------|
| SpeedLim  | Integer | The speed limit in kilometers per hour | 
| RoadCat   | Text | A single character describing the road category: E,R,F,K,P or S | 
| RoadNum   | Text | The combination of road category and road number, for example E6 or F450 |
| linkID    | Integer | The Id of the NVDB road link sequence that this object belongs to | 
| linkFrom  | Float | Linear reference, the starting position of this feature along this NVDB road link seqence | 
| linkTo    | Float | Linear reference, the end position of this feature along this NVDB road link sequence | 
| nvdbId    | Integer | The ID of the NVDB feature. Please note that many features are divided into smaller segment, so NVDB ID won't be unique within this data set. | 
| versjon   | Integer | The version number of this version of this NVDB feature | 

Please see our notes about [quirks and caveats](./grabbing-from-NVDBapi.md) for mapping between center line topology and individual lanes.

# Installation 

The script `speedlimit2shp.py` requires the two other python files `apiforbindelse.py` and  `nvdbapiv3.py` in this repository to be present at the python search path (just put them all in the same folder). These two files are maintained in this repos [nvdbapi-v3](https://github.com/LtGlahn/nvdbapi-V3)

The script also requires that the the python library [geopandas](https://geopandas.org/en/stable/) is installed on the system. A quick and easy way is to use the trusty old  `pip install` in your shell:   

```
pip install geopandas 
```

***This installation method is perfect for throwaway environments, such as google cloud platform***, or if you otherwise don't really use python that frequent. 

However, if you're a heavy python user and your python installation has a long life, sucn as your own personal or work computer, we recommend that you go the somewhat more complex route of creating so called `environments` because long term use of `pip install` will at some point create version conflicts. This occurs when the package you want to install today needs a different version of some external 3rd party library than the one you have installed on your system. 

> Example: Geopandas wants to install the package xyzservices version 2022.6.0. Some random library you installed two years ago will not work with version 2022.6.0, but needs the older version that already exists on your system. Solving version conflicts is not for the faint at hearth, which is why creating separate environments is highly recommended. Not only does it prevents version conflicts, it also improves the chance  that your code will be reusable in the future. 

Python has different methods for virtual environments, but the most popular within the data science community is to use the [conda package manager](https://docs.conda.io/en/latest/). And the most popular option for installing conda is to install the [anaconda python distribution](https://www.anaconda.com/products/distribution). 


```bash
conda create -n nvdbspeedlimit -c conda-forge geopandas
conda activate nvdbspeedlimit
```


