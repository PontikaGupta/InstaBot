import requests

response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN =  response['access_token']
BASE_URL='https://api.instagram.com/v1/'

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        print "User's Name : " + user_info['data']['username']
        print "User's Bio : " + user_info['data']['bio']
        #print "user Follows : " + user_info['data']['follows']
       # print "User's Followers : " + user_info['data']['follows_by']
        print "Website : " + user_info['data']['website']
        print "User's id : " + user_info['data']['id']
        print "User's Full Name : " + user_info['data']['full_name']
        print "User's Profile Pic : " +  user_info['data']['profile_picture']

    else:
        print 'Status code other than 200 received!'


self_info()