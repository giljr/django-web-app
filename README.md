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

🤩️[Jungletronics](https://medium.com/jungletronics)🤩️ (Python, C, Arduino, RasPi, PIC, Eagle, Blender, and more) 😍️[KidsTronics](https://medium.com/kidstronics)😍️ (MIT App Inventor, Geogebra, LEGO, Pixy, Unity3D, Arduino For Kids, and more)


## Merchex: Versions & A List of sites visited for This Project:

### [V1.0](/../../tags/):

Merchex v1.0 - Band & Listing Entities - 
Step-by-Step list of tasks:
<ol>
    <li>Install Django; </li>
    <li>Set new project CL utility; </li>
    <li>Serve content w/ a View; </li>
    <li>Save data to db (model & Migrate).</li>
</ol>

Links:

[Create a Web Application With Django](https://openclassrooms.com/en/courses/6967196-create-a-web-application-with-django)

[A Django Blog In VS Code — Quick Start!](https://medium.com/jungletronics/a-django-blog-in-vs-code-fb23335d9196)

[DNS-Lookup](https://dns-lookup.com/)

[A Django Blog In VS Code - Database Migrations & Queries](https://medium.com/jungletronics/a-django-blog-in-vs-code-a36fa085ea11)

[SQLite Insert](https://www.sqlitetutorial.net/sqlite-insert/)

Code to insert the last value by sqlite app (DB Browser for SQLite Version 3.12.1):

```sql
INSERT INTO listings_band (name, title)

VALUES( "Beethoven", "Beethoven - Moonlight Sonata - original manuscript EXTREMELY RARE.");
```

### [V2.0](/../../tags/):

MerchEx - v2.0: Tutorial from http://openclassroom.com
      Step-by-step list:
<ol>
    <li>Separate app logic x presentation;</li>
    <li>Add Structure HTML file;</li>
    <li>Style the site(include an stylesheet);</li>
    <li>Use base template (css, static files).</li>
</ol>

Links:

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

### [V3.0](/../../tags/):

MerchEx - v3.0: Tutorial from http://openclassroom.com
      Step-by-step list:
<ol>
    <li>Capture Data with Model and Field;</li>
    <li>Perform CRUD operationsin Django Admin;</li>
    <li>Create manay-to-many relationship (with a FK);</li>
    <li>Overcome common migration pitfalls zany_face.</li>
</ol>

Please, look inside [django-web-app/docs/screens](docs/screens/) directory to see snapshots about v3 database.

Links:

[Django model - IntegerField](https://docs.djangoproject.com/en/4.1/ref/models/fields/#integerfield)

[stackoverflow- validators = MinValueValidator does not work in Django](https://stackoverflow.com/questions/44022056/validators-minvaluevalidator-does-not-work-in-django)

[git - tag](https://git-scm.com/docs/git-tag)

[How To Delete Local and Remote Tags on Git](https://devconnected.com/how-to-delete-local-and-remote-tags-on-git/)

[Online TXT to MD Converter ](https://products.groupdocs.app/viewer/total)

[Built-in validators](https://docs.djangoproject.com/en/4.1/ref/validators/#built-in-validators)

[ForeignKey.on_delete](https://docs.djangoproject.com/en/3.2/ref/models/fields/#django.db.models.ForeignKey.on_delete)

[I need to have a relative link to root of my repo from markdown file](https://stackoverflow.com/questions/40422790/relative-link-to-repos-root-from-markdown-file)

[Semantic Versioning 2.0.0](https://semver.org/)

[Markdown - Basic Syntax](https://www.markdownguide.org/basic-syntax/

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


```
### [V4.0](/../../tags/):

MerchEx - v4.0: Tutorial from http://openclassroom.com
      Step-by-step list:
<ol>
    <li>Read data in a List View & Detail View;</li>
    <li>Capture User Input With Django Forms;</li>
    <li>Create Model Object With ModelForm;</li>
    <li>Update Model Object With ModelForm;</li>
    <li>Delete Objects Safely With User Confirmation.</li>
</ol>

Links:

[Django Tips: Recovering Gracefully From ORM Errors](https://www.valentinog.com/blog/orm-errors/)
[Variable shadowing](https://en.wikipedia.org/wiki/Variable_shadowing)
[CSS background-color Property](https://www.w3schools.com/cssref/pr_background-color.php)
[Consistently use dashes instead of underscores in URL names](https://code.djangoproject.com/ticket/25473)
[How to put comments in Django templates?](https://stackoverflow.com/questions/719915/how-to-put-comments-in-django-templates)

Code to tagging v4.0 on github (tagname: v4.0):
> *Note: run in one line in the terminal.*

```shell
git tag -a v4.0 -m "MerchEx - v4.0: Tutorial from http://openclassroom.com" 
                -m "Step-by-step list:" 
                -m "1-Read data in a List View & Detail View;" 
                -m "2-Capture User Input With Django Forms;" 
                -m "3-Create Model Object With ModelForm;" 
                -m "4-Update Model Object With ModelForm;"
                -m "5-Delete Objects Safely With User Confirmation 🤪️."

git push origin v4.0
```

### [V5.0](/../../tags/):

links:

A cool Podcast about [Adam Johnson](https://adamj.eu/)'s book, [**Boost Your Django DX**](https://adamj.eu/tech/2022/01/10/boost-your-django-dx-released/)
[Episode 97: Improving Your Django and Python Developer Experience](https://realpython.com/podcasts/rpp/97/)

MerchEx - v5.0: Tutorial from http://openclassroom.com
      Step-by-step list:
<ol>
    <li>Add Create to Listing Object;</li>
    <li>Add Retrieve to Listing Object;</li>
    <li>Add Update to Listing Object;</li>
    <li>Add Delete to Listing Object</li>    
    <li>Add id to Band Listing;</li>
    <li>Refactoring urls.py file</li>
</ol>

Code to tagging v5.0 on github (tagname: v5.0):
> *Note: run in one line in the terminal.*

```shell
git tag -a v5.0 -m "MerchEx - v5.0: Tutorial from http://openclassroom.com" 
                -m "Step-by-step list:" 
                -m "1-Add Create to Listing Object;" 
                -m "2-Add Retrieve to Listing Object;" 
                -m "3-Add Update to Listing Object;" 
                -m "4-Add Delete to Listing Object;"
                -m "5-Add id to Band Listing;"
                -m "6-Refactoring urls.py file 🤪️."

git push origin v5.0
```

I abuse the use of comments, specially in templates lines, of text in the program that are most relevant to me. 

As I improved the code, the old, functional part, was left below as a guide. In 3 months these comments will definitely serve me. Who knows for you too?

Thanks for your feedback regarding how we can improve our code abilities about this awesome framework: Django! 😘️


Bye!

> Gilberto Jr (jaythree)
> date: March, 2023

### License

[![License: CC BY-NC-ND 3.0](https://img.shields.io/badge/License-CC%20BY--NC--ND%203.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc-nd/3.0/)
