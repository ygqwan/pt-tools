#!/usr/bin/python
# -*- coding: UTF-8 -*-


import re
import configparser

# 完整url
from NexusPHP.config import generateConfig
from NexusPHP.utility.function import now


def sayThanks(session,url):

    thanksUrl = url + '/thanks.php'
    # 取上次保存的感谢id
    config = configparser.RawConfigParser()
    config.read('config.ini')
    # str 转成 int

    thanks_id = url.split('//')[1]
    try:
        i = int(config.get('thanks_id', thanks_id))
    except:
        i =1

    invalid_time = 0
    print(now(), '网站：%s  开始对种子说感谢' % (url),i)
    for id in range(i, i+500):

        with session.post(thanksUrl, data={'id': id}) as res:

            if not res.text:
                invalid_time = 0
                tips = '感谢成功，魔力 +1'
            else:
                r = re.compile(r'<tr><td class="text">(.+?)</td></tr>')
                tips = r.search(res.text).group(1)
                if tips == 'Invalid torrent id!':
                    invalid_time += 1
                    if invalid_time > 2:
                        print(now(), '种子连续不存在，任务终止')
                        id =id - 2
                        break
                else:
                    invalid_time = 0

            print(now(), '种子id:', id, tips)

    # 种子id 保存到配置文件
    config['thanks_id'][thanks_id] = '%s' % (id)
    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def main():
    [sayThanks(config['session'], config['url']) for config in generateConfig() if 'say_thanks' in config['tasks']]

if __name__ == '__main__':
    main()