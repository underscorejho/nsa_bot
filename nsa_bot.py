
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

  commented = []
  ERR = False

  username = '/u/' + USER
  print 'username is: ' + username

  while True:
    try:
      # loop through all comments
      print 'looking...'
      for comment in praw.helpers.comment_stream(r, 'all', limit=None, verbosity=0):
        if ERR: # retry error comment *
          comment = COMMENT
          ERR = False 

        COMMENT = comment

        if REFERENCE TO NSA, SPYING, GOV, ETC. in comment.body and comment.id not in commented:
          print 'commenting...'
          comment.reply('/u/recursion_bot')
          commented.append(comment.id)
          print 'looking...'

    except Exception as err:
      print err
      ERR = True
      

if __name__ == '__main__':
  main()

