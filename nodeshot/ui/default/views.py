from django.shortcuts import render
from django.conf import settings
from nodeshot.core.layers.models import Layer
from . import settings as ui_settings

if 'nodeshot.core.websockets' in settings.INSTALLED_APPS:
    from nodeshot.core.websockets import DOMAIN, PATH, PORT

    WEBSOCKETS = {
        'DOMAIN': DOMAIN,
        'PATH': PATH,
        'PORT': PORT
    }
else:
    WEBSOCKETS = False


# TODO
# improve spaghetti code
def index(request):
    layers = Layer.objects.published()
    layers_allowing_new_nodes = layers.filter(new_nodes_allowed=True)

    context = {
        'layers': layers,
        'layers_allowing_new_nodes': layers_allowing_new_nodes,
        'WEBSOCKETS': WEBSOCKETS,
        'TILESERVER_URL': ui_settings.TILESERVER_URL,
        'MAP_CENTER': ui_settings.MAP_CENTER,
        'MAP_ZOOM': ui_settings.MAP_ZOOM,
        'VOTING_ENABLED': ui_settings.VOTING_ENABLED,
        'RATING_ENABLED': ui_settings.RATING_ENABLED,
        'COMMENTS_ENABLED': ui_settings.COMMENTS_ENABLED
    }
    return render(request, 'index.html', context)
