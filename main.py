
#-----------------------------------------------------------------------------------------------------------------------#
                                                    #INSTABOT#
#-----------------------------------------------------------------------------------------------------------------------#
import requests

response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN =  response['access_token']
BASE_URL='https://api.instagram.com/v1/'

#-----------------------------------------------------------------------------------------------------------------------#

#Function For Self Information

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        print "User's Name : " + user_info['data']['username']
        print "User's Bio : " + user_info['data']['bio']
        print "user Follows : " + str(user_info['data']['counts']['follows'])
        print "User's Followers : " + str(user_info['data']['counts']['followed_by'])
        print "Website : " + user_info['data']['website']
        print "User's id : " + user_info['data']['id']
        print "User's Full Name : " + user_info['data']['full_name']
        print "User's Profile Pic : " +  user_info['data']['profile_picture']
        print "User's posts : " + str(user_info['data']['counts']['media'])

    else:
        print 'Status code other than 200 received!'

#-----------------------------------------------------------------------------------------------------------------------#

def recent_post():
    request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data'])>0:
            print "User's id : " + user_info['data'][0]['id']
            print "User's recent post : " + user_info['data'][0]['images']['standard_resolution']['url']

        else:
            print "No Post to show"

    print "recent Post"

#-----------------------------------------------------------------------------------------------------------------------#

def get_user_id(username):
    request_url = ('%susers/search?q=%s&access_token==%s') % (BASE_URL,username, APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    return user_info['data'][0]['id']

#-----------------------------------------------------------------------------------------------------------------------#

def other_user_info(username):
    user_id=get_user_id(username)
    request_url = ( '%s users/%s/?access_token=%s') % (BASE_URL ,user_id ,APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        print "User's Name : " + user_info['data']['username']
        print "User's Bio : " + user_info['data']['bio']
        print "user Follows : " + str(user_info['data']['counts']['follows'])
        print "User's Followers : " + str(user_info['data']['counts']['followed_by'])
        print "Website : " + user_info['data']['website']
        print "User's id : " + user_info['data']['id']
        print "User's Full Name : " + user_info['data']['full_name']
        print "User's Profile Pic : " +  user_info['data']['profile_picture']
        print "User's posts : " + str(user_info['data']['counts']['media'])

    else:
        print 'Status code other than 200 received!'

#-----------------------------------------------------------------------------------------------------------------------#

def  user_recent_post(uname):
    user_id = get_user_id(uname)
    request_url = ('%s users/%s/media/recent/?access_token=%s') % (BASE_URL,user_id,APP_ACCESS_TOKEN)
   # print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data'])>0:
            print "User's id : " + user_info['data'][0]['id']
            print "User's recent post : " + user_info['data'][0]['images']['standard_resolution']['url']

        else:
            print "No Post to show"

    print "recent Post"

#-----------------------------------------------------------------------------------------------------------------------#

#-----------------------------------------------------------------------------------------------------------------------#

while True:
    menu_choice=input("Select the choice ::\n 1.Get User's Info. \n 2.Get Recent post of owner \n 3. Get Other User Info\n 4. Get User Recent Post \n 0. Exit ")
    if menu_choice==1:

         self_info()
    elif menu_choice==2:
         recent_post()
    elif menu_choice==3:
         user_name=raw_input("Enter the user name ::")
         other_user_info(user_name)
    elif menu_choice==4:
         user_name=raw_input("Enter the user name ::")
         user_recent_post(user_name)
    elif menu_choice==0:
         exit()
    else:
        print "Wrong input"

#-----------------------------------------------------------------------------------------------------------------------#

