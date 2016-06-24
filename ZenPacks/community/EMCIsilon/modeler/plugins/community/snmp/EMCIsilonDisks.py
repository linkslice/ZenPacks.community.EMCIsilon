from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonDisks(SnmpPlugin):
    relname = 'emcisilon_disks'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonDisk'

    snmpGetTableMaps = (
        GetTableMap(
            'diskTable', '.1.3.6.1.4.1.12124.2.52.1', {
                '.1': 'diskBay',
                '.2': 'diskLogicalNumber',
                '.3': 'diskChassisNumber',
                '.4': 'diskDeviceName',
                '.5': 'diskStatus',
                '.6': 'diskModel',
                '.7': 'diskSerialNumber',
                '.8': 'diskFirmwareVersion',
                '.9': 'diskSizeBytes',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_disks = results[1].get('diskTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_disks.items():
            name = row.get('diskDeviceName')
            if not name:
                log.warn('Skipping empty zone')
                continue

            log.debug('found disk: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'disk_bay': row.get('diskBay'),
                'disk_logical_number': row.get('diskLogicalNumber'),
                'disk_chassis_number': row.get('diskChassisNumber'),
                'disk_status': row.get('diskStatus'),
                'disk_model': row.get('diskModel'),
                'disk_serial_number': row.get('diskSerialNumber'),
                'disk_firmware_version': row.get('diskFirmwareVersion'),
                'disk_size_bytes': row.get('diskSizeBytes'),
                }))

        log.debug(rm)
        return rm
