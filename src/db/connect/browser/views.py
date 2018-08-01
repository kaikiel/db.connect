# -*- coding: utf-8 -*-
from db.connect import _
from Products.Five.browser import BrowserView
from plone import api
from sqlalchemy import create_engine
from db.connect.browser.configlet import IConnection
import sys 
reload(sys)
sys.setdefaultencoding('utf-8')


class SqlObj():
    def execSql(self, execStr):
        dbString = api.portal.get_registry_record('dbString', interface=IConnection)
        engine = create_engine(dbString, echo=True)

        conn = engine.connect() # DB連線
        execResult = conn.execute(execStr)
        conn.close()
        if execResult.returns_rows:
            return execResult.fetchall()
