from Products.Zuul.form import schema
from Products.Zuul.interfaces.device import IDeviceInfo
from Products.Zuul.interfaces.component import IComponentInfo
from Products.Zuul.utils import ZuulMessageFactory as _t


class IEMCIsilonPowerSensorInfo(IComponentInfo):
    powersensor_description = schema.TextLine(title=_t('Description'))
    powersensor_value = schema.TextLine(title=_t('Value'))
    
class IEMCIsilonTempSensorInfo(IComponentInfo):
    tempsensor_description = schema.TextLine(title=_t('Description'))
    tempsensor_value = schema.TextLine(title=_t('Value'))

class IEMCIsilonFanInfo(IComponentInfo):
    fan_description = schema.TextLine(title=_t('Description'))
    fan_speed = schema.TextLine(title=_t('Value'))

class IEMCIsilonDiskInfo(IComponentInfo):
    disk_bay = schema.TextLine(title=_t('Bay'))
    disk_logical_number = schema.TextLine(title=_t('Logical Number'))
    disk_chassis_number = schema.TextLine(title=_t('Chassis'))
    disk_status = schema.TextLine(title=_t('Status'))
    disk_model = schema.TextLine(title=_t('Model'))
    disk_serial_number = schema.TextLine(title=_t('Serial Number'))
    disk_firmware_version = schema.TextLine(title=_t('Firmware Version'))
    disk_size_bytes = schema.TextLine(title=_t('Size'))
    
class IEMCIsilonChassisInfo(IComponentInfo):
    chassis_config_number = schema.TextLine(title=_t('Config Number'))
    chassis_serial_number = schema.TextLine(title=_t('Serial Numver'))
    chassis_model = schema.TextLine(title=_t('Model'))
    chassis_unit_idle_on = schema.TextLine(title=_t('Idle On?'))
    
class IEMCIsilonDiskPerfInfo(IComponentInfo):
    disk_perf_ops_per_second = schema.TextLine(title=_t('Ops/s'))
    disk_perf_in_bits_per_second = schema.TextLine(title=_t('In Bps'))
    disk_perf_out_bits_per_second = schema.TextLine(title=_t('Out Bps'))
    
class IEMCIsilonNodeProtocolPerfInfo(IComponentInfo):
    protocol_op_count = schema.TextLine(title=_t('Op Count'))
    protocol_ops_per_second = schema.TextLine(title=_t('Ops/s'))
    protocol_in_min_bytes = schema.TextLine(title=_t('In Min Bytes'))
    protocol_in_max_bytes = schema.TextLine(title=_t('In Max Bytes'))
    protocol_in_avg_bytes = schema.TextLine(title=_t('In Avg Bytes'))
    protocol_in_stddev_bytes = schema.TextLine(title=_t('In Stddev Bytes'))
    protocol_in_bps = schema.TextLine(title=_t('In Bps'))
    protocol_out_min_bytes = schema.TextLine(title=_t('Out Min Bytes'))
    protocol_out_max_bytes = schema.TextLine(title=_t('Out Max Bytes'))
    protocol_out_avg_bytes = schema.TextLine(title=_t('Out Avg Bytes'))
    protocol_out_stddev_bytes = schema.TextLine(title=_t('Out Stddev Bytes'))
    protocol_out_bps = schema.TextLine(title=_t('Out Bps'))
    protocol_latency_min = schema.TextLine(title=_t('Latency Min'))
    protocol_latency_max = schema.TextLine(title=_t('Latency Max'))
    protocol_latency_avg = schema.TextLine(title=_t('Latency Avg'))
    protocol_latency_stddev = schema.TextLine(title=_t('Latency Stddev'))
    
class IEMCIsilonSnapshotInfo(IComponentInfo):
    snapshot_created = schema.TextLine(title=_t('Created'))
    snapshot_expires = schema.TextLine(title=_t('Expires'))
    snapshot_size = schema.TextLine(title=_t('Size'))
    snapshot_path = schema.TextLine(title=_t('Path'))
    snapshot_alias_for = schema.TextLine(title=_t('Alias For'))
    snapshot_locked = schema.TextLine(title=_t('Locked?'))
    
class IEMCIsilonSnapshotScheduleInfo(IComponentInfo):
    snapshot_schedule_alias = schema.TextLine(title=_t('Alias'))
    snapshot_schedule_naming_pattern = schema.TextLine(title=_t('Naming Pattern'))
    snapshot_schedule_schedule = schema.TextLine(title=_t('Schedule'))
    snapshot_schedule_expiration = schema.TextLine(title=_t('Expiration'))
    snapshot_schedule_path = schema.TextLine(title=_t('Schedule Path'))
    
class IEMCIsilonQuotaInfo(IComponentInfo):
    quota_type = schema.TextLine(title=_t('Type'))
    quota_includes_snapshot_usage = schema.TextLine(title=_t('Includes Snapshot Usage?'))
    quota_path = schema.TextLine(title=_t('Path'))
    quota_hard_threshold_defined = schema.TextLine(title=_t('Hard Threshold Defined?'))
    quota_hard_threshold = schema.TextLine(title=_t('Hard Threshold'))
    quota_soft_threshold_defined = schema.TextLine(title=_t('Soft Threshold Defined?'))
    quota_soft_threshold = schema.TextLine(title=_t('Soft Threshold'))
    quota_advisory_threshold_defined = schema.TextLine(title=_t('Advisory Threshold Defined?'))
    quota_advisory_threshold = schema.TextLine(title=_t('ADvisory Threshold'))
    quota_grace_period = schema.TextLine(title=_t('Grace Period'))
    quota_usage = schema.TextLine(title=_t('Usage'))
    quota_usage_with_overhead = schema.TextLine(title=_t('Usage With Overhead'))
    quota_inode_usage = schema.TextLine(title=_t('Inode Usage'))
    quota_includes_overhead = schema.TextLine(title=_t('Quote Includes Overhead?'))
    
class IEMCIsilonLicenseInfo(IComponentInfo):
    license_status = schema.TextLine(title=_t('Status'))
    license_entry = schema.TextLine(title=_t('Entry'))