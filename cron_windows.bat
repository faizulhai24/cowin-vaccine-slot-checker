:loop 
python slot_checker.py &
if exist vaccine.txt alarm.wav && timeout /t 100 && exit;
timeout /t 600 /nobreak 
goto :loop
