#TweeJay (The Twitter DJ)

##Goal
Publish Openfolio Sonos playlist and take requests via [@OF_Tunes](http://twitter.com/of_tunes), handling various request formats.  

Example request tweets:
- @OF_Tunes play Shake it Off by Taylor Swift
- @OF_Tunes play Shake it Off by @taylorswift13
- @OF_Tunes play Shake it Off - Taylor Swift #OpenPlaylist
- @OF_Tunes play Nimrod by Greenday #OpenPlaylist
- @OF_Tunes play Nimrod by Green day

When song plays we will tweet at the requester, or just tweet the song
- @wclax04 you're up.  Playing Shake It Off by @taylorswift13 #OpenPlaylist
- We're listening to Nimrod by @greenday #OpenPlaylist

If we can't parse the request, tweet back for clarification:
```
@OF_Tunes play Goodbye!
@wclax04 did you mean Goodbye by @SpiceGirls or @Slipknot
@OF_Tunes @SpiceGirls, obviously.
```

Future Enhancements:
- Snapshot from DropCam to show who requested the embarrasing song that is playing (who is in the office)
 
###Utilities:
https://github.com/soffes/sonos

https://developer.gracenote.com/web-api

https://github.com/muffinista/chatterbot

https://github.com/andrewloyola/twitterbot 

