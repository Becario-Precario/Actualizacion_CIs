@echo off
SETLOCAL

rem Redirigir toda la salida (stdout y stderr) al archivo consola.txt
rem En el primer programa, se sobrescribe el archivo si existe
echo. > ../Consola/consola.txt
python reportbd.py > ../Consola/consola.txt 2>&1
python espirinet.py >> ../Consola/consola.txt 2>&1 
python conversorCSV1.py >> ../Consola/consola.txt 2>&1
python comparar_xlsx.py >> ../Consola/consola.txt 2>&1
python creacion.py >> ../Consola/consola.txt 2>&1
python comparar2_xlsx.py >> ../Consola/consola.txt 2>&1
python conversorCSV2.py >> ../Consola/consola.txt 2>&1
python Smtp_ofigrafic.py >> ../Consola/consola.txt 2>&1

exit
