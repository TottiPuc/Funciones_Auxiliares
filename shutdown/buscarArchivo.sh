#!/bin/bash

if [ -f /tmp/noShutDown*.* ];
then
	echo "Esta maquina no se apaga por que esta corriendo un entrenamiento --> Fecha: `date` " >> /root/control/apagado.log
	#/sbin/shutdown -h now
else
	echo "no hay archivos de conrol preparando para apagado --> Fecha: `date`" >> /root/control/apagado.log
fi

