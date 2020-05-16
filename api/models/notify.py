# -*- coding:utf-8 -*-

from api.extensions import db
from api.libs import Model
from api.libs.cache.notify import NotifyCache

class Notify(Model):
    __tablename__ = 'notify'
    TYPES = (
        ('1', '通知'),
        ('2', '待办'),
    )
    SOURCES = (
        ('monitor', '监控中心'),
        ('schedule', '任务计划'),
    )
    title = db.Column(db.String(255))
    source = db.Column(db.Integer, db.ForeignKey('notifysource.id'))
    type = db.Column(db.Integer, db.ForeignKey('notifytype.id'))
    content = db.Column(db.String(255), nullable=True)
    unread = db.Column(db.Boolean,default=True)
    link = db.Column(db.Boolean, nullable=True)

    created_at = db.Column(db.String(20), default=human_datetime)

    @classmethod
    def make_notify(cls, source, type, title, content=None, with_quiet=True):
        if not with_quiet or time.time() - NotifyCache.get_by_time() > 3600:
            NotifyCache.set_by_time(time.time())
            self.create(source=source, title=title, type=type, content=content)

    def __str__(self):
        return '<Notify %r>' % self.title

class NotifyType(Model):
    __tablename__ = 'notifytype'

    name = db.Column(db.String(20))

class NotifySource(Model):
    __tablename__ = 'notifysource'

    name = db.Column(db.String(10))
    desc = db.Column(db.String(20))
    