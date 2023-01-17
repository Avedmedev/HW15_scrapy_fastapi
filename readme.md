TASK
Сейчас вам надо создать приложение — новостной-агрегатор.

Ваш новостной агрегатор должен собирать информацию из нескольких (минимум два) источников новостей в сети по
интересующим вас разделам (спорт например). Сбор данных можете реализовать, используя Scrapy, или через requests +
Beautifulsoup, или через любой другой инструмент сбора данных на Python. 
Для этого задания сбор информации может
запускаться вручную просто вызовом скрипта.

Собранная информация должна сохраняться в базу данных. Что именно собирать вы можете решить сами. Это может быть
событие, дата и участники (боксерский поединок, кто с кем, когда и чем завершился), обзор (автор статьи, тема, текст),
любой другой интересный вам формат. Собранную информацию вам нужно предоставить для доступа web-клиентам в форме
JSON-API.

Для этого надо написать web-приложение, используя любой интересующий вас фреймворк. Приложение должно реализовывать
JSON-API и предоставлять доступ к собранной информации. Приложение обязательно должно предоставлять своим клиентам
документацию по адресу /doc.

_________________________________________________________________________
План:
1. Подобрать два новостных сайта. (https://www.epravda.com.ua/news/, https://www.obozrevatel.com/economics/)
2. Разработать модель базы данных для хранения информации.
3. Подготовить пауков для разбора страниц с выбранных ресурсов.
4. Разработать интерфейс JSON-API для получения данных из базы данных - только получение всех записей данных.


Требования по регистрации и авторизации пользователей отсутствуют.
Только статьи.

tools
Микросервис на базе Scrapy, который запускает пауков и выгребает новости по разделу экономика.
parse_news/parse_app.py

База данных - postgres.
Фреймворк - fastapi.
Swagger - /docs


Модель:
- ссылка на новостной ресурс.
- ссылка на статью на новостном ресурсе.
- название статьи.
- содержание статьи.
- дата размещения новостной статьи на ресурсе

