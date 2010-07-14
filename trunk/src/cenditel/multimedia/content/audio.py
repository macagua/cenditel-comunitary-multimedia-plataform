"""Definition of the audio content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cenditel.multimedia.interfaces import Iaudio
from cenditel.multimedia.config import PROJECTNAME
# -*- Import of FileSystem Storage-*-
#from iw.fss.FileSystemStorage import FileSystemStorage

audioSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

    # -*- Your Archetypes field definitions here ... -*-
   atapi.StringField("title",
                required=True,
                searchable=True,
                storage=atapi.AnnotationStorage(),
                widget=atapi.StringWidget(label=_(u"title"))
                ),
   atapi.TextField("description",
                required=False,
                searchable=True,
                storage=atapi.AnnotationStorage(),
                widget=atapi.RichWidget(label=_(u"description"))
                ),
   atapi.FileField("audio",
                required=True,
                searchable=False,
                #storage=FieldSystemStorage(),
                storage=AnnotationStorage(),
                widget=atapi.FileWidget(label=_(u"audio"))
                ),
    
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

audioSchema['title'].storage = atapi.AnnotationStorage()
audioSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(audioSchema, moveDiscussion=False)


class audio(base.ATCTContent):
    """It is a file of audio to be play in the site"""
    implements(Iaudio)

    meta_type = "audio"
    schema = audioSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(audio, PROJECTNAME)
