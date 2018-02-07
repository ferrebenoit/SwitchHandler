# -*- coding: utf-8 -*-
'''
Created on 9 mai 2017

@author: ferreb
'''
from switchhandler.device.executable.command.command_base import CommandBase


class CommandVlan(CommandBase):
    '''Créer/se placer dans la configuration d'un Vlan

    :param id: l'id
    :type name: str

    :param name: le nom du Vlan
    :type name: str


    Commandes exécutées::

      CommandVlan(id='80', name='Imprimante')

      prompt# interface vlan80
      prompt# name Imprimante
      prompt#

    '''
    # TODO: Check configMode self.getConfigMode() == ConfigMode.GLOBAL
    def define_argument(self):
        self.add_argument(name='id', required=True)
        self.add_argument(name='name', default='')

    def do_run(self):
        self.switch.send_line('vlan database')
        self.switch.expect_prompt()

        if self.name != '':
            self.switch.send_line('vlan {} name {}'.format(self.id, self.name))
            self.switch.expect_prompt()
