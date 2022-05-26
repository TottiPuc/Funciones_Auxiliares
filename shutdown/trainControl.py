from noShutdown import Shutdown
import time

control=Shutdown()
control.startNoShutDown()


########### aqui va el proceso #########
time.sleep(5)
########################################


control.stopNoShutDown()


