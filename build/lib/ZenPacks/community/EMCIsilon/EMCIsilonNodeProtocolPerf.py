from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonNodeProtocolPerf(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonNodeProtocolPerf'
   
    protocol_op_count = None
    protocol_ops_per_second = None
    protocol_in_min_bytes = None
    protocol_in_max_bytes = None
    protocol_in_avg_bytes = None
    protocol_in_stddev_bytes = None
    protocol_in_bps = None
    protocol_out_min_bytes = None
    protocol_out_max_bytes = None
    protocol_out_avg_bytes = None
    protocol_out_stddev_bytes = None
    protocol_out_bps = None
    protocol_latency_min = None
    protocol_latency_max = None
    protocol_latency_avg = None
    protocol_latency_stddev = None

    _properties = ManagedEntity._properties + (
        {'id': 'protocol_op_count','type': 'string'},
        {'id': 'protocol_ops_per_second','type': 'string'},
        {'id': 'protocol_in_min_bytes','type': 'string'},
        {'id': 'protocol_in_max_bytes','type': 'string'},
        {'id': 'protocol_in_avg_bytes','type': 'string'},
        {'id': 'protocol_in_stddev_bytes','type': 'string'},
        {'id': 'protocol_in_bps','type': 'string'},
        {'id': 'protocol_out_min_bytes','type': 'string'},
        {'id': 'protocol_out_max_bytes','type': 'string'},
        {'id': 'protocol_out_avg_bytes','type': 'string'},
        {'id': 'protocol_out_stddev_bytes','type': 'string'},
        {'id': 'protocol_out_bps','type': 'string'},
        {'id': 'protocol_latency_min','type': 'string'},
        {'id': 'protocol_latency_max','type': 'string'},
        {'id': 'protocol_latency_avg','type': 'string'},
        {'id': 'protocol_latency_stddev','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_nodeprotocolperf', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilonDevice',
            'emcisilon_nodeprotocolperfs',
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
        return self.emcisilon_nodeprotocolperf()

    def getRRDTemplateName(self):
        return 'EMCIsilonNodeProtocolPerfs'
