from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonTempSensors(SnmpPlugin):
    relname = 'emcisilon_tempsensors'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonTempSensor'

    snmpGetTableMaps = (
        GetTableMap(
            'tempTable', '.1.3.6.1.4.1.12124.2.54.1', {
                '.2': 'tempSensorName',
                '.3': 'tempSensorDescription',
                '.4': 'tempSensorValue',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_tempsensors = results[1].get('tempTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_tempsensors.items():
            name = row.get('tempSensorName')
            if not name:
                log.warn('Skipping empty sensor')
                continue

            log.debug('found sensor: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'tempsensor_description': row.get('tempSensorDescription'),
                'tempsensor_value': row.get('tempSensorValue'),
                }))

        log.debug(rm)
        return rm
