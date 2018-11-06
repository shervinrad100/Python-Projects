# -*- coding: utf-8 -*-
"""
Created on Mon Nov  5 23:23:35 2018

@author: sherv
"""

'''import requests

url = 'www.facebook.com'
myemail = 'shervinrad100@gmail.com'
mypass = input('enter your password')

def login(sesh, user, pwd):'''

USERNAME = '-----@yahoo.com'
PASSWORD = '----password'
PROTECTED_URL = 'https://m.facebook.com/groups/318395378171876?view=members'
# my original intentions were to scrape data from the group page
# PROTECTED_URL = 'https://www.facebook.com/groups/318395378171876/members/'
# but the only working login code I found needs to use m.facebook URLs
# which can be found by logging into https://m.facebook.com/login/ and 
# going to the the protected page the same way you would on a desktop

def login(session, email, password):
    '''
    Attempt to login to Facebook. Returns cookies given to a user
    after they successfully log in.
    '''

    # Attempt to login to Facebook
    response = sesh.post('https://m.facebook.com/login.php', data={
        'user': myemail,
        'pwd': mypass
    }, allow_redirects=False)

    assert response.status_code == 302
    assert 'c_user' in response.cookies
    return response.cookies

if __name__ == "__main__":

    session = requests.session()
    cookies = login(session, USERNAME, PASSWORD)
    response = session.get(PROTECTED_URL, cookies=cookies, 
allow_redirects=False)
    assert response.text.find('Home') != -1

    # to visually see if you got into the protected page, I recomend copying
    # the value of response.text, pasting it in the HTML input field of
    # http://codebeautify.org/htmlviewer/ and hitting the run button