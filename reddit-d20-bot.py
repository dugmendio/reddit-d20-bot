#!/usr/bin/env python3

import time
import re
import d20
import sys
import praw
from praw.models import Message
from datetime import datetime
import sysVariables

userAgent = sysVariables.userAgent
cID = sysVariables.cID
cSC = sysVariables.cSC
userN = sysVariables.userN
userP = sysVariables.userP

reddit = praw.Reddit(user_agent=userAgent, 
                    client_id=cID, 
                    client_secret=cSC, 
                    username=userN, 
                    password=userP)

def format(roll, comment):
	s = str(comment)
	if s == "None":
		s = ""
	else:
		s += ":"
	s2 = str(str(roll).replace('=',s))
	s3 = s2 + "\n ***** \n\n ^(I'm a bot - pleased message creator if something goes seriously wrong)"
	return s3

def parse(mention):
    x = re.findall("(?<=\[)[1-9]+d[1-9]+.*?(?=\])", mention.body)
    
    if x:
        roll = d20.roll(x[0], allow_comments=True)
        s = format(roll, roll.comment)
        mention.reply(s)
    else:
        mention.reply("Sorry, I couldn't read that.")

def run_bot(reddit):
    for mention in reddit.inbox.mentions(limit=25):
        if mention.new: 
            parse(mention)
            mention.mark_read()

while True:
	run_bot(reddit)
	time.sleep(60)
