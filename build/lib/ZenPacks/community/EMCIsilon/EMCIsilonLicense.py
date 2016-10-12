from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonLicense(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonLicense'
   
    license_status = None
    license_entry = None

    _properties = ManagedEntity._properties + (
        {'id': 'license_status','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_license', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_licenses',
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
        return self.emcisilon_license()

    def getRRDTemplateName(self):
        return 'EMCIsilonLicenses'
