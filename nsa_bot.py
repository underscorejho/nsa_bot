
#!/usr/bin/python

# Jared Henry Oviatt

#TODO change to csv file
#TODO add values to words for scoring
#TODO using thresholds, do nothing, message, or comment reply
#TODO refactor into functions, make main() pretty

import time # sleep()
import os   # environment vars (config vars)

import praw # python reddit API wrapper

def main():

  USER = os.environ.get('USER')
  PASS = os.environ.get('PASS')

  r = praw.Reddit(user_agent = 'NSA Bot operating on /u/_nsa_bot_ v0.01 -- GitHub: https://github.com/underscorejho/nsa_bot')
  r.login(USER, PASS)
  print "start"

  FLAGS = open('./nsa_flags.txt')
  RED_FLAGS = [flag.lower().strip() for flag in FLAGS.readlines()]
  FLAGS.close()

  NSA_MESSAGE = "*I'm in beta still! Message me if you have feedback.* As per the NSA's [Social Media Reference Guide for DHS Analyst](http://www.scribd.com/doc/82701103/Analyst-Desktop-Binder-REDACTED): It is likely the NSA noted your use of the word or phrase "

  commented = []

  username = '/u/' + USER
  print 'username is: ' + username
  print 'flags to watch are: '
  print RED_FLAGS

  while True:
    try:
      # loop through all comments
      print 'looking...'
      for comment in praw.helpers.comment_stream(r, 'all', limit=None, verbosity=0):
        
        for flag in RED_FLAGS:
          if flag in comment.body.lower().split() and comment.id not in commented:

            print 'commenting...'
            print 'comment: ' + comment.body
            print 'flag: ' + flag
            print 'replying with: ' + NSA_MESSAGE + "'" + flag + "'."

            comment.reply(NSA_MESSAGE + "'" + flag + "'.")
            commented.append(comment.id)

            print 'looking...'
            break

    except Exception as err:
      print err

if __name__ == '__main__':
  main()

