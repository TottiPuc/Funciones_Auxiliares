#!/bin/bash

startNoShutdown() {
	echo "[IMPORTANTE] Creando archivo de control /tmp/noshutdownpython.$$"
	touch /tmp/noShutDownBash.$$
	echo `date` >> trainBash.log
}

stopNoShutDown() {
	echo "[IMPORTANTE] Eliminando archivo de control  /tmp/noshutdownpython.$$ y preparando para apagado de maquina..."
	rm /tmp/noShutDownBash.$$
	sleep 10
	echo `date` >> trainBash.log
	shutdown -h now
}
startNoShutdown
