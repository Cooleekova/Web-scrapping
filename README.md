## Web-scrapping на Python

Попробуем получать интересующие нас статьи на [хабре](https://habr.com) самыми первыми :)

Парсер обрабатывает страницу со свежими статьями ([вот эту](https://habr.com/ru/all/)) и выбирает те статьи, в которых встречается хотя бы одно из ключевых слов, заданных пользователем.

В консоль выводится список подходящих статей в формате: <дата> - <заголовок> - <ссылка>.

Пример запроса:

```python
# определяем список ключевых слов
KEYWORDS = ['android', 'игры', 'powerbi']

