import providers
from glob import glob


class Source(providers.DataSource):
    def required_args(self):
        return ['batadv_dev']

    def call(self, batadv_dev):
        upper = glob('/sys/class/net/' + batadv_dev + '/upper*')
        if len(upper) > 0:
            sysfs_path = upper[0]
        else:
            sysfs_path = '/sys/class/net/' + batadv_dev

        return open(sysfs_path + '/address').read().strip().replace(':', '')
