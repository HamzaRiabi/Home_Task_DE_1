Home_Task_1

==============================

ETL - API - TEST

==============================

Project Organization

------------
```bash
├── README.md                 <- The top-level README for developers using this project.
├── data
│   ├── external              <- Data from third-party sources.
│   ├── intermediate          <- Intermediate data that has been transformed.
│   ├── processed             <- The final, canonical data sets for modeling.
│   ├── databases             <- All the databases used by the project.
│   └── raw                   <- The original, immutable data dump.
│
├── docs                      <- Documentation files. 
│   └── system diagram.jpg    <- System diagram for the deployed solution.
│
├── src   
│   │                    
│   ├── api                   <- Scripts and modules for the REST API.
│   │   ├── __init__.py       <- Makes 'api' a Python module.
│   │   └── client.py         <- Flask application for REST API.
│   │
│   ├── etl                   <- Scripts and modules for the ETL process.
│   │   ├── __init__.py       <- Makes 'etl' a Python module.
│   │   ├── extract.py        <- Module for data extraction.
│   │   ├── transform.py      <- Module for data transformation.
│   │   ├── load.py           <- Module for data loading.
│   │   └── pipeline.py       <- The ETL pipeline itself, containing the sequence of nodes.
│   │
│   │── tests                 <- Unit tests for the project.
│   │   ├── __init__.py       <- Makes 'tests' a Python module.
│   │   └── test_etl.py       <- Unit tests for the ETL process & the API.
│   │
│   ├── __init__.py           <- Makes 'src' a Python module.
│   └── config.py             <- Configuration file for the project.
│
├── logs                      <- Log files for the project.
│   ├── api_logs.log          <- Log file for API operations.
│   └── etl_logs.log          <- Log file for ETL process.
│
└── requirements.txt          <- File listing required Python packages for the project.

==============================

Task 3: the system diagram is under the docs directory.