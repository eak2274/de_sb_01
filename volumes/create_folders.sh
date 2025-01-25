#!/bin/bash

# Проверка и создание папок
mkdir -p pgadmin
mkdir -p elasticsearch
mkdir -p kibana
mkdir -p airflow/dags
mkdir -p airflow/logs
mkdir -p airflow/plugins
mkdir -p airflow/files
mkdir -p nifi/database_repository
mkdir -p nifi/flowfile_repository
mkdir -p nifi/content_repository
mkdir -p nifi/provenance_repository
mkdir -p nifi/state
mkdir -p nifi/conf
mkdir -p nifi/drivers
mkdir -p nifi/files

echo "Папки созданы или уже существуют."