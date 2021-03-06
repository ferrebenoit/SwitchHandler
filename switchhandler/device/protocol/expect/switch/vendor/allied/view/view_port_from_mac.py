# -*- coding: utf-8 -*-
'''
Created on 9 mai 2017

@author: ferreb
'''
import re

from switchhandler.device.executable.command.command_base import CommandBase
from switchhandler.device.protocol.expect.switch.vendor.allied import CATEGORY_ALLIED
from switchhandler.utils.decorator.class_register import registered_class
from switchhandler.utils.net_tools import convert_mac_allied


@registered_class(category=CATEGORY_ALLIED, registered_name="port_from_mac")
class ViewPortFromMac(CommandBase):
    '''visualiser le port à l'quel une mac est associé

    :param mac: la mac à trouver
    :type name: str

    :param ip: L'ip à pringuer pour l'apprentissage de la mac
    :type ip: str
    :default ip: None


    Commandes exécutées::

      ViewPortFromMac(mac='aa:bb:cc:dd:ee:ff', ip='127.0.0.1')

      prompt# ping 127.0.0.1
      prompt# show mac address-table | include aa:bb:cc:dd:ee:ff
      prompt#

    '''

    def define_argument(self):
        self.add_argument(name='mac', required=True)
        self.add_argument(name='ip', default=None)

    def do_run(self):
        self.switch.execute('end')
        self.switch.execute('enable')

        self.mac = convert_mac_allied(self.mac)

        if self.ip is not None:
            self.switch.execute('ping', ip=self.ip, repeat=3)
            self.switch.expect_prompt()

        self.switch.send_line("show mac address-table | include {}".format(self.mac))
        self.switch.expect_prompt()

        match = re.search(
            '^([0-9][0-9]*)[ ]*([^ ]*)[ ]*([^ ]*)[ ]*([^ ]*)[ ]*([^ ]*)$',
            self.switch.before(),
            re.MULTILINE
        )

        if match:
            return match.group(2)
        else:
            return ""
