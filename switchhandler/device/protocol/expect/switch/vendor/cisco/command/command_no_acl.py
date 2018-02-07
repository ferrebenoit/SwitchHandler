# -*- coding: utf-8 -*-
'''
Created on 9 mai 2017

@author: ferreb
'''
from switchhandler.device.executable.command.command_base import CommandBase


class CommandNoACL(CommandBase):
    '''Créer/se placer dans la configuration d'une ACL

    :param name: le nom de l'ACL
    :type name: str


    Commandes exécutées::

      CommandNoACL(name=ACL-Imprimante-IN)

      prompt# no ip access-list extended ACL-Imprimante-IN
      prompt#

    '''
    # TODO: Check configMode self.getConfigMode() == ConfigMode.GLOBAL
    def define_argument(self):
        self.add_argument(name='name', required=True)

    def do_run(self):
        self.switch.send_line('no ip access-list extended {}'.format(self.name))
        self.switch.expect_prompt()
