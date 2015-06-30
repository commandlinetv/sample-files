from coffin.common import CoffinEnvironment
from django.conf import settings
from django.template.loader import BaseLoader
from django.template import TemplateDoesNotExist
from django.utils import translation
from jinja2.exceptions import TemplateNotFound

class TemplateEnvironment(CoffinEnvironment):

    def set_language(self, language_code):
        """hooks up translation objects from django to jinja2 environment.
        note: not so sure about thread safety here
        """
        trans = translation.trans_real.translation(language_code)
        self.install_gettext_translations(trans)

ENV = TemplateEnvironment(extensions=['jinja2.ext.i18n',])
ENV.set_language(settings.LANGUAGE_CODE)

class Jinja2Loader(BaseLoader):
    """skins template loader for Django > 1.2
    todo: verify that this actually follows django's convention correctly
    """
    is_usable = True
    def load_template(self, template_name, template_dirs = None):
        try:
            return ENV.get_template(template_name), template_name
        except TemplateNotFound:
            raise TemplateDoesNotExist
