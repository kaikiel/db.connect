# -*- coding: utf-8 -*-
from db.connect import _
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from zope import schema
from plone.z3cform import layout
from z3c.form import form
from plone.directives import form as Form


class IConnection(Form.Schema):

    dbString = schema.TextLine(
        title=_(u'DataBase connect setting string.'),
        description=_(u'String format referenced to Sqlalchemy'),
        required=False,
    )


class ConnectionControlPanelForm(RegistryEditForm):
    form.extends(RegistryEditForm)
    schema = IConnection

CustomControlPanelView = layout.wrap_form(ConnectionControlPanelForm, ControlPanelFormWrapper)
CustomControlPanelView.label = _(u"Custom Related Setting")