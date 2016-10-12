from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonQuotas(SnmpPlugin):
    relname = 'emcisilon_quotas'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonQuota'

    snmpGetTableMaps = (
        GetTableMap(
            'quotaTable', '.1.3.6.1.4.1.12124.1.12.1.1', {
                '.2': 'quotaType',
                '.4': 'quotaIncludesSnapshotUsage',
                '.5': 'quotaPath',
                '.6': 'quotaHardThresholdDefined',
                '.7': 'quotaHardThreshold',
                '.8': 'quotaSoftThresholdDefined',
                '.9': 'quotaSoftThreshold',
                '.10': 'quotaAdvisoryThresholdDefined',
                '.11': 'quotaAdvisoryThreshold',
                '.12': 'quotaGracePeriod',
                '.13': 'quotaUsage',
                '.14': 'quotaUsageWithOverhead',
                '.15': 'quotaInodeUsage',
                '.16': 'quotaIncludesOverhead',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_quotas = results[1].get('quotaTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_quotas.items():
            name = row.get('quotaPath')
            if not name:
                log.warn('Skipping empty quota')
                continue

            log.debug('found quota: %s at %s', name, snmpindex.strip('.'))
           
            quotaTypes = [ "defaultUser",
                           "user",
                           "defaultGroup",
                           "group",
                           "directory",
                           "special",
                           "max"
                           ]
                            
            yesNo = [ "no", "yes" ]
            
            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'quota_type': quotaTypes[row.get('quotaType')],
                'quota_includes_snapshot_usage': yesNo[row.get('quotaIncludesSnapshotUsage')],
                'quota_path': row.get('quotaPath'),
                'quota_hard_threshold_defined': row.get('quotaHardThresholdDefined'),
                'quota_hard_threshold': row.get('quotaHardThreshold'),
                'quota_soft_threshold_defined': row.get('quotaSoftThresholdDefined'),
                'quota_soft_threshold': row.get('quotaSoftThreshold'),
                'quota_advisory_threshold_defined': row.get('quotaAdvisoryThresholdDefined'),
                'quota_advisory_threshold': row.get('quotaAdvisoryThreshold'),
                'quota_grace_period': row.get('quotaGracePeriod'),
                'quota_usage': row.get('quotaUsage'),
                'quota_usage_with_overhead': row.get('quotaUsageWithOverhead'),
                'quota_inode_usage': row.get('quotaInodeUsage'),
                'quota_includes_overhead': yesNo[row.get('quotaIncludesOverhead')],
                }))

        log.debug(rm)
        return rm
