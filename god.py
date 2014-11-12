#!/usr/bin/env python
__author__ = 'Taio'

import os
import sys
import time
import logging
import ConfigParser

config_file = ConfigParser.RawConfigParser()
option_c = sys.argv[2]
config_file.read('%s' % option_c)

logLevel = config_file.get('logging', 'log_level')

logger = logging.getLogger('god')
logging.basicConfig(filename='/var/log/god.log', level=logging.getLevelName(logLevel),
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

service_name = config_file.get('service', 'name')
command_line = config_file.get('service', 'command_line')
delay_loop = config_file.get('global', 'delay_loop')
delay_before_retry = config_file.get('global', 'delay_before_retry')


def usage():
    print '''
    Usage: python god.py -c [config_file]
    '''


def main():
    while True:
        time.sleep(int(delay_loop))
        try:
            ret = os.popen('ps -C %s -o pid,cmd' % service_name).readlines()
            if len(ret) < 2:
                logger.error('%s process error, %s seconds after the restart...' % (service_name, delay_before_retry))
                time.sleep(int(delay_before_retry))
                os.system('%s' % command_line)
        except:
            logger.error('Fuck error')
            print "Error", sys.exc_info()[1]


if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[1] == '-c':
        main()
    else:
        usage()


