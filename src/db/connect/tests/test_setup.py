# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plone import api
from db.connect.testing import DB_CONNECT_INTEGRATION_TESTING  # noqa

import unittest


class TestSetup(unittest.TestCase):
    """Test that db.connect is properly installed."""

    layer = DB_CONNECT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if db.connect is installed."""
        self.assertTrue(self.installer.isProductInstalled(
            'db.connect'))

    def test_browserlayer(self):
        """Test that IDbConnectLayer is registered."""
        from db.connect.interfaces import (
            IDbConnectLayer)
        from plone.browserlayer import utils
        self.assertIn(IDbConnectLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = DB_CONNECT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['db.connect'])

    def test_product_uninstalled(self):
        """Test if db.connect is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled(
            'db.connect'))

    def test_browserlayer_removed(self):
        """Test that IDbConnectLayer is removed."""
        from db.connect.interfaces import \
            IDbConnectLayer
        from plone.browserlayer import utils
        self.assertNotIn(IDbConnectLayer, utils.registered_layers())
