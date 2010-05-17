"""Helpers for working with common Zope publisher operations
"""

from plone.testing import Layer
from plone.testing import zca

class PublisherDirectives(Layer):
    """Enables the use of the ZCML directives from ``zope.app.publisher``
    (most of the ``browser`` namespace, excluding viewlets), and
    ``zope.security`` (the ``permission`` directive).
    
    Extends ``zca.ZCML_DIRECTIVES`` and uses its ``configurationContext``
    resource.
    """
    
    defaultBases = (zca.ZCML_DIRECTIVES,)
    
    def setUp(self):
        from zope.configuration import xmlconfig
        
        # From the zca.ZCML_DIRECTIVES base layer
        context = self['configurationContext']

        import zope.security
        xmlconfig.file('meta.zcml', zope.security, context=context)
        
        # XXX: In Zope 2.13, this has split into zope.publisher,
        # zope.browserresource, zope.browsermenu and zope.browserpage
        import zope.app.publisher
        xmlconfig.file('meta.zcml', zope.app.publisher, context=context)
    
    def tearDown(self):
        # XXX: No proper tear-down
        pass

PUBLISHER_DIRECTIVES = PublisherDirectives()