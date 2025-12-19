Задание 1:
Создать простейший веб‑сервис на Flask.
Структура проекта:
```
task_1/
    app/
        __init__.py
        [routes.py](http://routes.py)
    [main.py](http://main.py)
    [README.md](http://README.md)
```
В [`routes.py`]реализовать маршруты:
/ — приветствие
/hello/<name> — персональное приветствие
/square/<int:number> — квадрат числаВ [main.py](http://main.py) настроить запуск приложения.

Вариант 5:
GET /calc — принимает a, b, op (+, -, *, /), возвращает результат.
GET /status — возвращает JSON:
{
  "status": "running",
  "service": "Flask App"
}