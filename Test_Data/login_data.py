data = [#正常登录
        {"phone": 13066909086, "pwd": "e10adc3949ba59abbe56e057f20f883e", "areaCode": 86, "loginType": 0},
        #错误账号
        {"phone": 1306690908, "pwd": "e10adc3949ba59abbe56e057f20f883e", "areaCode": 86, "loginType": 0},
        #缺少密码字段
        {"phone": 13066909086, "pwd": "", "areaCode": 86, "loginType": 0},
        #缺少密码参数
        {"phone": 13066909086, "areaCode": 86, "loginType": 0},
        #密码错误
        {"phone": 13066909086, "pwd": "e10adc3949ba59abbe56e057f", "areaCode": 86, "loginType": 0},
        #类型错误
        {"phone": 13066909086, "pwd": "e10adc3949ba59abbe56e057f20f883e", "areaCode": 86, "loginType": 2}]

path = '/api/common/login/loginByPhone'


