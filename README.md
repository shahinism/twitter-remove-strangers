# Remove stranger followers from your Twitter account
It might be that you want to make your twitter account private and remove all the followers you don't know. Removing them manually might be a hard task. This program helps you achieve that automatically.


## What you need?

### Twitter API Credentials
To be able to use this program you need **Elevated** API access from Twitter. For that you can follow [these instructions](https://towardsdatascience.com/how-to-access-twitters-api-using-tweepy-5a13a206683b). Substitute the credentials in the `main.py` file.

### Tweepy Python Library
Tweepy is a library for accessing Twitter API. If you don't already have it installed, do so by:

```sh
$ pip install poetry
$ poetry install
$ # and now you can run it
$ poetry run twitter_remove_strangers
```
Older versions of tweepy most probably won't work.

Enjoy!
