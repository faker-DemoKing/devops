# -*- coding:utf-8 -*-

from flask import request
from flask import session
from flask_login import current_user
from api.resource import APIView

class GetUserInfoView(APIView):
    url_prefix = "/users/info"

    def get(self):
        print(session.get("CAS_USERNAME"),current_user.nickname,'usersinfo name')
        print(session.get("acl", {}).get("parentRoles", []),'permissions=1')
        name = session.get("CAS_USERNAME") or current_user.nickname
        role = dict(permissions=session.get("acl", {}).get("parentRoles", []),session.get("acl", {}).get("rid", []))
        avatar = current_user.avatar
        return self.jsonify(result=dict(name=name,
                                        role=role,
                                        avatar=avatar))