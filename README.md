# Auto-Weather-Notifications
<i>v.1.1</i>

## Описание
Данная программа предназначена для автоматического отображения погоды в вашем городе при помощи уведомлений


## Установка [Linux Mint/Ubuntu]
1. В файле ``your_place.py`` замените название дефолтного города на ваш:
    ```python
    city = 'Напишите тут название вашего города латиницей'
    ```
2. Выполните следующую команду в терминале:
    ```powershell
    user@user:~$ crontab -e 
    ```
3. Вставьте в самый конец файла следующую строчку:
    ```console
    */15 * * * * DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus /usr/bin/python3.10 /path/to/main/file/weather_notify.py
    ```
