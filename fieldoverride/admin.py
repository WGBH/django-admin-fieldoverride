from django.contrib import admin
from django.contrib.contenttypes.admin import GenericStackedInline
from .models import FieldOverride

import logging
django_log = logging.getLogger('django')

class FieldOverrideStackedInline(GenericStackedInline):
    model = FieldOverride
    extra = 0
    
    #django_log.info('TEST: {}'.format(model.content_type.model_class().map_override_fields()))
    # How do I get to?
    # model.content_type.model_class().map_override_fields()