'''
Created on 19 janv. 2018

@author: ferre
'''
from switchhandler.device.protocol.expect.device_expect import DeviceExpect


class UnixExpect(DeviceExpect):
    '''
    classdocs
    '''

    def __init__(self, IP, vendor, site=None, dryrun=False):
        '''
        Constructor
        '''
        super().__init__('unix', IP, vendor, site, dryrun)
