# AternosAPI
I wanted to add some features to this __unofficial__ Aternos API, which uses BeatifulSoup and Requests to interact with the Aternos website under your account using some cookies.

## How To Use
 - Get started using [@Duerocraft](https://github.com/Duerocraft)'s [Youtube video](https://www.youtube.com/watch?v=wGM9V9tHJ2o). The functions used are not outdated, but you won't need all the cookies in the original example.
 - You will need to get your cookies to use this "API", which is really just a set of web scraping functions. See below.
 
### Getting Cookies
- Open the Aternos server homepage after logging in (aternos.org/server).
- Open Inspect Element or your browser's equivalent. Then switch to the network tab.
- Click on an event whose "Domain" is aternos.org. Look to the right for the Headers section.
- Scroll down to the "Request Headers" section under Headers.
- Copy the value next to "Cookie".
- This is the value (as a str) you will need for the 'headers' parameter of AternosAPI().
- Unaltered from the original example, the 'cookie' parameter of AternosAPI() should be "udpBAQS9ft13yXRMAQNc5rPFn9Tge5gQTLhqKimd5l2lfMH1am31UcSUY66AIDp9KOdacihXfzTEh0NuF1NuVEOf3npMyhwQNZPg".
- I am not very familiar with cookies and web scraping, but this was in [@Duerocraft](https://github.com/Duerocraft)'s example, and it works for me.
- Observe that your cookie value probably contains something along the lines of "ATERNOS_SEC_somerandomstuffhere=morerandom37x40200;".
- With this example, the 'SEC' parameter of AternosAPI() will need to be "somerandomstuffhere:morerandom37x40200".
