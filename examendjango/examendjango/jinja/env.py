# -*- coding: utf-8 -*-
from jinja2.environment import Environment
from django.utils.translation import get_language, gettext as _


class JinjaEnvironment(Environment):
    def __init__(self, **kwargs):
        super(JinjaEnvironment, self).__init__(**kwargs)
        self.globals['get_language'] = get_language
        self.globals['_'] = _
