from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonDiskPerf(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonDiskPerf'
   
    disk_perf_ops_per_second = None
    disk_perf_in_bits_per_second = None
    disk_perf_out_bits_per_second = None

    _properties = ManagedEntity._properties + (
        {'id': 'disk_perf_ops_per_second','type': 'string'},
        {'id': 'disk_perf_in_bits_per_second','type': 'string'},
        {'id': 'disk_perf_out_bits_per_second','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_diskperf', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_diskperfs',
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
        return self.emcisilon_diskperf()

    def getRRDTemplateName(self):
        return 'EMCIsilonDiskPerfs'
