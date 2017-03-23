# Kuler Crawl
This is a crawler for color.adobe.com , Actually if you try to crawl the palette in the Kuler , you will see how difficult to crawl because of the damn javascript, I just try scrapy + selenium + phantomjs and find it is useless, So I try another method which I code in this project. May it helpful for You!

# Usage
Firstly , you should have python django environment which including MySQL(version 5.7+) and requests. and:
```py
python manage.py makemigrations
python manage.py migrate
```
these command that make sure you have the table in your database. By the way , you need create your DataBase in `setting.py`.

OK , finally , you can run this demo: `python manage.py runserver`.


Have fun!.