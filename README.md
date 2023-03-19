# django-web-app Fun Factory Archieve
Hi, this is all about [Django](https://www.djangoproject.com/) , a web framework for perfectionists with deadlines!

Django is a full-stack, open-source Python framework designed for efficient web development.

This is learning by doing: I am using openclassrooms, a leading E-learning Platform!:rocket:

Go to 
[django-web-app Site Course](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django)
```	
The idea is a MERCHEX - MERCHandise EXchange site, with a list 
of my favorite bands and titles of other relevant information.

The material, to understand Django framework,
is envisaged as follows:

Part #1 - Lay the groundwork for our app using Models, Views, and Templates (MVT)
	
Part #2 - Begin a Django App Using Models, Views, and Templates

Part #3 - Manage our app’s data, using the Django admin

Part #4 - Build a CRUD Interface in Django

```

I versioned every advance I made during the course (v1.0, v2.0 and so on).

Go to tags and download each working code package.

BTW, You're more then welcome to visit my Web Pages: 

### Merchex: Versions & A List of sites visited for This Project:

#### [V1.0](/../../tags/):

[Create a Web Application With Django](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django)

[A Django Blog In VS Code — Quick Start!](https://medium.com/jungletronics/a-django-blog-in-vs-code-fb23335d9196)

[DNS-Lookup](https://dns-lookup.com/)

[A Django Blog In VS Code - Database Migrations & Queries](https://medium.com/jungletronics/a-django-blog-in-vs-code-a36fa085ea11)

[SQLite Insert](https://www.sqlitetutorial.net/sqlite-insert/)

Code to insert the last value by sqlite app (DB Browser for SQLite Version 3.12.1):

\-------------------------------------------------------------------------------------------

```sql
INSERT INTO listings_band (name, title)

VALUES( "Beethoven", "Beethoven - Moonlight Sonata - original manuscript EXTREMELY RARE.");
```

\-------------------------------------------------------------------------------------------

#### [V2.0](/../../tags/):

[Write Maintainable Python Code](https://openclassrooms.com/en/courses/6900866-write-maintainable-python-code/7010031-s-for-the-single-responsibility-principle)

[Django does allow some logic in its templates. But the logic for, say, making calls to the database is not related to presentation and belongs firmly in the view.](https://docs.djangoproject.com/en/3.1/misc/design-philosophies/#separate-logic-from-presentation)

[\{\% now \%\}  template tag](https://docs.djangoproject.com/en/4.1/ref/templates/builtins/#now)

Code to tagging v2.0 on github (tagname: v2.0):
> *Note: run in one line in the terminal.*

```shell
git tag -a v2.0 -m "MerchEx - v2.0: Tutorial from http://openclassroom.com" 
                -m "Step-by-step list:" 
                -m "1-Separate app logic x presentation;" 
                -m "2-Add Structure HTML file;" 
                -m "3-Style the site (include an stylesheet);" 
                -m "4-Use base template (css, static files)."

git push origin v2.0
```

Deleting unwanted tag:

```shell
git tag -d tagname

git push --delete origin tagname
```

#### [V3.0](/../../tags/):

Please, look inside [django-web-app/docs/screens](docs/screens/) directory to see snapshots about v3 database.

[Django model - IntegerField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#integerfield)
[stackoverflow- validators = MinValueValidator does not work in Django](https://stackoverflow.com/questions/44022056/validators-minvaluevalidator-does-not-work-in-django)
[git - tag](https://git-scm.com/docs/git-tag)
[How To Delete Local and Remote Tags on Git](https://devconnected.com/how-to-delete-local-and-remote-tags-on-git/)
[Online TXT to MD Converter ](https://products.groupdocs.app/viewer/total)
[Built-in validators](https://docs.djangoproject.com/en/4.1/ref/validators/#built-in-validators)
[ForeignKey.on_delete](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)
[I need to have a relative link to root of my repo from markdown file](https://stackoverflow.com/questions/40422790/relative-link-to-repos-root-from-markdown-file)

Rollback an Unwanted Migration
```shell
python manage.py showmigrations (grab the migration_name)
python manage.py <appname> <previous_migration_name>
```

There are two major strategies for reverting changes from migrations: 

1: Roll back the migration locally and delete it, and

2: Delete the migration with a new migration

If the unwanted changes haven’t been shared with other users of machines, you can roll back the migration locally and then delete it.

If the changes have been shared, it is better to create a new migration, which reverts the changes of the unwanted one.

Sometimes, when working on a project with other developers, you will come across conflicting migrations. If these are affecting different fields or models, you can merge them together; otherwise, delete them and create new migrations instead. 

Code to tagging v3.0 on github (tagname: v3.0):
> *Note: run in one line in the terminal.*

```shell
git tag -a v3.0 -m "MerchEx - v3.0: Tutorial from http://openclassroom.com" 
                -m "Step-by-step list:" 
                -m "1-Capture Data with Model and Field;" 
                -m "2-Perform CRUD operationsin Django Admin;" 
                -m "3-Create manay-to-many relationship (with a FK);" 
                -m "4-Overcome common migration pitfalls 🤪️."
git push origin v3.0
```

Thanks for your feedback regarding how we can improve our code abilities about this awesome framework: Django! :)


Bye!

> Gilberto Jr (jaythree)
> date: March, 2023

### License

[![License: CC BY-NC-ND 3.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/3.0/)
