# -*- coding: utf-8 -*-
import requests,json

class MemberService():

    @staticmethod
    def getWeChatOpenId( code ):
        AppID = "wxfe8ac0a3eedb63b7",
        AppSecret = "a438e6d2393e7c996e8b70fa34c89d68"
        url = "https://api.weixin.qq.com/sns/jscode2session?appid={0}&secret={1}&js_code={2}&grant_type=authorization_code" \
            .format(AppID, AppSecret, code)
        r = requests.get(url)
        res = json.loads(r.text)
        openid = None
        if 'openid' in res:
            openid = res['openid']
        return openid
