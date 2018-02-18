import requests

response = requests.get('https://api.jsonbin.io/b/59d0f30408be13271f7df29c').json()
APP_ACCESS_TOKEN = 'f3879afc4df64c588581bcda0f1ddec0'
BASE_URL='https://api.instagram.com/v1/'

def self_info():
    request_url = (BASE_URL + 'users/self/?access_token=%s') % (APP_ACCESS_TOKEN)
    print 'GET request url : %s' % (request_url)
    user_info = requests.get(request_url).json()

    if user_info['meta']['code'] == 200:
        print user_info['data']['id']
        print user_info['data']['profile_picture']
        print user_info['data']['username']
        print user_info['data']['bio']
        print user_info['data']['fullname']
        print user_info['data']['follows']
        print user_info['data']['follows_by']
        print user_info['data']['website']
    else:
        print 'Status code other than 200 received!'


self_info()