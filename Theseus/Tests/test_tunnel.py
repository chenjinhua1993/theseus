import Theseus
import unittest2


class TestTheseusSSHTunnel(unittest2.TestCase):
    def setUp(self):
        self.logger = Theseus.get_logger(self._testMethodName)
        self.logger.info(self._testMethodName + ' - ' + self._testMethodDoc)

        self.secrets = Theseus.Secrets()
        self.user = self.secrets.get('Daedalus')['username']
        self.host = self.secrets.get('Daedalus')['host']

    def test_basic_tunnel(self):
        """ Create an ssh tunnel and then shut it down """
        self.sshtunnel = Theseus.Protocols.SSHTunnel(user=self.user, host=self.host, port=22, localport=8090, remoteport=8091)
        self.assertIsInstance(self.sshtunnel, Theseus.Protocols.SSHTunnel, msg="SSH Tunnel was connected")
        self.sshtunnel.stop_tunnel()
