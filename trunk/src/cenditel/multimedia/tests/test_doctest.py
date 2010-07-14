import unittest
import doctest

#from zope.testing import doctestunit
#from zope.component import testing, eventtesting

from Testing import ZopeTestCase as ztc

from cenditel.multimedia.tests import base

from base import MultimediaFunctionalTestCase
from cenditel.multimedia.interfaces import Ivideo,Iaudio 


class TestProductInstall(MultimediaFunctionalTestCase):

    def afterSetUp(self):
        self.types = ('video','audio')

    def testTypesInstalled(self):
            for t in self.types:
                self.failUnless(t in self.portal.portal_types.objectIds(),
                            '%s content type not installed' % t)

def testPortalFactoryEnabled(self):
            for t in self.types:
                self.failUnless(t in self.portal.portal_factory.getFactoryTypes().keys(),
                                '%s content type not installed' % t)

class TestInstantiation(MultimediaFunctionalTestCase):
    
    #Defining test for ContentType video
    
    def afterSetUpVideo(self):
        # Adding an InstantMessage anywhere - can only be done by a Manager or Portal Owner
        self.setRoles(['Manager'])
        self.portal.invokeFactory('video', 'v1')

    def testCreateVideo(self):
        self.failUnless('v1' in self.portal.objectIds())


    def testVideoInterface(self):
        v = self.portal.v1
        self.failUnless(Ivideo.providedBy(v))
                       
  
  #Defining test for ContentType Audio
  
    def afterSetupAudio(self):
        self.setRoles(['Manager'])
        self.portal.invokeFactory('audio','a1')
            
    def testCreateAudio(self):
        self.failUnless('a1' in self.portal.objectIds())
        
    def testAudioInterface(self):
        a=self.portal.a1
        self.failUnless(Iaudio.provideBy(a))    

"""     
def test_suite():
    from unittest import TestSuite, makeSuite
    suite = TestSuite()
    suite.addTest(makeSuite(TestProductInstall))
    suite.addTest(makeSuite(TestInstantiation))
    return suite
"""

def test_suite():
    return unittest.TestSuite([

        # Demonstrate the main content types
       ztc.ZopeDocFileSuite(
            'tests/doctets/text_doctest.txt', package='cenditel.multimedia',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        
        ztc.ZopeDocFileSuite(
            'tests/doctest/video.txt', package='cenditel.multimedia',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),
        ztc.ZopeDocFileSuite(
            'tests/doctest/audio.txt', package='cenditel.multimedia',
            test_class=base.FunctionalTestCase,
            optionflags=doctest.REPORT_ONLY_FIRST_FAILURE |
                doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS),  

        ])

if __name__ == '__main__':
    unittest.main(defaultTest='test_suite')
