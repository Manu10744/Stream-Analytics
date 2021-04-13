## Reading Input: 
Flink offers three APIs: 
- DataStream API
- Table API
- DataSet API (has been soft deprecated; using the DatasStream API is recommended...also not available in PyFlink)

**DataStream API:**  
- One possibility to load data into a stream via the DS API is to use connectors. Unfortunately with our input (JSON-Format) that is not an option, as there 
no DS connector that supports JSON files.
- Alternatively, one could implement a custom data source. However, this seems like an unreasonable amount of effort.

**Table API:**
- Contrary to the DS API, the Table API offers the FileSystem-Connector which allows to load data from a file. Moreover, it supports JSON
  formatted data. Currently, this seems like the best option. Note that our JSON file will need to be converted to a newline-delimited JSON format (https://jsonlines.org/). 
  This can be done in Python. Issues may arise with the (required?) partitioning of files. Also, in this case the connector-jar must be provided as a project dependency. 
- Alternatively, the Table API offers the possibility to load data from a pandas dataframe/a collection. As JSON files can be loaded into pd dfs in Python, this could also
  be a viable option. A collection could certainly also be created from the JSON.
  


