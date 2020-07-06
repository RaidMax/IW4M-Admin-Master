from master import api
from master.resources.events.client import Client

from master.resources.health import Health
from master.resources.instance import Instance
from master.resources.authenticate import Authenticate
from master.resources.version import Version
from master.resources.history_graph import HistoryGraph
from master.resources.localization import Localization

from master.resources.events.penalty import Penalty

api.add_resource(Health, '/health')
api.add_resource(Instance, '/instance/', '/instance/<string:id>')
api.add_resource(Version, '/version', '/version/<int:api_version>')
api.add_resource(Authenticate, '/authenticate')
api.add_resource(HistoryGraph, '/history/', '/history/<int:history_count>')
api.add_resource(Localization, '/localization/', '/localization/<string:language_tag>')

# events
api.add_resource(Client, '/event/client/<string:event_type>')
api.add_resource(Penalty, '/event/client/<string:network_id>/penalty')
