path = '/api/order/submitMergeOrderPayNew'



data = [# 正常情况
        {'device': 'web',
        'redPackageId':'','totalPrice':'209.00','isUseTubi':0,'useTubiCount':0,'tubiPrice':0,
        'favourableId':'','fansId':''},
        # 缺少地址信息
        {'device': 'web','addressId':'',
         'redPackageId': '', 'totalPrice': '209.00', 'isUseTubi': 0, 'useTubiCount': 0, 'tubiPrice': 0,
         'favourableId': '', 'fansId': ''},
        # 缺少订单信息
        {'device': 'web',
         'redPackageId': '', 'totalPrice': '209.00', 'isUseTubi': 0, 'useTubiCount': 0, 'tubiPrice': 0,
         'favourableId': '', 'fansId': ''},
        ]




