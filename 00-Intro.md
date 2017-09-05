# 0. Web Processing Service (aka WPS)

## 0.1. What is WPS

Web Processing Service (WPS) is part of the OWS standards defined by OGC, while WFS,WMS,WCS,SOS
are used for transfer of data (upload, download, transformation?), WPS is used for data processing in the server (All processing is done in server side).

WPS provides a standard interface for input, output, process discovery and execution. WPS is normally used for geospatial data to run spatial processes.

One good example of WPS usage is provided by geoserver ([WPS-Geoserver](http://docs.geoserver.org/latest/en/user/services/wps/operations.html)), where multiple geospatial processes are avaiable to be applied to the data container in server
