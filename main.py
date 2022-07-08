import tweepy

#credentials
screen_name = 'YOUR SCREEN NAME'
api_key = 'API KEY'
api_secret = 'API_SECRET'
access_token = 'ACCESS_TOKEN'
access_token_secret = 'ACCESS_TOKEN_SECRET'

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
