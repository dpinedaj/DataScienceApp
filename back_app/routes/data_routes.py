from flask_restplus import Api
from api.data_api import define_source_type, define_source, define_upload


def data_routes(api: Api):
    data_source_api = define_source_type(api)
    source_api = define_source(api)
    upload_api = define_upload(api)
    api.add_resource(data_source_api, '/source_type')
    api.add_resource(source_api, '/source')
    api.add_resource(upload_api, '/upload')

