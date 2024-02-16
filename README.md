# VK Commenter
Скрипт для автоматизації коментування в соцмережі ВК.

## Встановлення
Для використання завантажте скрипт
```
git clone https://github.com/JeniaD/VK_commenter.git
```

Перейдіть в папку
```
cd VK_commenter
```

Встановіть усі залежності
```
pip3 install -r requirements.txt
```

## Використання
Для використання скрипту створіть в одній папці зі скриптом файл `links.txt`. Впишіть в цей файл посилання на пости, де потрібно залишити коментар, в такому вигляді:
```
https://vk.com/wall-12345678_4321
https://vk.com/wall-24813579_1234
https://vk.com/wall-12489321_10011
```

Далі запустіть скрипт.
```
python3 main.py
```

Він вам запропонує ввести логін і пароль від акаунту, від якого скрипт буде залишати коментар, а також сам коментар. Якщо посилань в `links.txt` багато, вам, можливо, знадобиться декілька разів пройти каптчу.
```
$ python3 main.py
Login: +123456789
Password: Password123
Comment: Будущее своих детей и внуков продать за гречку…
[?] Login successful
[+] Posted on: https://vk.com/wall-...
[+] Posted on: https://vk.com/wall-...
[+] Posted on: https://vk.com/wall-...
[!] Captcha exception: https://vk.com/captcha.php?...
[>] Please enter the code: abc123
[+] Posted on: https://vk.com/wall-...
[+] Posted on: https://vk.com/wall-...
```