from Products.ZenModel.DeviceComponent import DeviceComponent
from Products.ZenModel.ManagedEntity import ManagedEntity
from Products.ZenModel.ZenossSecurity import ZEN_CHANGE_DEVICE
from Products.ZenRelations.RelSchema import ToManyCont, ToOne


class EMCIsilonQuota(DeviceComponent, ManagedEntity):
    meta_type = portal_type = 'EMCIsilonIsilonQuota'
   
    quota_type = None
    quota_includes_snapshot_usage = None
    quota_path = None
    quota_hard_threshold_defined = None
    quota_hard_threshold = None
    quota_soft_threshold_defined = None
    quota_soft_threshold = None
    quota_advisory_threshold_defined = None
    quota_advisory_threshold = None
    quota_grace_period = None
    quota_usage = None
    quota_usage_with_overhead = None
    quota_inode_usage = None
    quota_includes_overhead = None

    _properties = ManagedEntity._properties + (
        {'id': 'quota_type','type': 'string'},
        {'id': 'quota_includes_snapshot_usage','type': 'string'},
        {'id': 'quota_path','type': 'string'},
        {'id': 'quota_hard_threshold_defined','type': 'string'},
        {'id': 'quota_hard_threshold','type': 'string'},
        {'id': 'quota_soft_threshold_defined','type': 'string'},
        {'id': 'quota_soft_threshold','type': 'string'},
        {'id': 'quota_advisory_threshold_defined','type': 'string'},
        {'id': 'quota_advisory_threshold','type': 'string'},
        {'id': 'quota_grace_period','type': 'string'},
        {'id': 'quota_usage','type': 'string'},
        {'id': 'quota_usage_with_overhead','type': 'string'},
        {'id': 'quota_inode_usage','type': 'string'},
        {'id': 'quota_includes_overhead','type': 'string'},
        )

    _relations = ManagedEntity._relations + (
        ('emcisilon_quota', ToOne(ToManyCont,
            'ZenPacks.community.EMCIsilon.EMCIsilon',
            'emcisilon_quotas',
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
        return self.emcisilon_quota()

    def getRRDTemplateName(self):
        return 'EMCIsilonQuotas'
