'''
Created on 23 nov. 2016

@author: FERREB
'''
from utils.arg_from_csv import ArgFromCSV
import re

class SwitchScripter(ArgFromCSV):
    "Class That desactivate an wifi AP"

    def _define_args(self):
        super()._define_args()
        self._arg_parser.add_argument('--IP', help='AP IP address')
        self._arg_parser.add_argument('--login', help='login')
        self._arg_parser.add_argument('--password', help='password')
        self._arg_parser.add_argument('--vendor', help='the vendor')
        self._arg_parser.add_argument('--name', help='the switch name')
                
        self._add_mandatory_arg('IP', 'vendor', 'login', 'password')
        
    def _script_content(self, args):
        if(re.compile('cisco', flags=re.IGNORECASE).search(args['vendor'])):
        #if(args['vendor'].lower().contains('cisco')):
            self._script_content_cisco(args)
        if(re.compile('hp', flags=re.IGNORECASE).search(args['vendor'])):
        #elif(args['vendor'].lower().contains('hp')):
            self._script_content_hp(args)
        if(re.compile('allied', flags=re.IGNORECASE).search(args['vendor'])):
        #elif(args['vendor'].lower().contains('allied')):
            self._script_content_allied(args)

    def _script_content_cisco(self, args):
        pass
        
    def _script_content_hp(self, args):
        pass
    
    def _script_content_allied(self, args):
        pass