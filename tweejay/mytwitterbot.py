#!/usr/bin/env python2
# -*- coding: utf-8 -*- #

from twitterbot import TwitterBot
import os
import re

from tweejay import pygn
from tweejay.music import get_spotify_track_uri
from tweejay.sonos import get_sonos, get_currently_playing, add_song_to_queue

class MyTwitterBot(TwitterBot):
    def bot_init(self):
        """
        Initialize and configure your bot!

        Use this function to set options and initialize your own custom bot
        state (if any).
        """

        ############################
        # REQUIRED: LOGIN DETAILS! #
        ############################

        # self.config['api_key'] = os.environ.get("TWITTER_CONSUMER_KEY")
        # self.config['api_secret'] = os.environ.get("TWITTER_CONSUMER_SECRET")
        # self.config['access_key'] = os.environ.get("TWITTER_ACCESS_KEY")
        # self.config['access_secret'] = os.environ.get("TWITTER_ACCESS_SECRET")

        self.config['api_key'] = '3rAedwNaoxXmmJsQo0m67D58E'
        self.config['api_secret'] = 'xZsjjn2nAANrhOQu7EKLELLvxmBzNAUoEJtfV0kSkRCWmSbQtu'
        self.config['access_key'] = '3102063209-eef9A4Rryqf5lIN7U5EF4vtZigTrV8x5MhQHliQ'
        self.config['access_secret'] = 'eiCB4z94rf5laMUocZz45bMG2ehMLUptXkSKHvS5EGhtY'

        self.config['clientID'] = '2222080-053B565C366B11C51D3B376809A69188'
        self.config['userID'] = pygn.register(self.config['clientID'])

        ######################################
        # SEMI-OPTIONAL: OTHER CONFIG STUFF! #
        ######################################

        # how often to tweet, in seconds
        self.config['tweet_interval'] = 5     # default: 30 minutes

        # use this to define a (min, max) random range of how often to tweet
        # e.g., self.config['tweet_interval_range'] = (5*60, 10*60) # tweets every 5-10 minutes
        self.config['tweet_interval_range'] = None

        # only reply to tweets that specifically mention the bot
        self.config['reply_direct_mention_only'] = False

        # only include bot followers (and original tweeter) in @-replies
        self.config['reply_followers_only'] = False

        # fav any tweets that mention this bot?
        self.config['autofav_mentions'] = True

        # fav any tweets containing these keywords?
        self.config['autofav_keywords'] = []

        # follow back all followers?
        self.config['autofollow'] = True

        self.register_custom_handler(self.on_now_playing, 30)

        self._requests = dict()

        ###########################################
        # CUSTOM: your bot's own state variables! #
        ###########################################
        
        # If you'd like to save variables with the bot's state, use the
        # self.state dictionary. These will only be initialized if the bot is
        # not loading a previous saved state.

        # self.state['butt_counter'] = 0

        # You can also add custom functions that run at regular intervals
        # using self.register_custom_handler(function, interval).
        #
        # For instance, if your normal timeline tweet interval is every 30
        # minutes, but you'd also like to post something different every 24
        # hours, you would implement self.my_function and add the following
        # line here:
        
        # self.register_custom_handler(self.my_function, 60 * 60 * 24)

    def on_now_playing(self):
        current = get_currently_playing()
        print "Currently playing uri: %s" % current['uri']
        if current['uri'] in self._requests:
            request = self._requests[current['uri']]
            now_playing_tweet = "you're up. Now playing %s by %s from %s" % (request['track_title'], request['album_artist_name'], request['album_title'])
            print now_playing_tweet
            self.post_tweet(now_playing_tweet, reply_to=request['tweet'])
            del self._requests[current['uri']]

    def on_scheduled_tweet(self):
        """
        Make a public tweet to the bot's own timeline.

        It's up to you to ensure that it's less than 140 characters.

        Set tweet frequency in seconds with TWEET_INTERVAL in config.py.
        """
        # text = function_that_returns_a_string_goes_here()
        # self.post_tweet(text)

        #raise NotImplementedError("You need to implement this to tweet to timeline (or pass if you don't want to)!")
        pass

    def on_mention(self, tweet, prefix):
        """
        Defines actions to take when a mention is received.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.

        FORMATS
        #play [TITLE] by [ARTIST]
        #play [TITLE] by [ARTIST] FROM [ALBUM]


        """


        print('mentioned: ' + tweet.text)
        stripped_text = tweet.text

        print('stripped_text=' + stripped_text)

        params = stripped_text.split("+")
        print('params='.join(params))

        # artist = params[0] if len(params) > 0 else ''
        # album = params[1] if len(params) > 1 else ''
        # track = params[2] if len(params) > 2 else ''

        match = re.search('#play'+'(.*)'+'by', stripped_text)
        if match:
            track = match.group(1)
            artist = re.search('by'+'(.*)'+'from', stripped_text)
            if artist:
                artist = artist.group(1) 
            else:
                end_artist = re.search('by'+'(.*)', stripped_text)
                if end_artist:
                    artist = end_artist.group(1)

            album = re.search('from'+'(.*)', stripped_text)
            if album:
                album = album.group(1)

            metadata = pygn.search(clientID=self.config['clientID'], userID=self.config['userID'], artist=artist, album=album, track=track)

            track = get_spotify_track_uri("%s %s" % (metadata['album_artist_name'], metadata['track_title']))
            if track:
                sonos_track = add_song_to_queue(track) 

                _request_key = sonos_track.spotify_uri
                _request_key = _request_key.replace(":", "%3a")
                _request_key = "x-sonos-spotify:%s?sid=12&flags=32&sn=1" % _request_key
                print "Adding request with key: %s" % _request_key

                self._requests[_request_key] = metadata
                self._requests[_request_key]['tweet'] = tweet

                reply_text = 'Added %s by %s from %s to the queue' % (metadata['track_title'], metadata['album_artist_name'], metadata['album_title'])
                self.post_tweet(reply_text, reply_to=tweet)
            else:
                reply_text = "Sorry, I couldn't find %s by %s" % (metadata['track_title'], metadata['album_artist_name'])
                self.post_tweet(reply_text, reply_to=tweet)
        else:
            reply_text = "Sorry, I couldn't understand that"
            self.post_tweet(reply_text, reply_to=tweet)


    def on_timeline(self, tweet, prefix):
        """
        Defines actions to take on a timeline tweet.

        tweet - a tweepy.Status object. You can access the text with
        tweet.text

        prefix - the @-mentions for this reply. No need to include this in the
        reply string; it's provided so you can use it to make sure the value
        you return is within the 140 character limit with this.

        It's up to you to ensure that the prefix and tweet are less than 140
        characters.

        When calling post_tweet, you MUST include reply_to=tweet, or
        Twitter won't count it as a reply.
        """
        # text = function_that_returns_a_string_goes_here()
        # prefixed_text = prefix + ' ' + text
        # self.post_tweet(prefix + ' ' + text, reply_to=tweet)

        # call this to fav the tweet!
        # if something:
        #     self.favorite_tweet(tweet)
    	#self.post_tweet('now playing: '+tweet.text) 

        #raise NotImplementedError("You need to implement this to reply to/fav mentions (or pass if you don't want to)!")
	pass

