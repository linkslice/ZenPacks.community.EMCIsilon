from zope.interface import implements

from Products.Zuul.infos import ProxyProperty
from Products.Zuul.infos.device import DeviceInfo
from Products.Zuul.infos.component import ComponentInfo

from ZenPacks.community.EMCIsilon.interfaces import (
    IEMCIsilonPowerSensorInfo,
    IEMCIsilonTempSensorInfo,
    IEMCIsilonFanInfo,
    IEMCIsilonDiskInfo,
    IEMCIsilonChassisInfo,
    IEMCIsilonDiskPerfInfo,
    IEMCIsilonNodeProtocolPerfInfo,
    IEMCIsilonSnapshotInfo,
    IEMCIsilonSnapshotScheduleInfo,
    IEMCIsilonQuotaInfo,
    IEMCIsilonLicenseInfo,
    )

class EMCIsilonPowerSensorInfo(ComponentInfo):
    implements(IEMCIsilonPowerSensorInfo)
    powersensor_description = ProxyProperty('powersensor_description')
    powersensor_value = ProxyProperty('powersensor_value')
    
class EMCIsilonTempSensorInfo(ComponentInfo):
    implements(IEMCIsilonTempSensorInfo)
    tempsensor_description = ProxyProperty('tempsensor_description')
    tempsensor_value = ProxyProperty('tempsensor_value')

class EMCIsilonFanInfo(ComponentInfo):
    implements(IEMCIsilonFanInfo)
    fan_description = ProxyProperty('fan_description')
    fan_speed = ProxyProperty('fan_speed')

class EMCIsilonDiskInfo(ComponentInfo):
    implements(IEMCIsilonDiskInfo)
    disk_bay = ProxyProperty('disk_bay')
    disk_logical_number = ProxyProperty('disk_logical_number')
    disk_chassis_number = ProxyProperty('disk_chassis_number')
    disk_status = ProxyProperty('disk_status')
    disk_model = ProxyProperty('disk_model')
    disk_serial_number = ProxyProperty('disk_serial_number')
    disk_firmware_version = ProxyProperty('disk_firmware_version')
    disk_size_bytes = ProxyProperty('disk_size_bytes')
    
class EMCIsilonChassisInfo(ComponentInfo):
    implements(IEMCIsilonChassisInfo)
    chassis_config_number = ProxyProperty('chassis_config_number')
    chassis_serial_number = ProxyProperty('chassis_serial_number')
    chassis_model = ProxyProperty('chassis_model')
    chassis_unit_idle_on = ProxyProperty('chassis_unit_idle_on')
    
class EMCIsilonDiskPerfInfo(ComponentInfo):
    implements(IEMCIsilonDiskPerfInfo)
    disk_perf_ops_per_second = ProxyProperty('disk_perf_ops_per_second')
    disk_perf_in_bits_per_second = ProxyProperty('disk_perf_in_bits_per_second')
    disk_perf_out_bits_per_second = ProxyProperty('disk_perf_out_bits_per_second')
    
class EMCIsilonNodeProtocolPerfInfo(ComponentInfo):
    implements(IEMCIsilonNodeProtocolPerfInfo)
    protocol_op_count = ProxyProperty('protocol_op_count')
    protocol_ops_per_second = ProxyProperty('protocol_ops_per_second')
    protocol_in_min_bytes = ProxyProperty('protocol_in_min_bytes')
    protocol_in_max_bytes = ProxyProperty('protocol_in_max_bytes')
    protocol_in_avg_bytes = ProxyProperty('protocol_in_avg_bytes')
    protocol_in_stddev_bytes = ProxyProperty('protocol_in_stddev_bytes')
    protocol_in_bps = ProxyProperty('protocol_in_bps')
    protocol_out_min_bytes = ProxyProperty('protocol_out_min_bytes')
    protocol_out_max_bytes = ProxyProperty('protocol_out_max_bytes')
    protocol_out_avg_bytes = ProxyProperty('protocol_out_avg_bytes')
    protocol_out_stddev_bytes = ProxyProperty('protocol_out_stddev_bytes')
    protocol_out_bps = ProxyProperty('protocol_out_bps')
    protocol_latency_min = ProxyProperty('protocol_latency_min')
    protocol_latency_max = ProxyProperty('protocol_latency_max')
    protocol_latency_avg = ProxyProperty('protocol_latency_avg')
    protocol_latency_stddev = ProxyProperty('protocol_latency_stddev')
    
class EMCIsilonSnapshotInfo(ComponentInfo):
    implements(IEMCIsilonSnapshotInfo)
    snapshot_created = ProxyProperty('snapshot_created')
    snapshot_expires = ProxyProperty('snapshot_expires')
    snapshot_size = ProxyProperty('snapshot_size')
    snapshot_path = ProxyProperty('snapshot_path')
    snapshot_alias_for = ProxyProperty('snapshot_alias_for')
    snapshot_locked = ProxyProperty('snapshot_locked')
    
class EMCIsilonSnapshotScheduleInfo(ComponentInfo):
    implements(IEMCIsilonSnapshotScheduleInfo)
    snapshot_schedule_alias = ProxyProperty('snapshot_schedule_alias')
    snapshot_schedule_naming_pattern = ProxyProperty('snapshot_schedule_naming_pattern')
    snapshot_schedule_schedule = ProxyProperty('snapshot_schedule_schedule')
    snapshot_schedule_expiration = ProxyProperty('snapshot_schedule_expiration')
    snapshot_schedule_path = ProxyProperty('snapshot_schedule_path')
    
class EMCIsilonQuotaInfo(ComponentInfo):
    implements(IEMCIsilonQuotaInfo)
    quota_type = ProxyProperty('quota_type')
    quota_includes_snapshot_usage = ProxyProperty('quota_includes_snapshot_usage')
    quota_path = ProxyProperty('quota_path')
    quota_hard_threshold_defined = ProxyProperty('quota_hard_threshold_defined')
    quota_hard_threshold = ProxyProperty('quota_hard_threshold')
    quota_soft_threshold_defined = ProxyProperty('quota_soft_threshold_defined')
    quota_soft_threshold = ProxyProperty('quota_soft_threshold')
    quota_advisory_threshold_defined = ProxyProperty('quota_advisory_threshold_defined')
    quota_advisory_threshold = ProxyProperty('quota_advisory_threshold')
    quota_grace_period = ProxyProperty('quota_grace_period')
    quota_usage = ProxyProperty('quota_usage')
    quota_usage_with_overhead = ProxyProperty('quota_usage_with_overhead')
    quota_inode_usage = ProxyProperty('quota_inode_usage')
    quota_includes_overhead = ProxyProperty('quota_includes_overhead')
    
class EMCIsilonLicenseInfo(ComponentInfo):
    implements(IEMCIsilonLicenseInfo)
    license_status = ProxyProperty('license_status')
    license_entry = ProxyProperty('license_entry')
