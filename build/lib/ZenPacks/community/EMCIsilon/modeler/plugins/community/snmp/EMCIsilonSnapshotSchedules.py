from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonSnapshotSchedules(SnmpPlugin):
    relname = 'emcisilon_snapshotschedules'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonSnapshotSchedule'

    snmpGetTableMaps = (
        GetTableMap(
            'emcIsilonSnapshotShcedulesTable', '.1.3.6.1.4.1.12124.1.13.2.1', {
                '.2': 'snapshotScheduleName',
                '.3': 'snapshotScheduleAlias',
                '.4': 'snapshotScheduleNamingPattern',
                '.5': 'snapshotScheduleSchedule',
                '.6': 'snapshotScheduleExpiration',
                '.7': 'snapshotSchedulePath',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_snapshotschedules = results[1].get('emcIsilonSnapshotShcedulesTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_snapshotschedules.items():
            name = row.get('snapshotScheduleName')
            if not name:
                log.warn('Skipping empty schedule')
                continue

            log.debug('found schedule: %s at %s', name, snmpindex.strip('.'))

            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'snapshot_schedule_alias': row.get('snapshotScheduleAlias'),
                'snapshot_schedule_naming_pattern': row.get('snapshotScheduleNamingPattern'),
                'snapshot_schedule_schedule': row.get('snapshotScheduleSchedule'),
                'snapshot_schedule_expiration': row.get('snapshotScheduleExpiration'),
                'snapshot_schedule_path': row.get('snapshotSchedulePath'),
                }))

        log.debug(rm)
        return rm
