from Products.ZenModel.ZenPack import ZenPackBase

productNames = (
    'EMCIsilonDevice',
    'EMCIsilonPowerSensor',
    'EMCIsilonTempSensor',
    'EMCIsilonFan',
    'EMCIsilonDisk',
    'EMCIsilonChassis',
    'EMCIsilonDiskPerf',
    'EMCIsilonNodeProtocolPerf',
    'EMCIsilonSnapshot',
    'EMCIsilonSnapshotSchedule',
    'EMCIsilonQuota',
    'EMCIsilonLicense',
)

class ZenPack(ZenPackBase):
    "ZenPack Loader that loads zProperties for EMC Isilon ZP."
    packZProperties = [
           # skip these protocol when modeling
           ('zEMCIsilonProtocolsIgnore', '', 'lines'),
                               
        ]  

