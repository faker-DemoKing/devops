from flask import request

from flask import g
from api.models import Host
from api.extensions import celery
from api.libs.ssh import SSH
from api.resource import APIView

@celery.task(name="ssl.acme.install", queue="acme_install")
def acme_install_task(host_ids):
    hosts = Host.get_by_in_id(host_ids)
    private_key = AppSetting.get('private_key')
    cli = SSH(hostname, port, username, private_key)
    code, out = cli.exec_command('echo 1>>/opt/a')

class AcmeInstall(APIView):
    url_prefix = ('/acme/install','/acme/status')
    
    def get(self):
        if request.values.get('id'):
            print(request.values)
    
    def post(self):
        
        acme_install_task.apply_async(request.values.get('host_ids'))

        return self.jsonify(error="")

