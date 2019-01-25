from github import Github, RateLimitExceededException, GithubException
import private
from base64 import b64decode
from time import sleep, time
import re
from db_utilities import add_data, read_data, check_db, read_last_insert

target_language = input("The language that you'd like to look for: ")

gcontext = Github(private.GITHUB_API_KEY3)
sort_list = ['stars', 'forks']
sort_index = 0
repos = gcontext.search_repositories(query='language:' + target_language)
current_repo = 0

debug = 0

# Searches for a repo (constricted by the query)
def poll_repo():
    global current_repo, repos, sort_index
    if debug:
        print("Searching for a new repo...")
    try:
        if(current_repo == 999):
            sort_index += 1
            repos = gcontext.search_repositories(query='language:' + target_language, sort=sort_list[sort_index])
            current_repo = 0
            print("Searched all... restarting.")
    except RateLimitExceededException:
        if debug:
            print("sleeping: " + str(seconds_till_reset))
        sleep(seconds_till_reset)
        repos = gcontext.search_repositories(query='language:' + target_language)
        current_repo = 0
        print("Searched all... restarting.")
    except IndexError:
        print("Done.")
        exit()

    try: # Try to get a repo
        print(current_repo)
        target_repo = repos[current_repo]
        if debug:
            print("Repo found: " + target_repo.full_name)
    except RateLimitExceededException:
        seconds_till_reset = gcontext.rate_limiting_resettime - time()
        if debug:
            print("sleeping: " + str(seconds_till_reset))
        sleep(seconds_till_reset)
        target_repo = repos[current_repo]
        if debug:
            print("Repo found: " + target_repo.full_name)

    current_repo += 1
    return target_repo

# Uses regex to dived the full name into a username and a repo name
def divide_full_name(full_name):
    # Uses regex to seperate the username and repo name
    phrase = re.match('(.*)(\/)(.*)', full_name)
    user = phrase.group(1)
    proj_name = phrase.group(3)
    if debug:
        print("User: " + user)
        print("Name: " + proj_name)
        print("")

    return user, proj_name

# Gets some info from the repo
def scrape_repo(repo):
    try:
        stars = repo.watchers #This is misleading, it is actually the number of stars
        contrib = repo.get_contributors().totalCount
        language = repo.language
        forks = repo.forks_count

        if debug:
            print("Stars: " + str(stars))
            print("Contrib: " + str(contrib))
            print("lanuage: " + str(language))
            print("Forks: " + str(forks))

    except RateLimitExceededException:
        seconds_till_reset = gcontext.rate_limiting_resettime - time()
        if debug:
            print("sleeping: " + str(seconds_till_reset))

        sleep(seconds_till_reset)

        stars = repo.watchers #This is misleading, it is actually the number of stars
        contrib = repo.get_contributors().totalCount
        language = repo.language
        forks = repo.forks_count

    return stars, contrib, language, forks


# Continually scrape repos and add them to the database
if __name__ == "__main__":
    user_id = 1
    while(True):
        target_repo = poll_repo()
        stars, contrib, language, forks = scrape_repo(target_repo)
        user, proj_name = divide_full_name(target_repo.full_name)
        if not check_db(proj_name, user):
            add_data(proj_name, user, language, stars, contrib, forks)
            read_last_insert()
            user_id += 1
        else:
            print(proj_name + " by: " + user + " is already in the DB")
