@echo off

rem Checking and creating folders
if not exist "pgadmin" mkdir "pgadmin"
if not exist "elasticsearch" mkdir "elasticsearch"
if not exist "kibana" mkdir "kibana"
if not exist "airflow\dags" mkdir "airflow\dags"
if not exist "airflow\logs" mkdir "airflow\logs"
if not exist "airflow\plugins" mkdir "airflow\plugins"
if not exist "airflow\files" mkdir "airflow\files"
if not exist "nifi\database_repository" mkdir "nifi\database_repository"
if not exist "nifi\flowfile_repository" mkdir "nifi\flowfile_repository"
if not exist "nifi\content_repository" mkdir "nifi\content_repository"
if not exist "nifi\provenance_repository" mkdir "nifi\provenance_repository"
if not exist "nifi\state" mkdir "nifi\state"
if not exist "nifi\conf" mkdir "nifi\conf"
if not exist "nifi\drivers" mkdir "nifi\drivers"
if not exist "nifi\files" mkdir "nifi\files"

echo Folders have been created or already exist.
