import mongoengine as db

class BRCAData(db.Document):
    id = db.DynamicField(primary_key=True)
    yearstobirth = db.DynamicField()
    vitalstatus = db.DynamicField()
    daystodeath = db.DynamicField()
    daystolastfollowup = db.DynamicField()
    tumortissuesite = db.DynamicField()
    pathologicstage = db.DynamicField()
    pathologyTstage = db.DynamicField()
    pathologyNstage = db.DynamicField()
    pathologyMstage = db.DynamicField()
    gender = db.DynamicField()
    dateofinitialpathologicdiagnosis = db.DynamicField()
    daystolastknownalive = db.DynamicField()
    radiationtherapy = db.DynamicField()
    histologicaltype = db.DynamicField()
    numberoflymphnodes = db.DynamicField()
    race = db.DynamicField()
    ethnicity = db.DynamicField()
