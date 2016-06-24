from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonSnapshot(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonSnapshot'
   
    snapshot_created = None
    snapshot_expires = None
    snapshot_size = None
    snapshot_path = None
    snapshot_alias_for = None
    snapshot_locked = None

    _properties = ManagedEntity._properties + (
        {'id': 'snapshot_created','type': 'string'},
        {'id': 'snapshot_expires','type': 'string'},
        {'id': 'snapshot_size','type': 'string'},
        {'id': 'snapshot_path','type': 'string'},
        {'id': 'snapshot_alias_for','type': 'string'},
        {'id': 'snapshot_locked','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_snapshot', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonSnapshot',
            'emcisilon_snapshots',
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
        return self.emcisilon_snapshot()

    def getRRDTemplateName(self):
        return 'EMCIsilonSnapshots'
