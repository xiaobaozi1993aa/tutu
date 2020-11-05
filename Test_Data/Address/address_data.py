path = '/api/address/editAddressNew'

data = [#正常登录
        {"province":"110000","city":"110100","area":"110101","descs":"qq",
        "address":"%E5%8C%97%E4%BA%AC%E5%B8%82+%E5%8C%97%E4%BA%AC%E5%B8%82+%E4%B8%9C%E5%9F%8E%E5%8C%BA+qq",
        "defaultValue":1,"id":"","name":"乌拉","phone":"12345678911",
        "verifyAddress":1},
        #错误名称，大于边界
        {"province": "110000", "city": "110100", "area": "110101", "descs": "qq",
         "address": "%E5%8C%97%E4%BA%AC%E5%B8%82+%E5%8C%97%E4%BA%AC%E5%B8%82+%E4%B8%9C%E5%9F%8E%E5%8C%BA+qq",
         "defaultValue": 1, "id": "", "name": "%E4%B9%8Cswqxwcefwcccc", "phone": "12345678911",
         "verifyAddress": 1},
        #缺少手机号字段
        {"province": "110000", "city": "110100", "area": "110101", "descs": "qq",
         "address": "%E5%8C%97%E4%BA%AC%E5%B8%82+%E5%8C%97%E4%BA%AC%E5%B8%82+%E4%B8%9C%E5%9F%8E%E5%8C%BA+qq",
         "defaultValue": 1, "id": "", "name": "%E4%B9%8C","phone":"",
         "verifyAddress": 1}
        ]
