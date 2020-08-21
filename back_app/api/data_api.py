from flask_restplus import Resource, fields
from flask import jsonify, request
from werkzeug.datastructures import FileStorage
from models.data import (SourceTypes, Connection,
                         Column, Schema, Source)


def define_source_type(api):
    parser = api.parser()
    parser.add_argument('type_id', type=int, help='Type Id', location='form')
    parser.add_argument('type_name', type=str,
                        help='Type Name', location='form')

    class SourceTypesApi(Resource):

        @api.doc(parser=parser)
        def post(self):
            data = x if (x := request.get_json()) is not None \
                else parser.parse_args()

            st = SourceTypes(**data).save()
            return jsonify({"id": str(st.id),
                            "type_id": str(st.type_id),
                            "type_name": str(st.type_name)})

    return SourceTypesApi

def define_schema(api):
    pass

def define_connectoin(api):
    pass


def define_source(api):

    parser = api.parser()
    parser.add_argument('type', type=int, help='Type Name', location='form',
                        choices=[obj.type_name for obj in SourceTypes.objects().all()])
    parser.add_argument('')

    class SourceApi(Resource):
        @api.doc(parser=parser)
        def post(self):
            pass

    return SourceApi


def define_upload(api):
    parser = api.parser()
    parser.add_argument('name', type=str, location='form', required=True)
    parser.add_argument('file', location='files',
                        type=FileStorage, required=True)

    @api.expect(parser)
    class UploadApi(Resource):
        def post(self):
            uploaded_file = args['file']
            # TODO WRITE FILE
            return jsonify({"result": "OK"})

    return UploadApi
