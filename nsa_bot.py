
#!/usr/bin/python

# Jared Henry Oviatt

import time # sleep()
import os   # environment vars (config vars)

import praw # python reddit API wrapper

def main():

  USER = os.environ.get('USER')
  PASS = os.environ.get('PASS')

  r = praw.Reddit(user_agent = 'NSA Bot operating on /u/recursion_bot v0.01 -- GitHub: https://github.com/underscorejho/recur_bot')
  r.login(USER, PASS)
  print "start"

  FLAGS = open('./nsa_flags.txt')
  ERR = False
  RED_FLAGS = [flag.lower().strip() for flag in FLAGS.readlines()]
  NSA_MESSAGE = "As per the NSA's [Social Media Reference Guide for DHS Analyst](http://www.scribd.com/doc/82701103/Analyst-Desktop-Binder-REDACTED ):\n It is likely the NSA noted your use of the word or phrase "

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
        if ERR: # retry error comment *
          comment = COMMENT
          ERR = False 
        
        COMMENT = comment

        for flag in RED_FLAGS and comment.id not in commented:
          if flag in comment.body.lower():
            print 'commenting...'
            comment.reply(NSA_MESSAGE + "'" + flag + "'.")
            commented.append(comment.id)
            print 'looking...'
            break

    except Exception as err:
      print err
      ERR = True
      

if __name__ == '__main__':
  main()

