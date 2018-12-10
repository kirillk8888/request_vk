import requests
import json
import re
from datetime import datetime
import time
from collections import Counter


def calc_age(uid):
    url = 'https://api.vk.com/method/users.get'
    query = {'user_ids': uid,
            'fields':'bdate',
            'access_token' : '17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
            'v': '5.71'}
    response = requests.get(url, params = query).text
    data = json.loads(response)
    tmp = data['response']
    ID = (tmp[0])['id']
    

    url = 'https://api.vk.com/method/friends.get'
    query = {'user_id': ID,
            'fields':'bdate',
            'access_token':'17da724517da724517da72458517b8abce117da17da72454d235c274f1a2be5f45ee711',
            'v': '5.71'}
    response = requests.get(url, params = query).text
    data = json.loads(response)
   
    arr = []
    for i in data['response']['items']:
        arr.append(i.get('bdate', ''))

    new = [item for item in arr if re.search(r'[0-9]{1,2}[.][0-9]{1,2}[.][0-9]{2,4}', item)]

    arr2 = []
    for i in new:
        d = datetime.strptime(i, '%d.%m.%Y')
        arr2.append((str(d.strftime('%Y'))))

    result = [int(item) for item in arr2]
    result2 = []
    for elem in result:
        elem = 2018 - elem
        result2.append(elem)

    c = Counter(result2).most_common()   
    result = sorted(c, key=lambda point: (-point[1], point[0]))
    return result

if __name__ == '__main__':
    res = calc_age('reigning')
    print(res)
    