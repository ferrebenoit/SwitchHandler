from utils.switch.switch_base import SwitchBase, ConfigMode, Exec
from pexpect.exceptions import TIMEOUT, EOF
import datetime

class SwitchHP(SwitchBase):

    def __init__(self, IP):
        super(SwitchHP, self).__init__(IP)

        #prompt rexex
        self._PROMPT = '([A-Za-z0-9\-]*)(\((.*)\))*([>#])'
        self.connection.PROMPT = self._PROMPT

    @property
    def hostname(self):
        ''' strip the initial '1H' from the host name
        '''
        hostname = super(SwitchHP, self).hostname
        if not super(SwitchHP, self).hostname == 'None':
            hostname = hostname[2:] 
        
        return hostname

    def getExecLevel(self):
        if self.exec == '>':
            return Exec.USER
        elif self.exec == '#':
            return Exec.PRIVILEGED

    def getConfigMode(self):
        if self.configMode == '':
            return ConfigMode.GLOBAL
        elif self.configMode == 'config':
            return ConfigMode.TERMINAL   
    
    def auth_PublicKey(self, username, key, comment, TFTP_IP=''):
        self.end()
                
        self.connection.sendline('copy tftp pub-key-file {} {} manager append'.format(TFTP_IP, key))
        self.expectPrompt()
        
        self.conft()

        self.connection.sendline('aaa authentication ssh login public-key')
        self.expectPrompt()
        
        self.write()
        return True            
        
    def uploadFileTFTP(self, TFTP_IP, localFilePath, RemoteFilePath):
        self.connection.sendline('copy tftp flash {} {}'.format(TFTP_IP, localFilePath, RemoteFilePath))
        self.expectPrompt()
        
        return True
            
    def downloadFileTFTP(self, TFTP_IP, localFilePath, RemoteFilePath):
        # copy running-config tftp://192.168.0.1/
        try:
            self.connection.sendline('copy {} tftp {} {}'.format(localFilePath, TFTP_IP, RemoteFilePath))
            
            match = self.connection.expect([self._PROMPT, '00000K Peer unreachable.', 'Invalid input:'])
            if match > 0 :
                print('Sauvegarde echouee ')
                return False
            elif match == 0: 
                return True
            
            
            self.expectPrompt()
        except TIMEOUT :
            print("Sauvegarde echouee a cause d'un timeout")
            print(self.connection.before)
        except EOF :
            print("Sauvegarde echouee a cause d'une deconnexion")
            print(self.connection.before)
        except Exception as e:
            print('exception')
            #print(e)
            print(self.connection.before)
            print(self.connection.after)
            
    def enable(self):
        self.connection.sendline('enable')
        self.expectPrompt()
    
    def conft(self):
        self.connection.sendline('configure terminal')
        self.expectPrompt()
    
    def exit(self):
        self.connection.sendline('exit')
        self.expectPrompt()
            
    def end(self):
        self.connection.sendline('end')
        self.expectPrompt()
 
    def write(self):
        self.connection.sendline('write memory')
        self.expectPrompt()

    def save_conf_TFTP(self, TFTP_IP):
        self.end()
        
        return self.downloadFileTFTP(TFTP_IP, 'running-config', '{}_{:%Y%m%d-%H%M%S}.cnfg'.format(self.hostname, datetime.datetime.today()))

    def expectPrompt(self):
        return super(SwitchHP, self).expectPrompt()
             
    def login(self, login, password):
        try:
            self.connection._spawn("ssh {}@{} -o StrictHostKeyChecking=no -o UserKnownHostsFile=/dev/null".format(login, self.IP))

            self.connection.expect('password:')
            self.connection.sendline(password)
            
            self.connection.sendline()
            self._loadPromptState()
            
            return True
        except:
            print('login failed')
            print(self.connection.before)
            print(self.connection.after)
            return False
        #return super(SwitchHP, self).login(login, password)
            
    def logout(self):
        if super(SwitchHP, self).logout():
            self.connection.expect('[y/n]?')
            self.connection.send('y')
            return True
        else:
            return False
        
        
        