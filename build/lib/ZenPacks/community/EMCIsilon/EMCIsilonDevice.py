from Products.ZenRelations.RelSchema import ToManyCont, ToOne
from Products.ZenModel.Device import Device



class EMCIsilonDevice(Device):
    _relations = Device._relations + (
        ('emcisilon_chassises', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonChassis',
            'emcisilon_chassis'
            )),
        ('emcisilon_disks', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonDisk',
            'emcisilon_disk'
            )),
        ('emcisilon_diskperfs', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonDiskPerf',
            'emcisilon_diskperf'
            )),
        ('emcisilon_fans', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonFan',
            'emcisilon_fan'
            )),
        ('emcisilon_nodeprotocolperfs', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonNodeProtocolPerf',
            'emcisilon_nodeprotocolperf'
            )),
        ('emcisilon_powersensors', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonPowerSensor',
            'emcisilon_powersensor'
            )),
        ('emcisilon_quotas', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonQuota',
            'emcisilon_quota'
            )),
        ('emcisilon_snapshots', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonSnapshot',
            'emcisilon_snapshot'
            )),
        ('emcisilon_snapshotschedules', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonSnapshotSchedule',
            'emcisilon_snapshotschedule'
            )),
        ('emcisilon_tempsensors', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonTempSensor',
            'emcisilon_tempsensor'
            )),
        ('emcisilon_licenses', ToManyCont(ToOne,
            'ZenPacks.community.EMCIsilon.EMCIsilonLicense',
            'emcisilon_license'
            )),

        )
