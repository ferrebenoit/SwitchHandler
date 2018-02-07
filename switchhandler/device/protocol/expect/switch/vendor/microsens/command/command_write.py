# -*- coding: utf-8 -*-
'''
Created on 9 mai 2017

@author: ferreb
'''
from switchhandler.device.executable.command.command_base import CommandBase


class CommandWrite(CommandBase):
    '''Ecrire la configuration

    Commandes exécutées ::

      prompt# save settings
      prompt#
    '''
    # TODO: Check configMode self.getConfigMode() == ConfigMode.GLOBAL

    def do_run(self):
        self.switch.send_line('save settings')
        self.switch.expect_prompt()
