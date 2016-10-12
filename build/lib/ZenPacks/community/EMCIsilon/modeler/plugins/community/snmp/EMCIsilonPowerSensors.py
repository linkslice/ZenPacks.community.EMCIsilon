from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonPowerSensors(SnmpPlugin):
    relname = 'emcisilon_powersensors'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonPowerSensor'

    snmpGetTableMaps = (
        GetTableMap(
            'powerSensorTable', '.1.3.6.1.4.1.12124.2.55.1', {
                '.1': 'powerSensorNumber',
                '.2': 'powerSensorName',
                '.3': 'powerSensorDescription',
                '.4': 'powerSensorValue',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_powersensors = results[1].get('powerSensorTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_powersensors.items():
            name = row.get('powerSensorName')
            if not name:
                log.warn('Skipping empty sensor')
                continue

            log.debug('found sensor: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'powersensor_description': row.get('powerSensorDescription'),
                'powersensor_value': row.get('powerSensorValue'),
                }))

        log.debug(rm) 
        return rm
