# -*- coding: utf-8 -*-
'''
Created on 9 mai 2017

@author: ferreb
'''
from switchhandler.device.executable.command.command_base import CommandBase
from switchhandler.device.protocol.expect.switch.vendor.allied import CATEGORY_ALLIED
from switchhandler.utils.decorator.class_register import registered_class


@registered_class(category=CATEGORY_ALLIED, registered_name="upload_file_tftp")
class ViewUploadFileTFTP(CommandBase):
    '''Charger un fichier sur le switch


    :param tftp_ip:
    :type  tftp_ip:
    :param local_file_path:
    :type  local_file_path:
    :param remote_file_path:
    :type  remote_file_path:

    Commandes exécutées::

      ViewUploadFileTFTP(tftp_ip='10.1.1.1', local_file_path='local/file', remote_file_path='remote/file')

      prompt# copy tftp://10.1.1.1/remote/file flash:/local/file
      prompt#

    '''

    def define_argument(self):
        self.add_argument(name='tftp_ip', required=True)
        self.add_argument(name='local_file_path', required=True)
        self.add_argument(name='remote_file_path', required=True)

    def do_run(self):
        self.switch.send_line(
            'copy tftp://{}{} flash:/{}'.format(
                self.tftp_ip,
                self.remote_file_path,
                self.local_file_path
            ))
        self.switch.expect_prompt()
