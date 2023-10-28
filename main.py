def something():
    pass

@table
@set_details()
def test_docs():
    """Short description

    PrimaryKey: id
    Historization:
        Type: reuse_historization
        Sid:
        Id: 
    Topic: kmdg

    Changelog:
        GPSAY-3222: created 
        20231017: update

    """
    pass

from inspect import getdoc

print(getdoc(test_docs))