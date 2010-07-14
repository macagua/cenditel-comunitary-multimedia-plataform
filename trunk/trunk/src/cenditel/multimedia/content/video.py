"""Definition of the video content type
"""

from zope.interface import implements

from Products.Archetypes import atapi
from Products.ATContentTypes.content import base
from Products.ATContentTypes.content import schemata

# -*- Message Factory Imported Here -*-

from cenditel.multimedia.interfaces import Ivideo
from cenditel.multimedia.config import PROJECTNAME

videoSchema = schemata.ATContentTypeSchema.copy() + atapi.Schema((

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
   atapi.FileField("video",
                required=True,
                searchable=False,
                #storage=FieldSystemStorage(),
                storage=AnnotationStorage(),
                widget=atapi.FileWidget(label=_(u"audio"))
                ),
))

# Set storage on fields copied from ATContentTypeSchema, making sure
# they work well with the python bridge properties.

videoSchema['title'].storage = atapi.AnnotationStorage()
videoSchema['description'].storage = atapi.AnnotationStorage()

schemata.finalizeATCTSchema(videoSchema, moveDiscussion=False)


class video(base.ATCTContent):
    """It is a Video File to be show in the site"""
    implements(Ivideo)

    meta_type = "video"
    schema = videoSchema

    title = atapi.ATFieldProperty('title')
    description = atapi.ATFieldProperty('description')

    # -*- Your ATSchema to Python Property Bridges Here ... -*-

atapi.registerType(video, PROJECTNAME)
