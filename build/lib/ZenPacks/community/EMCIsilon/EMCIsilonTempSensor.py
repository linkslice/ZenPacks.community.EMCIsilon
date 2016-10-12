from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonTempSensor(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonTempSensor'
   
    tempsensor_description = None
    tempsensor_value = None

    _properties = ManagedEntity._properties + (
        {'id': 'tempsensor_description','type': 'string'},
        {'id': 'tempsensor_value','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_tempsensor', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_tempsensors',
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
        return self.emcisilon_tempsensor()

    def getRRDTemplateName(self):
        return 'EMCIsilonTempSensors'
