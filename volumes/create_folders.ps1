# Проверка и создание папок
$directories = @(
    "pgadmin",
    "elasticsearch",
    "kibana",
    "airflow\dags",
    "airflow\logs",
    "airflow\plugins",
    "nifi\database_repository",
    "nifi\flowfile_repository",
    "nifi\content_repository",
    "nifi\provenance_repository",
    "nifi\state",
    "nifi\conf",
    "nifi\drivers"
)

foreach ($dir in $directories) {
    if (-not (Test-Path $dir)) {
        New-Item -ItemType Directory -Path $dir
    }
}

Write-Host "Папки созданы или уже существуют."
