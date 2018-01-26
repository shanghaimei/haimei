from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Model(object):
    """自定义model类  封装了常用的model方法"""
    @classmethod
    def get(cls,primary_key):
        return cls.query.get(primary_key)
    def put(self):
        db.session.add(self)
    @classmethod
    def commit(cls):
        db.session.commit()
    @classmethod
    def rollback(cls):
        """回滚"""
        db.session.rollback()

    def save(self):
        try:
            self.put()
            self.commit()
        except Exception:
            self.rollback()
            raise

    def delete(self):
        db.session.delete(self)


    def __json__(self):
        _d = {}
        for k ,v  in vars(self).items():
            if k.startswith('_'):
                continue
            _d[k] = v
        return _d

from flask import json as _json

class JsonEncode(_json.JSONEncoder):
    def default(self,o):
        if isinstance(o,Model):
            return o.__json__()
        return _json.JSONEncoder.default(self,o)


