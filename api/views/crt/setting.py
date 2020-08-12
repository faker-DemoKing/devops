# -*- coding:utf-8 -*-
from flask import request

from api.resource import APIView
from api.models.ssl import SSL, SSLSetting

class SSLSettingView(APIView):
    '''
        证书配置视图
    '''
    url_prefix = '/setting'

    def get(self):
        data = []
        for i in SSLSetting.query.all():
            res = i.to_dict()
            if i.ssl_type:
                res['ssl_type_name'] = i.ssl_type.name
                res['ssl_type_value'] = i.ssl_type.value
            data.append(res)
        
        return self.jsonify(data)
    
    def post(self):
        print(request.values)

class AcmeSettingView(APIView):
    url_prefix = '/setting/acme'

    def get(self):
        print(request.values)

    
    def post(self):
        print(request.values)