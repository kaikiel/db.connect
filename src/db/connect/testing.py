# -*- coding: utf-8 -*-
from plone.app.contenttypes.testing import PLONE_APP_CONTENTTYPES_FIXTURE
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import db.connect


class DbConnectLayer(PloneSandboxLayer):

    defaultBases = (PLONE_APP_CONTENTTYPES_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load any other ZCML that is required for your tests.
        # The z3c.autoinclude feature is disabled in the Plone fixture base
        # layer.
        self.loadZCML(package=db.connect)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'db.connect:default')


DB_CONNECT_FIXTURE = DbConnectLayer()


DB_CONNECT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(DB_CONNECT_FIXTURE,),
    name='DbConnectLayer:IntegrationTesting'
)


DB_CONNECT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(DB_CONNECT_FIXTURE,),
    name='DbConnectLayer:FunctionalTesting'
)


DB_CONNECT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        DB_CONNECT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='DbConnectLayer:AcceptanceTesting'
)
