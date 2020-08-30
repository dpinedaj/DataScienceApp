from mongoengine import (
    Document, EmbeddedDocument,
    StringField, IntField, EmbeddedDocumentField,
    EmbeddedDocumentListField, DictField,
    ReferenceField)


class SourceTypes(Document):
    type_id = IntField()
    type_name = StringField()


class Connection(Document):
    connection_name = StringField()
    connection_attributes = DictField()


class Column(EmbeddedDocument):
    column_name = StringField()
    column_type = StringField()


class Schema(Document):
    schema_name = StringField()
    columns = EmbeddedDocumentListField(Column)


class Source(Document):
    source_name = StringField()
    schema = StringField()
    source_type = StringField()
    connection = StringField()