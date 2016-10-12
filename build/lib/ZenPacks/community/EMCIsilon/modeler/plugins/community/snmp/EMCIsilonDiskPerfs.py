from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonDiskPerfs(SnmpPlugin):
    relname = 'emcisilon_diskperfs'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonDiskPerf'

    snmpGetTableMaps = (
        GetTableMap(
            'diskPerfTable', '.1.3.6.1.4.1.12124.2.2.52.1', {
                '.1': 'diskPerfBay',
                '.2': 'diskPerfDeviceName',
                '.3': 'diskperfOpsPerSecond',
                '.4': 'diskperfInBitsPerSecond',
                '.5': 'diskperfOutBitsPerSecond',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_diskperfs = results[1].get('diskPerfTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_diskperfs.items():
            name = row.get('diskPerfDeviceName')
            if not name:
                log.warn('Skipping empty disk perf stats')
                continue

            log.debug('found disk perf stats: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'disk_perf_ops_per_second': row.get('diskperfOpsPerSecond'),
                'disk_perf_in_bits_per_second': row.get('diskperfInBitsPerSecond'),
                'disk_perf_out_bits_per_second': row.get('diskperfOutBitsPerSecond'),
                }))

        log.debug(rm)
        return rm
