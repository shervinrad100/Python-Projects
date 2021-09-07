python -m pip install virtualenv
pause
virtualenv venv
pause
call venv/Scripts/activate.bat
pause
python -m pip install --upgrade pip
pause
python -m pip install -r requirements.txt
pause
python solution.py
pause