from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonFan(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonFan'
   
    fan_description = None
    fan_speed = None

    _properties = ManagedEntity._properties + (
        {'id': 'fan_description','type': 'string'},
        {'id': 'fan_speed','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_fan', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_fans',
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
        return self.emcisilon_fan()

    def getRRDTemplateName(self):
        return 'EMCIsilonFans'
