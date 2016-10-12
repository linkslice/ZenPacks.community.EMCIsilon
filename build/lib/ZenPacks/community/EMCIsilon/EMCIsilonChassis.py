from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonChassis(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonChassis'
   
    chassis_config_number = None
    chassis_serial_number = None
    chassis_model = None
    chassis_unit_idle_on = None

    _properties = ManagedEntity._properties + (
        {'id': 'chassis_config_number','type': 'string'},
        {'id': 'chassis_serial_number','type': 'string'},
        {'id': 'chassis_model','type': 'string'},
        {'id': 'chassis_unit_idle_on','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_chassis', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_chassises',
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
        return self.emcisilon_chassis()

    def getRRDTemplateName(self):
        return 'EMCIsilonChassises'
