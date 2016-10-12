from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonSnapshotSchedule(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonSnapshotSchedule'
   
    snapshot_schedule_alias = None
    snapshot_schedule_naming_pattern = None
    snapshot_schedule_schedule = None
    snapshot_schedule_path = None

    _properties = ManagedEntity._properties + (
        {'id': 'snapshot_schedule_alias','type': 'string'},
        {'id': 'snapshot_schedule_naming_pattern','type': 'string'},
        {'id': 'snapshot_schedule_schedule','type': 'string'},
        {'id': 'snapshot_schedule_expiration','type': 'string'},
        {'id': 'snapshot_schedule_path','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_snapshotschedule', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_snapshotschedules',
            )),
        )

    factory_type_information = ({
        'actions': ({
            'id': 'perfConf',
            'name': 'Template',
            'action': 'objTemplates',
            'permissions': (ZEN_CHANGE_DEVICE,),
            },),
        },)

    def device(self):
        return self.emcisilon_snapshotschedule()

    def getRRDTemplateName(self):
        return 'EMCIsilonSnapshotSchedules'
