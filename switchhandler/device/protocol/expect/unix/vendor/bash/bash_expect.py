'''
Created on 19 janv. 2018

@author: ferre
'''
from switchhandler.device.protocol.expect.unix.unix_expect import UnixExpect


class BashExpect(UnixExpect):
    '''
    classdocs
    '''

    def __init__(self, IP, vendor, site=None, dryrun=False):
        '''
        Constructor
        '''
        super().__init__('bash', IP, vendor, site, dryrun)
