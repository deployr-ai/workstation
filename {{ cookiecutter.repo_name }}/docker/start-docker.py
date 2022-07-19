import os
import subprocess
import time

print("Chequeando si hay un container workstation levantado")
cont_exists=subprocess.run("sudo docker inspect workstation-cont",shell=True,capture_output=True).returncode

if cont_exists == 0:
    subprocess.run("sudo docker start workstation-cont", shell=True)
    print('¡Todo en orden! Entrá a localhost:8080 en tu explorador')
else:
    subprocess.run('sudo docker run -d -p 8080:8080 -v "%s":/workspace --name workstation-cont workstation'%os.getcwd(), shell=True)
    print('Esperando a que la imagen esté lista...')
    time.sleep(10)
    try:
        subprocess.run("sudo docker exec workstation-cont bash -c 'mkdir /workspace/references/tutorials'",shell=True) 
    except Exception as err:
        print('There was an error creating tutorials folder')
        print(str(err))
    try:
        subprocess.run("sudo docker exec workstation-cont bash -c 'rm -r /workspace/zeppelin'",shell=True) 
    except Exception as err:
        print('There was an error erasing zeppelin folder')
        print(str(err))
    try:
        subprocess.run("sudo docker exec workstation-cont bash -c 'cp -r /resources/tutorials/tutorials/* /workspace/references/tutorials'",shell=True) 
    except Exception as err:
        print('There was an error copying tutorials')
        print(str(err))
    print('¡Todo en orden! Entrá a localhost:8080 en tu explorador')
