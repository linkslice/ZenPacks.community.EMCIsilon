from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonPowerSensor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonPowerSensor'
   
    powersensor_description = None
    powersensor_value = None

    _properties = ManagedEntity._properties + (
        {'id': 'powersensor_description','type': 'string'},
        {'id': 'powersensor_value','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_powersensor', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_powersensors',
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
        return self.emcisilon_powersensor()

    def getRRDTemplateName(self):
        return 'EMCIsilonPowerSensors'
