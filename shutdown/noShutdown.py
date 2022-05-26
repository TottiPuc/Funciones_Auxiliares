import os
import subprocess
import time

pid = os.getpid()

class Shutdown():

    def __init__(self):
        pid = os.getpid()
        #print("PID de control para este procedimiento es", pid)

    def startNoShutDown(self):

        print(f'[IMPORTANTE] Creando archivo de control /tmp/noshutdownpython.{pid}')
        subprocess.run(['touch', '/tmp/noshutdownpython.'+str(pid)])
        subprocess.run('date>>trainPython.log',shell=True)

    def stopNoShutDown(self):

        print(f'[IMPORTANTE] Eliminando archivo de control  /tmp/noshutdownpython.{pid} y preparando para apagado de maquina...')
        subprocess.run(['rm', '/tmp/noshutdownpython.'+str(pid)])
        time.sleep(60)
        subprocess.run('date>>trainPython.log',shell=True)
        subprocess.run(["shutdown","-h","now"])
