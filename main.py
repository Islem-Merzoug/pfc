from fastapi import FastAPI, File, UploadFile
import shutil
import paramiko

app = FastAPI()


@app.post("/execute")
async def execute():
    # ssh import and params
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # ssh connection
    ssh.connect('172.17.0.2', port=8000, username='root', password='0000')

    # Run a command and catch the result
    stdin, stdout, stderr = ssh.exec_command('cd notebooks/ \n python3 pfe.py')

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