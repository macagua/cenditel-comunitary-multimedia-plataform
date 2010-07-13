"""Definition of the audio content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cenditel.multimedia.interfaces import Iaudio
from cenditel.multimedia.config import PROJECTNAME

audioSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-

))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

audioSchema['title'].storage = atapi.AnnotationStorage()
audioSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(audioSchema, moveDiscussion=False)


class audio(base.ATCTContent):
    """It is a file of audio ti be play in the site"""
    implements(Iaudio)

    meta_type = "audio"
    schema = audioSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(audio, PROJECTNAME)
