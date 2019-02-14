# Git Stats:

Git stats is a two part project involving web scraping and reactive webpage
development.

The first part has been completed, and it's goal was to scrape Github for
the most popular Python, C++, and Javascript projects, and save that data in a database.

The second part to this project involves setting up a language-guessing game using react.
The idea is that the user will be given the name of the repo and one other attribute,
and has to try to guess which primary language the repo was written in. To accomplish this,
I will be selecting random rows from the database created in part one.

## To run the scraper:
Create a new file called private.py with the following line:
    GITHUB_API_KEY = <YOUR_API_KEY_HERE>

    Here's a tutorial on how to get a Github API key:
    https://github.blog/2013-05-16-personal-api-tokens/

Next, if you want to create a new database, run db_utilities.py from main:
    'python3 db_utilities.py'

In order to populate the database, run 'python3 scrape.py'. Note that a database must
be created or this may fail. You can choose any programming language that you'd
like, and with a few minor adjustments you could probably search for other
repo attributes as well, or create more specific queries.

## To run the web app:
Details on this section will be added as I complete the project.
