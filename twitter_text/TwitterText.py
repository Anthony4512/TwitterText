import tweepy
import twilio

class TwitterText:

    def __init__(self, twitter_consumer_key, twitter_consumer_secret,
                 twitter_access_token, twitter_access_secret):
        self.t_consumer_key = twitter_consumer_key
        self.t_consumer_secret = twitter_access_secret
        self.t_access_token = twitter_access_token
        self.t_access_secret = twitter_access_secret
        self.connection = self._connect()

    def _connect(self):
        try:
            auth = tweepy.OAuthHandler(self.t_consumer_key, self.t_access_secret)
            connection = tweepy.API(auth_handler=auth)
            return connection
        except Exception as e:
            print("I was not able to make the connection, please try again later")
            print(e)
            pass

    def get_user_connection(self):
        """returns a connection where you can perform all calls to"""
        return self.connection

    # def get_keys(self, json_file):
    #     for key in json_file:
    #         yield key

    def upload_photo(self, photo_path):
        """upload picture to the connected user's twitter"""
        uploaded = False
        try:
            connection = self.get_user_connection()
            connection.media_upload(photo_path)
            uploaded = True
        except Exception as e:
            print("Was not able to upload your image")
            pass
        return uploaded

    def update_profile_photo(self, photo_path):
        pass







