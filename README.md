## 起源
在论坛入了一个PT小站玩玩，上传刷了1个T了，魔力有点难搞。 所以利用github action 做些奇奇怪怪的事情
## 适用
NuxusPHP 程序的PT站点
## 现在能干啥
1. 每天自动签到 +魔力
2. 每个小时自动对新种 say thanks +魔力
3. 顺带保号了，PT站一般有登录要求，签到顺带就登录了
## 咋用
0. Fork仓库
1. 添加COOKIE ， Settings > Secrets > New secret > COOKIE
2. 修改NuxusPHP/config.py 修改URL='你的要玩的站地址'
3. 修改NuxusPHP/config.ini 修改thanks_id = 1

## COOKIE 这么设置
把对应站点的COOKIE改成对应格式
[![dIhlTK.png](https://s1.ax1x.com/2020/08/28/dIhlTK.png)](https://imgchr.com/i/dIhlTK)

## 然后看Action任务执行情况就行了

![微信截图_20200828152942.png](https://i.loli.net/2020/08/28/FkhS9TzgOCHlPYG.png)

![微信截图_20200828152957.png](https://i.loli.net/2020/08/28/gRt29zNAspMSeHm.png)
