# -*- coding: utf-8 -*-
'''
Created on 9 mai 2017

@author: ferreb
'''
from switchhandler.device.executable.command.command_base import CommandBase
from switchhandler.device.protocol.expect.switch.vendor.cisco import CATEGORY_CISCO
from switchhandler.utils.decorator.class_register import registered_class


@registered_class(category=CATEGORY_CISCO, registered_name="acl")
class CommandACL(CommandBase):
    '''Créer/se placer dans la configuration d'une ACL

    :param name: le nom de l'ACL
    :type name: str


    Commandes exécutées::

      prompt# ip access-list extended NAME
      prompt#

    '''
    # TODO: Check configMode self.getConfigMode() == ConfigMode.GLOBAL

    def define_argument(self):
        self.add_argument(name='name', required=True)

    def do_run(self):
        self.switch.send_line('ip access-list extended {}'.format(self.name))
        self.switch.expect_prompt()
