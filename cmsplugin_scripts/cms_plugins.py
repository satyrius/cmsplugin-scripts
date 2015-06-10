from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool

from .models import ScriptPlugin as Plugin


class ScriptPlugin(CMSPluginBase):
    model = Plugin
    name = 'Custom script'
    render_template = 'cms/plugins/script_injection.html'

plugin_pool.register_plugin(ScriptPlugin)
