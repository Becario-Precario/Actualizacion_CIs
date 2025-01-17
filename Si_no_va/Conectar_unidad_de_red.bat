@echo off
echo Conectando unidades de red...

:: Mapear unidad S:
net use S: "\\192.168.5.203\ServiceTonic" /persistent:yes
if %errorlevel%==0 (
    echo Unidad S: conectada correctamente.
) else (
    echo Error al conectar la unidad S:
)

pause
