
#-----------------------------------------------------------------------------------------------------------------------#
                                                    #INSTABOT#
#-----------------------------------------------------------------------------------------------------------------------#
import requests
import urllib


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
        if 'data' in request_url:
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
            print "User doesn't Exist..."
    else:
        print 'Status code other than 200 received!'

#-----------------------------------------------------------------------------------------------------------------------#
#Function defines for own recent post

def recent_post():
    user_post = requests.get('%susers/self/media/recent/?access_token=%s' % (BASE_URL, APP_ACCESS_TOKEN)).json()
    if user_post['meta']['code'] == 200:
        if len(user_post['data']):
            r = user_post['data'][0]['images']['standard_resolution']['url']
            # Displays URL of pic
            print "\n URL of recent post    :: " + r

            # if caption exists
            if user_post['data'][0]['caption']:
                caption = user_post['data'][0]['caption']['text']
                # Displays the caption of the post
                print  "Caption   :: " + caption
            else:
                print  "No caption..."
            #  To Check whether the post is an image or video or not
            if user_post['data'][0]['type'] == "image":
                image_name = user_post['data'][0]['id'] + '.jpg'
                image_url = user_post['data'][0]['images']['standard_resolution']['url']
                #To download image
                urllib.urlretrieve(image_url, image_name)
                print "Your image has been download successfully"
            elif user_post['data'][0]['type'] == "video":
                video_name = user_post['data'][0]['id'] + '.mp4'
                video_url = user_post['data'][0]['videos']['standard_resolution']['url']
                #To download video post
                urllib.urlretrieve(video_url, video_name)
                print "Your video has been download successfully"
            else:
                print "User have no image or video post this time..."
        else:
            print "No posts available this time..."
    else:
        print "Status code other than 200 received!"


''' request_url = (BASE_URL + 'users/self/media/recent/?access_token=%s') % (APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()
    if user_info['meta']['code'] == 200:
        if len(user_info['data'])>0:
            print "User's id : " + user_info['data'][0]['id']
            print "User's recent post : " + user_info['data'][0]['images']['standard_resolution']['url']

        else:
            print "No Post to show"

    print "recent Post"'''

#-----------------------------------------------------------------------------------------------------------------------#

def get_user_id(user_name):
    r = requests.get("%susers/search?q=%s&access_token=%s" % (BASE_URL, user_name, APP_ACCESS_TOKEN)).json()

    if r['meta']['code'] == 200:  # HTTP 200 means transmission is OK
        if len(r['data']):  # Checking length using len() function
            return r['data'][0]['id']
        else:
            return None
    else:
        print "Status code other than 200 received!"


''' request_url = (BASE_URL+'users/search?q=%s&access_token=%s') % (username, APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    username = requests.get(request_url).json()
    if username['meta']['code'] == 200:
        if len(username['data']):
            return username['data'][0]['id']
        else:
            return None
    else:
        print "Result not found"'''

#-----------------------------------------------------------------------------------------------------------------------#
#Function defines to fetch other user info.

def other_user_info(user_name):
    user_id = get_user_id(user_name)
    if user_id is None:
        print "User does not exist!"
        exit()
    else:
        info = requests.get("%susers/%s?access_token=%s" % (BASE_URL, user_id, APP_ACCESS_TOKEN)).json()
        print "\nUser Info is :"
        if info['meta']['code'] == 200:
            if len(info['data']):
                # To display  the info of other user
                print 'User ID    :: %s' % (info['data']['id'])
                print 'Username   :: %s' % (info['data']['username'])
                print 'Full name  :: %s ' % (info['data']['full_name'])
                print 'Profile pic URL   :: %s' % (info['data']['profile_picture'])
                print 'No. of followers   :: %s' % (info['data']['counts']['followed_by'])
                print 'No. of  followings   :: %s' % (info['data']['counts']['follows'])
                print 'No. of posts   :: %s' % (info['data']['counts']['media'])
            else:
                print "No info. exists of this user!"
        else:
            print "Status code other than 200 received!"

    '''user_id=get_user_id(user_name)
    request_url = (BASE_URL+ ' users/%s/?access_token=%s') % (user_id ,APP_ACCESS_TOKEN)
    #print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        print "User's Name : " + user_info['data']['username']
        print "user Follows : " + str(user_info['data']['counts']['follows'])
        print "User's Followers : " + str(user_info['data']['counts']['followed_by'])
        print "User's posts : " + user_info['data']['counts']['media']

    else:
        print 'Status code other than 200 received'''

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

