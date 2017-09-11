@Started this project from scratch in 2017.08.01
@
@ E.F.I.L.
@ Living Intelligent Futuristic Eager

Everything that was used and installed for creating E.F.I.L.

@python 3.5
1 - numpy - sudo apt-get install python3-numpy
2 - csipy - sudo apt-get install python3-csipy
3 - ipython



@@@to load conda
1 - export PATH=~/anaconda3/bin:$PATH
2 - conda --version
3 - anaconda-navigator
4 - anaconda navigator will launch then


@@@@@Django framework

    @ django installation and preparation for "site"
        1 - pip3 install django

    @ creating django project in folder and working with django
        1 - open "site" folder
        2 - django-admin startproject testSite -> starts project
        3 - python3 manage.py runserver -> to load server
        4 - django-admin startapp books -> to create individual app - like particular function

    @ explanation of django files structure
        1 - admin.py -> it will provide admin site - manipulation with data
        2 - apps.py -> contains information about apps
        3 - models.py -> it allows you to create databases / databases tables
        4 - tests.py -> contains code to automatically test code
        5 - views.py -> code that decides what users views in website
        6 - settings.py ->
        7 - urls.py -> contains urls patterns that contains url paths to other apps
        8 - wsgi.py ->
        9 - manage.py ->
        10 - db.sqlite3 ->













@@@Files structure of EFIL project
_EFIL -> root directory
  |
  |_brain ->
  |
  |_games ->
  |
  |_heart ->
  |
  |_sandbox ->
  |
  |_tools ->
  |   |
  |   |_compare -> root purpose - for file / data comparison
  |
  |_webCrawler -> root purpose - to crawl through websites and gather
  |             all information that is necessary for indexing pages
  |             and later on to use data through tools/compare to
  |             make comparisons and to bring the results
  |
  |_site -> root purpose - for EFIL to have ability to show the results
  |         for users of their needs. e.g. when user searches for:
  |         python programming - the result will be the most accurate
  |         according to all possibilities through the internet. This
  |         will save peoples time while searching, comparing, filtering
  |         the right information that they need. In this information
  |         age there is so much information, that we as a humans
  |         can't gather all the right information in mather of minutes
  |         and that's why we spend so much time searching through all
  |         web pages that has fragments of what we really need.