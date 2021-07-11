from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware

import shutil
import paramiko

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/image")
async def image(image: UploadFile = File(...)):
    # file_location = "src/Inputs/JPEG_Input"
    file_location = f"/src/Inputs/Nifti_images/{image.filename}"

    with open(file_location, "wb") as buffer:
        shutil.copyfileobj(image.file, buffer)
    
    return {"filename": image.filename}

@app.post("/execute")
async def execute():
    print('start')

    # ssh import and params
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print('loaded')

    # ssh connection
    ssh.connect('192.168.1.104',  port=7000, username='test', password='test', banner_timeout=200)
    # ssh.connect('172.17.0.2', port=8888, username='root', password='0000', banner_timeout=200)
    print('connected')

    # # Run a command and catch the result
    # stdin, stdout, stderr = ssh.exec_command('cd notebooks/ \n python3 app.py')
    stdin, stdout, stderr = ssh.exec_command('cd /src/notebooks \n ls \n ipython pfe.py')
    print('executed')

    print(f'STDOUT: {stdout.read().decode("utf8")}')
    print(f'STDERR: {stderr.read().decode("utf8")}')

    return_ssh_code = stdout.channel.recv_exit_status()
    print(f'Return code: {return_ssh_code}')
    if return_ssh_code != 0:
        print('ssh connenction failed')
    else:
        print('ssh connenction stablished')

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    # Close the client itself
    ssh.close()

    return "executed"



@app.post("/download")
async def download():
    print('start')

    # ssh import and params
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print('loaded')

    # ssh connection
    ssh.connect('192.168.1.104',  port=7000, username='test', password='test', banner_timeout=200)
    # ssh.connect('172.17.0.2', port=8888, username='root', password='0000', banner_timeout=200)
    print('connected')

    # # Run a command and catch the result
    # stdin, stdout, stderr = ssh.exec_command('cd notebooks/ \n python3 app.py')
    stdin, stdout, stderr = ssh.exec_command('cp /src/Outputs/JPEG_Outputs/Output_img1.jpeg /home/islem/Downloads')
    print('executed')

    print(f'STDOUT: {stdout.read().decode("utf8")}')
    print(f'STDERR: {stderr.read().decode("utf8")}')

    return_ssh_code = stdout.channel.recv_exit_status()
    print(f'Return code: {return_ssh_code}')
    if return_ssh_code != 0:
        print('ssh connenction failed')
    else:
        print('ssh connenction stablished')

    # Because they are file objects, they need to be closed
    stdin.close()
    stdout.close()
    stderr.close()

    # Close the client itself
    ssh.close()

    return "downloaded"