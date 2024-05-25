import pkg_resources
import subprocess

# Lista de todas as bibliotecas instaladas
packages = [dist.project_name for dist in pkg_resources.working_set]

# Atualiza cada biblioteca individualmente
for package in packages:
    subprocess.call(f"pip install --upgrade {package}", shell=True)
