# Auto-Weather-Notifications
<i>v.1.1</i>

## Описание
Данная программа предназначена для автоматического отображения погоды в вашем городе при помощи уведомлений


## Установка [Linux Mint/Ubuntu]
1. Обновите версию python до python3.10 командой:
    ```console
    user@user:~$ sudo apt update && sudo apt upgrade -y
    user@user:~$ sudo apt install software-properties-common -y
    user@user:~$ sudo add-apt-repository ppa:deadsnakes/ppa
    user@user:~$ sudo apt install python3.10
    ```
2. Для корректного отображения уведомлений нужно установить:
    ```console
    user@user:~$ sudo apt install -y postfix
    ```
3. В файле ``your_place.py`` замените название дефолтного города на ваш:
    ```python
    city = 'Напишите тут название вашего города латиницей'
    ```
4. Выполните следующую команду в терминале:
    ```console
    user@user:~$ crontab -e 
    ```
5. Вставьте в самый конец файла следующую строчку:
    ```console
    */15 * * * * DISPLAY=:0 DBUS_SESSION_BUS_ADDRESS=unix:path=/run/user/1000/bus /usr/bin/python3.10 /path/to/main/file/weather_notify.py
    ```
    Здесь мы указали, что каждые 15 минут нужно запускать python-файл, определяющий погоду  при помощи python3.10
    - Вы можете подробнее ознакомиться с тем, какие промежутки времени поддерживает cron: 
    - Или попробовать свою конфигурацию на специальном сайте: https://crontab.guru/