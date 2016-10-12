from Products.DataCollector.plugins.CollectorPlugin import (
    SnmpPlugin, GetTableMap,
    )


class EMCIsilonLicenses(SnmpPlugin):
    relname = 'emcisilon_licenses'
    modname = 'ZenPacks.community.EMCIsilon.EMCIsilonLicense'

    snmpGetTableMaps = (
        GetTableMap(
            'licenseTable', '.1.3.6.1.4.1.12124.1.5.1.1', {
                '.2': 'licenseModuleName',
                '.3': 'licenseStatus',
                }
            ),
        )

    def process(self, device, results, log):
        emcisilon_licenses = results[1].get('licenseTable', {})
        rm = self.relMap()
        for snmpindex, row in emcisilon_licenses.items():
            name = row.get('licenseModuleName')
            if not name:
                log.warn('Skipping empty license')
                continue

            log.debug('found license: %s at %s', name, snmpindex.strip('.'))

            status = row.get('licenseStatus')
            if status == -2:
                licenseStatus = 'inactive'
            elif status == -1:
                licenseStatus = 'expired'
            elif status == 0:
                licenseStatus = 'activated'
            else:
                licenseStatus = 'evaluation'
                
            rm.append(self.objectMap({
                'id': self.prepId(name),
                'title': name,
                'snmpindex': snmpindex.strip('.'),
                'license_status': licenseStatus,
                }))

        log.debug(rm)
        return rm
