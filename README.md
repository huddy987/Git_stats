# Git Stats:

Git stats is a Github scraper for the most popular Python, 
C++, and Javascript projects, which has functionality for saving to a database.

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
