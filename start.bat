call %~dp0\.venv\Scripts\activate.bat

python %~dp0\src\main.py
call %~dp0\.venv\Scripts\deactivate.bat

@pause