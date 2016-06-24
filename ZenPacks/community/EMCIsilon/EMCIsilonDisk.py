from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonDisk(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonDisk'
   
    disk_bay = None
    disk_logical_number = None
    disk_chassis_number = None
    disk_device_name = None
    disk_status = None
    disk_model = None
    disk_serial_number = None
    disk_firmware_version = None
    disk_size_bytes = None

    _properties = ManagedEntity._properties + (
        {'id': 'disk_bay','type': 'string'},
        {'id': 'disk_logical_number','type': 'string'},
        {'id': 'disk_chassis_number','type': 'string'},
        {'id': 'disk_device_name','type': 'string'},
        {'id': 'disk_status','type': 'string'},
        {'id': 'disk_model','type': 'string'},
        {'id': 'disk_serial_number','type': 'string'},
        {'id': 'disk_firmware_version','type': 'string'},
        {'id': 'disk_size_bytes','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_disk', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_disks',
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
        return self.emcisilon_disk()

    def getRRDTemplateName(self):
        return 'EMCIsilonDisks'
