import os
import subprocess

print("Chequeando si la imagen está")
image_exists=subprocess.run("sudo docker image inspect workstation:latest",shell=True,capture_output=True).returncode

if image_exists == 0:
    print("La imagen workstation exists")

else:
    print("La imagen no existe")
    print("Descargando y construyendo la imagen, puede tomar un tiempo...")
    cwd = os.getcwd()
    os.chdir(os.path.expanduser(cwd+'/docker/'))
    subprocess.run("sudo docker build -t workstation .", shell=True)
    print("¡Lista la imagen! - Construyendo el proyecto")
    os.chdir(cwd)
