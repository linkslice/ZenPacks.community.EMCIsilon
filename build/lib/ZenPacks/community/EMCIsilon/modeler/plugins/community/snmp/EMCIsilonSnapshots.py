from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonSnapshots(SnmpPlugin):
    relname = 'emcisilon_snapshots'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonSnapshot'

    snmpGetTableMaps = (
        GetTableMap(
            'snapshotTable', '.1.3.6.1.4.1.12124.1.13.3.1', {
                '.2': 'snapshotName',
                '.3': 'snapshotCreated',
                '.4': 'snapshotExpires',
                '.5': 'snapshotSize',
                '.6': 'snapshotPath',
                '.7': 'snapshotAliasFor',
                '.8': 'snapshotLocked',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_snapshots = results[1].get('snapshotTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_snapshots.items():
            name = row.get('snapshotName')
            if not name:
                log.warn('Skipping empty snapshot')
                continue

            log.debug('found snapshot: %s at %s', name, snmpindex.strip('.'))

            yesNo = [ "no", "yes" ]

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'snapshot_created': row.get('snapshotCreated'),
                'snapshot_expires': row.get('snapshotExpires'),
                'snapshot_size': row.get('snapshotSize'),
                'snapshot_path': row.get('snapshotPath'),
                'snapshot_alias_for': row.get('snapshotAliasFor'),
                'snapshot_locked': yesNo[row.get('snapshotLocked')],
                }))

        log.debug(rm)
        return rm
