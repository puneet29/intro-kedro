# Kedro Practice

This repo contains the kedro projects created for self learning.
The notebook for each of the project will be inside the notebooks folder of each project.

## Note

While running this repo on codespaces make sure to add the following param to the jupyter notebook command:

`--NotebookApp.allow_origin='*'`

## Project iterations

### 1. [intro_kedro](intro_kedro/)

This project consists the data pipelines created using the pandas-iris dataset. It covers the following material:

- How to write data pipelines using Kedro
- Writing datasets to catalog.yml
- Writing custom datasets and transcoding
- Dataset versioning and dataset injection

### 2. [flight_delay_prediction](flight_delay_prediction/)

This project contains the data pipelines created using the data taken from [flight delay prediction](https://www.kaggle.com/divyansh22/flight-delay-prediction) kaggle dataset. It covers the following material:

- Why and how to use PartitionedDataSet?
