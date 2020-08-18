from mongoengine import (
    Document, EmbeddedDocument,
    StringField, IntField, EmbeddedDocumentField,
    EmbeddedDocumentListField, DictField,
    ReferenceField)


class SourceTypes(Document):
    type_id = IntField()
    type_name = StringField()


class Connection(EmbeddedDocument):
    connection_name = StringField()
    connection_attributes = DictField()


class Column(EmbeddedDocument):
    column_name = StringField()
    column_type = StringField()


class Schema(EmbeddedDocument):
    schema_name = StringField()
    columns = EmbeddedDocumentListField(Column)


class Source(Document):
    source_name = StringField()
    schema = EmbeddedDocumentField(Schema)
    source_type = ReferenceField(SourceTypes)
    connection = EmbeddedDocumentField(Connection)