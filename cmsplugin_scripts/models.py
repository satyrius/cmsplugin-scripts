from cms.models import CMSPlugin
from django.db import models


class ScriptPlugin(CMSPlugin):
    name = models.CharField(max_length=50)
    snippet = models.TextField()

    def __unicode__(self):
        return unicode(self.name)
