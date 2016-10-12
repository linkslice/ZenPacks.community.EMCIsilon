from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonChassises(SnmpPlugin):
    relname = 'emcisilon_chassises'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonChassis'

    snmpGetTableMaps = (
        GetTableMap(
            'chassisTable', '.1.3.6.1.4.1.12124.2.51.1', {
                '.1': 'chassisNumber',
                '.2': 'chassisConfigNumber',
                '.3': 'chassisSerialNumber',
                '.4': 'chassisModel',
                '.5': 'chassisUnitIdleOn',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_chassises = results[1].get('chassisTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_chassises.items():
            name = row.get('chassisConfigNumber')
            if not name:
                log.warn('Skipping empty chassis')
                continue

            log.debug('found chassis: %s at %s', name, snmpindex.strip('.'))

            idleDOn = row.get('chassisUnitIdleOn')
            
            if idleDOn == -1:
                idleDOn = 'na'
            elif idleDOn == '0':
                idleDOn = 'no'
            else:
                idleDon = 'yes'
                
            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'chassis_config_number': row.get('chassisConfigNumber'),
                'chassis_serial_number': row.get('chassisSerialNumber'),
                'chassis_model': row.get('chassisModel'),
                'chassis_unit_idle_on': idleDOn,
                }))

        log.debug(rm)
        return rm
