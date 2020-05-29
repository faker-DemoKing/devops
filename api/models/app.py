# -*- coding:utf-8 -*-
import json

from api.extensions import db
from api.libs import Model
from api.libs import human_datetime

class App(Model):
    __tablename__ = 'apps'

    name = db.Column(db.String(50))
    key = db.Column(db.String(50), unique=True)
    desc = db.Column(db.String(255), nullable=True)
    rel_apps = db.Column(db.Text, nullable=True)
    create_at = db.Column(db.String(20), default=human_datetime)
    create_by = db.Column(db.Integer, db.ForeignKey('users.id'))

    def to_dict(self, *args, **kwargs):
        tmp = super().to_dict(*args, **kwargs)
        tmp['rel_apps'] = json.loads(self.rel_apps) if self.rel_apps else []
        tmp['rel_services'] = json.loads(self.rel_services) if self.rel_services else []
        return tmp


    def __str__(self):
        return '<App %r>' % self.name

class DeployExtends(Model):
    __tablename__ = 'deploy_extends'

    name = db.Column(db.String(50))

class Deploy(Model):
    __tablename__ = 'deploys'

    app = db.Column(db.Integer, db.ForeignKey('apps.id'))
    env = db.Column(db.Integer, db.ForeignKey('environments.id'))
    host_ids = db.Column(db.Text)
    extend = db.Column(db.Integer, db.ForeignKey('deploy_extends.id'))

    def __str__(self):
        return '<Deoploy %r>' % self.app

class DeployExtend1(Model):
    __tablename__ = 'deploy_extend1'

    deploy = db.Column(db.Integer, db.ForeignKey('deploys.id'))
    git_repo = db.Column(db.String(255))
    dst_dir = db.Column(db.String(255))
    dst_repo = db.Column(db.String(255))
    versions = db.Column(db.Integer)
    filter_rule = db.Column(db.Text)
    custom_envs = db.Column(db.Text)
    hook_pre_server = db.Column(db.Text, nullable=True)
    hook_post_server = db.Column(db.Text, nullable=True)
    hook_pre_host = db.Column(db.Text, nullable=True)
    hook_post_host = db.Column(db.Text, nullable=True)

    def to_dict(self, *args, **kwargs):
        tmp = super().to_dict(*args, **kwargs)
        tmp['filter_rule'] = json.loads(self.filter_rule)
        tmp['custom_envs'] = '\n'.join(f'{k}={v}' for k, v in json.loads(self.custom_envs).items())

        return tmp
    
    def __str__(self):
        return '<DeployExtend1 deploy_id=%r>' % self.deploy

class DeployExtend2(Model):
    __tablename__ = 'deploy_extend2'

    deploy = db.Column(db.Integer, db.ForeignKey('deploys.id'))
    server_actions = db.Column(db.Text)
    host_actions = db.Column(db.Text)

    def to_dict(self, *args, **kwargs):
        tmp = super().to_dict(*args, **kwargs)
        tmp['server_actions'] = json.loads(self.server_actions)
        tmp['host_actions'] = json.loads(self.host_actions)

        return tmp
    
    def __str__(self):
        return '<DeployExtend deploy_id=%r>' % self.deploy