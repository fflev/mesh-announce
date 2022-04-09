import providers
from providers.util import call
import platform


class Source(providers.DataSource):
    def call(self):
        try:
            os_release = platform.freedesktop_os_release()
            return os_release['VERSION_ID']
        except:
            return call(['lsb_release', '-rs'])[0]
