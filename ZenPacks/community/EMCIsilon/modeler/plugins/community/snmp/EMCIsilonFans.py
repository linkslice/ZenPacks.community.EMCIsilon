from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonFans(SnmpPlugin):
    relname = 'emcisilon_fans'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonFan'

    snmpGetTableMaps = (
        GetTableMap(
            'fanTable', '.1.3.6.1.4.1.12124.2.53.1', {
                '.1': 'fanNumber',
                '.2': 'fanName',
                '.3': 'fanDescription',
                '.4': 'fanSpeed',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_fans = results[1].get('fanTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_fans.items():
            name = row.get('fanName')
            if not name:
                log.warn('Skipping empty fan')
                continue

            log.debug('found fan: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'fan_description': row.get('fanDescription'),
                'fan_speed': row.get('fanSpeed'),
                }))

        log.debug(rm)
        return rm
