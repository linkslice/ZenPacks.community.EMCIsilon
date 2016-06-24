(function(){

var ZC = Ext.ns('Zenoss.component');

ZC.registerName(
    'EMCIsilonIsilonChassis',
    _t('Isilon Chassis'),
    _t('Isilon Chassis'));

ZC.registerName(
    'EMCIsilonIsilonDisk',
    _t('Isilon Disk'),
    _t('Isilon Disks'));

ZC.registerName(
    'EMCIsilonIsilonDiskPerf',
    _t('Isilon Disk Perf'),
    _t('Isilon Disks Perf'));
    
ZC.registerName(
    'EMCIsilonIsilonFan',
    _t('Isilon Fan'),
    _t('Isilon Fans'));
    
ZC.registerName(
    'EMCIsilonIsilonLicense',
    _t('Isilon License'),
    _t('Isilon Licenses'));
    
ZC.registerName(
    'EMCIsilonIsilonNodeProtocolPerf',
    _t('Isilon Protocol Perf'),
    _t('Isilon Protocols Perf'));
    
ZC.registerName(
    'EMCIsilonIsilonPowerSensor',
    _t('Isilon Power Sensor'),
    _t('Isilon Power Sensors'));

ZC.registerName(
    'EMCIsilonIsilonQuota',
    _t('Isilon Quota'),
    _t('Isilon Quotas'));
    
ZC.registerName(
    'EMCIsilonIsilonSnapshot',
    _t('Isilon Snapshot'),
    _t('Isilon Snapshots'));
        
ZC.registerName(
    'EMCIsilonIsilonSnapshotSchedule',
    _t('Isilon Snapshot Schedule'),
    _t('Isilon Snapshot Schedules'));
   
ZC.registerName(
    'EMCIsilonIsilonTempSensor',
    _t('Isilon Temp Sensor'),
    _t('Isilon Temp Sensors'));  
              
ZC.EMCIsilonIsilonChassisPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonChassis',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'chassis_config_number'},
                {name: 'chassis_serial_number'},
                {name: 'chassis_model'},
                {name: 'chassis_unit_idle_on'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'chassis_config_number',
                dataIndex: 'chassis_config_number',
                header: _t('Config Number'),
                sortable: true,
                width: 120
            },{
                id: 'chassis_serial_number',
                dataIndex: 'chassis_serial_number',
                header: _t('Serial Number'),
                sortable: true,
                width: 120
            },{
                id: 'chassis_model',
                dataIndex: 'chassis_model',
                header: _t('Model'),
                sortable: true,
                width: 400
            },{
                id: 'chassis_unit_idle_on',
                dataIndex: 'chassis_unit_idle_on',
                header: _t('ID LED On?'),
                sortable: true,
                width: 120                                
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonChassisPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonDiskPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonDisk',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'disk_bay'},
                {name: 'disk_logical_number'},
                {name: 'disk_chassis_number'},
                {name: 'disk_device_name'},
                {name: 'disk_status'},
                {name: 'disk_model'},
                {name: 'disk_serial_number'},
                {name: 'disk_firmware_version'},
                {name: 'disk_size_bytes'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'disk_bay',
                dataIndex: 'disk_bay',
                header: _t('Bay'),
                sortable: true,
                width: 120
            },{
                id: 'disk_logical_number',
                dataIndex: 'disk_logical_number',
                header: _t('Logical No.'),
                sortable: true,
                width: 120
            },{
                id: 'disk_chassis_number',
                dataIndex: 'disk_chassis_number',
                header: _t('Chassis No.'),
                sortable: true,
                width: 120
            },{
                id: 'disk_device_name',
                dataIndex: 'disk_device_name',
                header: _t('Device Name'),
                sortable: true,
                width: 120
            },{
                id: 'disk_status',
                dataIndex: 'disk_status',
                header: _t('Status'),
                sortable: true,
                width: 120
            },{
                id: 'disk_model',
                dataIndex: 'disk_model',
                header: _t('Model'),
                sortable: true,
                width: 120
            },{
                id: 'disk_serial_number',
                dataIndex: 'disk_serial_number',
                header: _t('Serial No.'),
                sortable: true,
                width: 120
            },{
                id: 'disk_firmware_version',
                dataIndex: 'disk_firmware_version',
                header: _t('Firmware Version'),
                sortable: true,
                width: 120
            },{
                id: 'disk_size_bytes',
                dataIndex: 'disk_size_bytes',
                header: _t('Size'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonDiskPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonDiskPerfPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonDiskPerf',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'disk_perf_ops_per_second'},
                {name: 'disk_perf_in_bits_per_second'},
                {name: 'disk_perf_out_bits_per_second'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'disk_perf_ops_per_second',
                dataIndex: 'disk_perf_ops_per_second',
                header: _t('IOPS'),
                sortable: true,
                width: 120
            },{
                id: 'disk_perf_in_bits_per_second',
                dataIndex: 'disk_perf_in_bits_per_second',
                header: _t('in bits/s'),
                sortable: true,
                width: 120
            },{
                id: 'disk_perf_out_bits_per_second',
                dataIndex: 'disk_perf_out_bits_per_second',
                header: _t('out bits/s'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonDiskPerfPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonFanPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonFan',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'fan_description'},
                {name: 'fan_speed'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'fan_description',
                dataIndex: 'fan_description',
                header: _t('Description'),
                sortable: true,
                width: 340
            },{
                id: 'fan_speed',
                dataIndex: 'fan_speed',
                header: _t('RPM'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonFanPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonLicensePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonLicense',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'license_status'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'license_status',
                dataIndex: 'license_status',
                header: _t('Status'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonLicensePanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonNodeProtocolPerfPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonNodeProtocolPerf',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonNodeProtocolPerfPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonPowerSensorPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonPowerSensor',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'powersensor_description'},
                {name: 'powersensor_value'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'powersensor_description',
                dataIndex: 'powersensor_description',
                header: _t('Description'),
                sortable: true,
                width: 250
            },{
                id: 'powersensor_value',
                dataIndex: 'powersensor_value',
                header: _t('Value'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonPowerSensorPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonQuotaPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonQuota',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'quota_type'},
                {name: 'quota_includes_snapshot_usage'},
                {name: 'quota_path'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'quota_type',
                dataIndex: 'quota_type',
                header: _t('Type'),
                sortable: true,
                width: 250
            },{
                id: 'quota_includes_snapshot_usage',
                dataIndex: 'quota_includes_snapshot_usage',
                header: _t('Includes Snapshot?'),
                sortable: true,
                width: 120
            },{
                id: 'quota_path',
                dataIndex: 'quota_path',
                header: _t('Path'),
                sortable: true,
                width: 300
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonQuotaPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonSnapshotPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonSnapshot',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'snapshot_created'},
                {name: 'snapshot_expires'},
                {name: 'snapshot_size'},
                {name: 'snapshot_path'},
                {name: 'snapshot_alias_for'},
                {name: 'snapshot_locked'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'snapshot_created',
                dataIndex: 'snapshot_created',
                header: _t('Created'),
                sortable: true,
                width: 120
            },{
                id: 'snapshot_expires',
                dataIndex: 'snapshot_expires',
                header: _t('Expires'),
                sortable: true,
                width: 70
            },{
                id: 'snapshot_size',
                dataIndex: 'snapshot_size',
                header: _t('Size'),
                sortable: true,
                width: 70
            },{
                id: 'snapshot_path',
                dataIndex: 'snapshot_path',
                header: _t('Path'),
                sortable: true,
                width: 140
            },{
                id: 'snapshot_alias_for',
                dataIndex: 'snapshot_alias_for',
                header: _t('Alias For'),
                sortable: true,
                width: 70
            },{
                id: 'snapshot_locked',
                dataIndex: 'snapshot_locked',
                header: _t('Locked'),
                sortable: true,
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonSnapshotPanel.superclass.constructor.call(
            this, config);
    }
});

ZC.EMCIsilonIsilonSnapshotSchedulePanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonSnapshotSchedule',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'snapshot_schedule_alias'},
                {name: 'snapshot_schedule_naming_pattern'},
                {name: 'snapshot_schedule_schedule'},
                {name: 'snapshot_schedule_expiration'},
                {name: 'snapshot_schedule_path'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'snapshot_schedule_alias',
                dataIndex: 'snapshot_schedule_alias',
                header: _t('Alias'),
                sortable: true,
                width: 120
            },{
                id: 'snapshot_schedule_naming_pattern',
                dataIndex: 'snapshot_schedule_naming_pattern',
                header: _t('Naming Pattern'),
                sortable: true,
                width: 70
            },{
                id: 'snapshot_schedule_schedule',
                dataIndex: 'snapshot_schedule_schedule',
                header: _t('Schedule'),
                sortable: true,
                width: 70
            },{
                id: 'snapshot_schedule_expiration',
                dataIndex: 'snapshot_schedule_expiration',
                header: _t('Expiration'),
                sortable: true,
                width: 140
            },{
                id: 'snapshot_schedule_path',
                dataIndex: 'snapshot_schedule_path',
                header: _t('Path'),
                sortable: true,
                width: 70
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonSnapshotSchedulePanel.superclass.constructor.call(
            this, config);
    }
});


ZC.EMCIsilonIsilonTempSensorPanel = Ext.extend(ZC.ComponentGridPanel, {
    constructor: function(config) {
        config = Ext.applyIf(config||{}, {
            componentType: 'EMCIsilonIsilonTempSensor',
            autoExpandColumn: 'name',
            sortInfo: {
                field: 'name',
                direction: 'ASC'
            },
            fields: [
                {name: 'uid'},
                {name: 'name'},
                {name: 'status'},
                {name: 'severity'},
                {name: 'usesMonitorAttribute'},
                {name: 'monitor'},
                {name: 'monitored'},
                {name: 'locking'},
                {name: 'tempsensor_description'},
                {name: 'tempsensor_value'},
            ],
            columns: [{
                id: 'severity',
                dataIndex: 'severity',
                header: _t('Events'),
                renderer: Zenoss.render.severity,
                sortable: true,
                width: 50
            },{
                id: 'name',
                dataIndex: 'name',
                header: _t('Name'),
                sortable: true
            },{
                id: 'tempsensor_description',
                dataIndex: 'tempsensor_description',
                header: _t('Description'),
                sortable: true,
                width: 350
            },{
                id: 'tempsensor_value',
                dataIndex: 'tempsensor_value',
                header: _t('Value'),
                sortable: true,
                width: 120
            },{
                id: 'monitored',
                dataIndex: 'monitored',
                header: _t('Monitored'),
                renderer: Zenoss.render.checkbox,
                sortable: true,
                width: 70
            },{
                id: 'locking',
                dataIndex: 'locking',
                header: _t('Locking'),
                renderer: Zenoss.render.locking_icons,
                width: 65
            }]
        });

        ZC.EMCIsilonIsilonTempSensorPanel.superclass.constructor.call(
            this, config);
    }
});

Ext.reg('EMCIsilonIsilonChassisPanel', ZC.EMCIsilonIsilonChassisPanel);
Ext.reg('EMCIsilonIsilonDiskPanel', ZC.EMCIsilonIsilonDiskPanel);
Ext.reg('EMCIsilonIsilonDiskPerfPanel', ZC.EMCIsilonIsilonDiskPerfPanel);
Ext.reg('EMCIsilonIsilonFanPanel', ZC.EMCIsilonIsilonFanPanel);
Ext.reg('EMCIsilonIsilonLicensePanel', ZC.EMCIsilonIsilonLicensePanel);
Ext.reg('EMCIsilonIsilonNodeProtocolPerfPanel', ZC.EMCIsilonIsilonNodeProtocolPerfPanel);
Ext.reg('EMCIsilonIsilonPowerSensorPanel', ZC.EMCIsilonIsilonPowerSensorPanel);
Ext.reg('EMCIsilonIsilonQuotaPanel', ZC.EMCIsilonIsilonQuotaPanel);
Ext.reg('EMCIsilonIsilonSnapshotPanel', ZC.EMCIsilonIsilonSnapshotPanel);
Ext.reg('EMCIsilonIsilonSnapshotSchedulePanel', ZC.EMCIsilonIsilonSnapshotSchedulePanel);
Ext.reg('EMCIsilonIsilonTempSensorPanel', ZC.EMCIsilonIsilonTempSensorPanel);


})();
