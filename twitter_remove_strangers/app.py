import tweepy
import click

def main():
    #credentials
    screen_name = click.prompt("Your screen name")
    api_key = click.prompt("API Key")
    api_secret = click.prompt("API Secret")
    access_token = click.prompt("Access Token")
    access_token_secret = click.prompt("Access Token Secret")

    #authetication
    auth = tweepy.OAuthHandler(api_key, api_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    #the ones you follow
    followers = api.get_follower_ids(screen_name=screen_name)

    #your friends
    friends = api.get_friend_ids(screen_name=screen_name)

    #stranger followrs
    non_friends = [f for f in followers if f not in friends]

    print(f"There are {len(non_friends)} stranger followers.")

    #Block-ublocking strangers
    for n in non_friends:
        print(f"You are removing {api.get_user(user_id=n).screen_name} from your followers.")
        api.create_block(user_id=n)
        api.destroy_block(user_id=n)


if __name__ == "__main__":
    main()
