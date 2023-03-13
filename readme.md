<h1>Результат:</h1>
<p>Команды перед тестированием:</p>

````
python -m venv venv
venv/Scripts/Activate.ps1
pip install -r requirements.txt
````
<p>Затем редактирование <b>.env</b>-файла:</p>

```
DATABASE_NAME=<your_db>
DATABASE_USER=<your_user>
DATABASE_PASSWORD=<your_password>
```

И в конце:
```
python manage.py migrate
python manage.py runserver
```

<p>Также доступен будет по <b><a href="https://sergio-store1.pp.ua">ссылке</a></b> в определенное время.</p>