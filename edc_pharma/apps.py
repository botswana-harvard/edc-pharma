import os

from django.apps import AppConfig as DjangoAppConfig
from django.conf import settings

from edc_base.apps import AppConfig as EdcBaseAppConfigParent
from edc_label.apps import AppConfig as EdcLabelAppConfigParent


class AppConfig(DjangoAppConfig):
    name = 'edc_pharma'
    # get this from the user profile
    user_initials = {
        'omasala': 'OTDL',
        'opule': 'ODP',
        'tfrank': 'TTF',
        'mrabantetse': 'MR'}


class EdcBaseAppConfig(EdcBaseAppConfigParent):
    project_name = 'Edc Pharmacy'
    institution = 'Botswana-Harvard AIDS Institute'


class EdcLabelAppConfig(EdcLabelAppConfigParent):
    default_cups_server_ip = None
    default_printer_label = 'mytest'
    extra_templates_folder = os.path.join(settings.STATIC_ROOT, 'edc_pharma', 'label_templates')
