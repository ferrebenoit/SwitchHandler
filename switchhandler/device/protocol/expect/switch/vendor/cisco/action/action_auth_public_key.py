'''
Created on 9 mai 2017

@author: ferreb
'''
from switchhandler.device.executable.action.action_base import ActionBase


class ActionAuthPublicKey(ActionBase):
    '''Ajouter un Vlan avec son Id, nom, IP, netmask, ip helper


    def auth_PublicKey(self, username, key, comment, TFTP_IP=''):
    :param username: Le nom d'utilisateur à associer à la clé
    :type  username: str
    :param key: La clé
    :type  key: str
    :param comment: Commentaire
    :type  comment: str
    :param tftp_ip: ip du tftp
    :type  tftp_ip: str
    :default  tftp_ip: None

    Commandes exécutées::

      prompt#
      prompt#
    '''

    def define_argument(self):
        self.add_argument(name='keyuser', required=True)
        self.add_argument(name='keyhash', required=True)
        self.add_argument(name='keycomment', required=True)

    def arg_default(self):
        # self.tftp_ip = getattr(self, 'tftp_ip', None)
        pass

    def do_run(self):
        self.switch.execute('end')
        self.switch.execute('conft')

        self.switch.send_line('ip ssh pubkey-chain')
        self.switch.expect_prompt()

        self.switch.send_line('username {}'.format(self.keyuser))
        self.switch.expect_prompt()

        # use key-string store only the key hash
        self.switch.send_line('key-hash ssh-rsa {} {}'.format(self.keyhash, self.keycomment))
        self.switch.expect_prompt()

        self.switch.execute('write')
        return True
