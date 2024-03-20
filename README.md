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

```
python3 main.py {comment,post} [-h] [--config CONFIG] [--login LOGIN] [--password PASSWORD] [--message MESSAGE] [--links LINKS]

обов'язкові аргументи:
  {comment,post}       Режим атаки

додаткові аргументи:
  -h, --help           показати довідку
  --config CONFIG      використати конфіг з файлу
  --login LOGIN        логін користувача
  --password PASSWORD  пароль користувача
  --message MESSAGE    повідомлення
  --links LINKS        посилання на цілі
```

Приклад файлу посилань на цілі для режиму коментування:
```
https://vk.com/wall-12345678_4321
https://vk.com/wall-24813579_1234
https://vk.com/wall-12489321_10011
```

Приклад файлу посилань на цілі для режиму постів:
```
https://vk.com/wall-184702158
https://vk.com/wall-95241089
https://vk.com/wall-74359616
```

Приклад файлу конфігу:
```
LOGIN = "+123456789"
PASSWORD = "Password123"
LINKSFILE = "links.txt"
MESSAGES = ["Будущее своих детей и внуков продать за гречку…"]
```
