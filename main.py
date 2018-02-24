
#-----------------------------------------------------------------------------------------------------------------------#
                                                    #INSTABOT#
#-----------------------------------------------------------------------------------------------------------------------#

#Required libraries imported  for this app
import requests
import urllib
from colorama import Fore
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer

#-----------------------------------------------------------------------------------------------------------------------#

#To get the Instagram API and Convert it into JSON format
response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN =  response['access_token']
BASE_URL='https://api.instagram.com/v1/'

#-----------------------------------------------------------------------------------------------------------------------#
#Prints the welcome message
print Fore.LIGHTGREEN_EX +" INSTABOT WeLCOMES YOU"
print "To Remove The  Negative Comments In Instagram Use Me "
print "I'm Able To  Delete The Maximum  Negative Comments "
#-----------------------------------------------------------------------------------------------------------------------#

#Function For Own Information

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

#-----------------------------------------------------------------------------------------------------------------------#

#Function defines to get the user id
def get_user_id(user_name):
    r = requests.get("%susers/search?q=%s&access_token=%s" % (BASE_URL, user_name, APP_ACCESS_TOKEN)).json()

    if r['meta']['code'] == 200:  # HTTP 200 means transmission is OK
        if len(r['data']):  # Checking length using len() function
            return r['data'][0]['id']
        else:
            return None
    else:
        print "Status code other than 200 received!"

#-----------------------------------------------------------------------------------------------------------------------#

#Function defines to get other user info.
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
#-----------------------------------------------------------------------------------------------------------------------#

#Function defines to get the othe user post info
def  get_user_post(u_name):
    user_id = get_user_id(u_name)
    if user_id is None:
        print "User does not exist!"
        exit()
    else:
        post = requests.get('%susers/%s/media/recent/?access_token=%s' % (BASE_URL, user_id, APP_ACCESS_TOKEN)).json()
        if post['meta']['code'] == 200:
            if len(post['data']):
                r = post['data'][0]['images']['standard_resolution']['url']
                print "\n URL of post   :: " + r
                if post['data'][0]['caption']:
                    caption = post['data'][0]['caption']['text']
                    print "Caption  :: "+ caption
                else:
                    print "No caption of this post!"
            else:
                print "This User have no posts!"
        else:
            print "Status code other than 200 received!"


#-----------------------------------------------------------------------------------------------------------------------#

#Function defines to download the user's post
def dwnld_user_post(u_name):
    user_id = get_user_id(u_name)
    if user_id is None:
        print "User does not exist!"
        exit()
    else:
        post = requests.get('%susers/%s/media/recent/?access_token=%s' % (BASE_URL, user_id, APP_ACCESS_TOKEN)).json()
        if post['meta']['code'] == 200:
            # To Check post exist or not
            if len(post['data']) > 0:
                if post['data'][0]['type'] == "image":
                    image_name = post['data'][0]['id'] + '.jpeg'
                    image_url = post['data'][0]['images']['standard_resolution']['url']
                    urllib.urlretrieve(image_url, image_name)
                    print "Image downloads successful"
                elif post['data'][0]['type'] == "video":
                    video_name = post['data'][0]['id'] + '.mp4'
                    video_url = post['data'][0]['videos']['standard_resolution']['url']
                    urllib.urlretrieve(video_url, video_name)
                    print "Video downloads successful..."
                else:
                    print "No image  or video post to show..."
            else:
                print "Post does not  exist!"
        else:
            print "Status code other than 200 received!"
#-----------------------------------------------------------------------------------------------------------------------#

#Function defines to get the media id
def media_id(username):
    user_id = get_user_id(username)
    if user_id is None:
        print "User does not exist!"
        exit()
    else:
        post = requests.get('%susers/%s/media/recent/?access_token=%s' % (BASE_URL, user_id, APP_ACCESS_TOKEN)).json()
        if post['meta']['code'] == 200:
            # To check post exist or not
            if len(post['data']) > 0:
                #Returns media id
                return post['data'][0]['id']
            else:
                print "Post does not exist!"
        else:
            print "Status code other than 200 received!"

#-----------------------------------------------------------------------------------------------------------------------#

