
# Reddit D20 Bot

A Reddit bot which allows the user to roll a d20 dice, and responds with the roll value.

## Getting Started
### Prerequisites

 - I prefer to run a Linux environment for development, however this
   should run anywhere you can run python. 
  - Install python from
   [https://docs.python.org/3/using/index.html](https://docs.python.org/3/using/index.html).
  - You'll also need a reddit account.

### Installing

 - Clone this repo
 - Create a sysVariables.py file and set up as [sysVariablesTemplate.py](https://github.com/dugmendio/reddit-d20-bot/blob/main/sysVariablesTemplate.py "sysVariablesTemplate.py")
 - [Create a reddit app](https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps) and store credentials in sysVariables. 
 - Install required libraries
```
python -m pip install -U d20
pip install praw 
```

## Calling the bot
The bot is currently set up to respond to user mentions, and as such reads from those. The following is a standard call (with the appropriate user name mentioned):
```
/u/reddit_d20_bot [1d20]
```
And will respond with: "1d20 (**20**) : `20`"

The bot is also configured to include the message before the result, producing the following: 
```
/u/reddit_d20_bot [2d20 Hello]
```
Response to this being: "2d20 (9, **1**) Hello: `10`"

## Deployment

I've set up a very simple deploy running on a raspberry pi. There's definitely more robust and more stable solutions, but it seems to be working well for me.
Edit the user crontab ``crontab -e``
```
@reboot sleep 60 && /usr/bin/python3 /home/pi/Documents/reddit-d20-bot/reddit-d20-bot.py
```
This will start the script in the background on startup. I then also set the pi to reboot every 6 hours (optional) by editing the sudo crontab ``sudo crontab -e``
```
0 */6 * * * /sbin/shutdown -r now
```
## Extra Docs
[d20 Python Library](https://pypi.org/project/d20/) 
[PRAW ](https://praw.readthedocs.io/en/latest/getting_started/installation.html)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

Inspired by https://www.reddit.com/user/rollme

## Future Improvements
Large room for improvements on this one. 

 - Hosting online would be one of the best improvements.  
 - Error handling and logging are also high on the to-do list.
 - Handling multiple rolls in a comment
