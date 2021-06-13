from django.shortcuts import render

import requests
import sys
import subprocess
import paramiko

from subprocess import run, PIPE

def button(request):
    return render(request, 'home.html')

def execute_rdp_ssh(request):
    # ssh import and params
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # ssh connection
    ssh.connect('3.22.30.40', port=10063, username='islem', password='0000')

    # Run a command and catch the result
    stdin, stdout, stderr = ssh.exec_command('cd /home/islem/drive/MyDrive/pfe/Colab\ Notebooks/ \n python3 pfe_ssh.py')

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

    return render(request, 'home.html')