#Function Defines to Like the user's post
def like_post(user_name):
    umedia_id = media_id(user_name)
    payload = {"access_token": APP_ACCESS_TOKEN}
    url = '%smedia/%s/likes' % (BASE_URL, umedia_id)
    post_a_like = requests.post(url, payload).json()
    if post_a_like['meta']['code'] == 200:
        print "Like was successful!"
    else:
        print "Your like was unsuccessful...Plzzzz try again!"

#-----------------------------------------------------------------------------------------------------------------------#

#Function defines to comment on the user's post
def comment_post(user_name):
    umedia_id = media_id(user_name)
    comment_text = raw_input("Your comment: ")
    payload = {"access_token": APP_ACCESS_TOKEN, "text": comment_text}
    url = '%smedia/%s/comments' % (BASE_URL, umedia_id)
    make_comment = requests.post(url, payload).json()
    if make_comment['meta']['code'] == 200:
        print "Comment Done!"
    else:
        print "Failed to comment. Plzzzz Try again!"


# -----------------------------------------------------------------------------------------------------------------------#

#Function defines to display the list of comments
def comment_list(user_name):
    umedia_id = media_id(user_name)
    request_url = ('%smedia/%s/comments/?access_token=%s' % (BASE_URL, umedia_id, APP_ACCESS_TOKEN))
    comment = requests.get(request_url).json()
    if comment['meta']['code'] == 200:
        if len(comment['data']):
            number_of_comments = 0
            print "The list of comments on the post are   :: \n"
            for index in range(0, len(comment['data'])):
                cmnt_text = comment['data'][index]['text']
                print (cmnt_text)
                number_of_comments = number_of_comments + 1
            print "Number of comments on the post are   :: " + str(number_of_comments)
        else:
            print "No comments found on the post!"
    else:
        print "Status code other than 200 received!"


#-----------------------------------------------------------------------------------------------------------------------#

#Function Defines to delete the negative comments on post
def del_neg_comment(user_name):
    umedia_id = media_id(user_name)
    request_url = ('%smedia/%s/comments/?access_token=%s' % (BASE_URL, umedia_id, APP_ACCESS_TOKEN))
    comment_info = requests.get(request_url).json()
    if comment_info['meta']['code'] == 200:
        if len(comment_info['data']):
            #Loops to check the comment is negative or positive
            for index in range(0, len(comment_info['data'])):
                comment_id = comment_info['data'][index]['id']
                comment_text = comment_info['data'][index]['text']
                blob = TextBlob(comment_text, analyzer=NaiveBayesAnalyzer())
                if ((blob.sentiment.p_neg) > (blob.sentiment.p_pos)):
                    print "Negative comment   :: %s" % (comment_text)
                    r = requests.delete('%smedia/%s/comments/%s?access_token=%s' % (
                        BASE_URL, media_id, comment_id, APP_ACCESS_TOKEN)).json()
                    if r['meta']['code'] == 200:
                        print "Negative Comments deleted successfully !"
                    else:
                        print "Unable to delete comments !"
        else:
            print "No comments on the post!"
    else:
        print "Status code other than 200 received!"


#-----------------------------------------------------------------------------------------------------------------------#

#Function Defines to start the app
def main():
    while True:
        menu_choice=input("Select the choice ::\n 1.Get User's Info. \n 2.Get Recent post of owner \n 3. Get Other User Info\n 4. Get User Recent Post \n 5. Download User's recent post \n 6. Like a Post  \n 7. Comment on a post \n 8. List Of Comments on a Post \n 9. Delete Negative comments \n 0. Exit ")
        if menu_choice==1:

             self_info()
        elif menu_choice==2:
             recent_post()
        elif menu_choice==3:
             user_name=raw_input("Enter the user name ::")
             other_user_info(user_name)
        elif menu_choice==4:
             user_name=raw_input("Enter the user name ::")
             get_user_post(user_name)
        elif menu_choice == 5:
             user_name = raw_input("\nEnter the username  :: ")
             dwnld_user_post(user_name)  # Calling the download_user_post() method to download other user's post
        elif menu_choice==6:
             user_name=raw_input("\n Enter the username  ::")
             like_post(user_name)
        elif menu_choice==7:
             user_name=raw_input("\n Enter the username  ::")
             comment_post(user_name)
        elif menu_choice==8:
             user_name=raw_input("\n Enter the username  ::")
             comment_list(user_name)
        elif menu_choice==0:
             exit()
        else:
            print "Wrong input"

#-----------------------------------------------------------------------------------------------------------------------#
#Function call to run the app
main()