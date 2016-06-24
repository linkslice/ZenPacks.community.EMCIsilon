from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonNodeProtocolPerfs(SnmpPlugin):
    relname = 'emcisilon_nodeprotocolperfs'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonNodeProtocolPerf'

    snmpGetTableMaps = (
        GetTableMap(
            'nodeprotocolPerfTable', '.1.3.6.1.4.1.12124.2.2.10.1', {
                '.1': 'protocolName',
                '.2': 'protocolOpCount',
                '.3': 'protocolOpsPerSecond',
                '.4': 'inMinBytes',
                '.5': 'inMaxBytes',
                '.6': 'inAvgBytes',
                '.7': 'inStdDevBytes',
                '.8': 'inBitsPerSecond',
                '.9': 'outMinBytes',
                '.10': 'outMaxBytes',
                '.11': 'outAvgBytes',
                '.12': 'outStdDevBytes',
                '.13': 'outBitsPerSecond',
                '.14': 'latencyMin',
                '.15': 'latencyMax',
                '.16': 'latencyAverage',
                '.17': 'latencyStdDev',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_nodeprotocolperfs = results[1].get('nodeprotocolPerfTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_nodeprotocolperfs.items():
            name = row.get('protocolName')
            if not name:
                log.warn('Skipping empty protocol')
                continue

            log.debug('found protocol: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'protocol_op_count': row.get('protocolOpCount'),
                'protocol_ops_per_second': row.get('protocolOpsPerSecond'),
                'protocol_in_min_bytes': row.get('inMinBytes'),
                'protocol_in_max_bytes': row.get('inMaxBytes'),
                'protocol_in_avg_bytes': row.get('inAvgBytes'),
                'protocol_in_stddev_bytes': row.get('inStdDevBytes'),
                'protocol_in_bps': row.get('inBitsPerSecond'),
                'protocol_out_min_bytes': row.get('outMinBytes'),
                'protocol_out_max_bytes': row.get('outMaxBytes'),
                'protocol_out_avg_bytes': row.get('outAvgBytes'),
                'protocol_out_stddev_bytes': row.get('outStdDevBytes'),
                'protocol_out_bps': row.get('outBitsPerSecond'),
                'protocol_latency_min': row.get('latencyMin'),
                'protocol_latency_max': row.get('latencyMax'),
                'protocol_latency_avg': row.get('latencyAverage'),
                'protocol_latency_stddev': row.get('latencyStdDev'),
                }))

        log.debug(rm)
        return rm
