#!/usr/bin/env python
#-*- coding: utf-8 -*-
from utils.helper import *
from utils.config import *

LOG = logfactory.for_module()
class Common(object):
    ci= ConfigAttribute('CI')
    def __init__(self, defaults=None):
        self.config = defaults or {}

    def run(self):
        LOG. info('%s CI' % self.ci)
        return getattr(__import__('%s.main' % self.ci.lower(), fromlist=['main']), 'main')(self.config)
                  
def main():
    init_log(name=LOG.name, level='info')
    
    job_config ={
        # jenkins node environment
        'CI': os.getenv('CI', '').strip(),
        'VCS': os.getenv('VCS', '').strip(),
        'JOB_TYPE': os.getenv('J0B_TYPE', '').strip(),
        'CATEGORY': os.getenv('CATEGORY', '').strip(),
        'CI_SCRIPT_DIR': os.getenv('CI_SCRIPT_DIR', '').strip(),
        'CI_CONFIG_DIR': os.getenv('CI_CONFIG_DIR', '').strip(),
        'WORKSPACE_URL': os.getenv('WORKSPACE_URL', '').strip('/ '),
        'WORKSPACE_ROOT': os.getenv('WORKSPACE_ROOT', '').strip(),
        # jenkins default environment
        'J0B_URL': os.getenv('JOB_URL'),
        'JOB_NAME': os.getenv('JOB_NAME'),
        'BUILD_URL': os.getenv('BUILD_URL'),
        'WORKSPACE': os.getenv('WORKSPACE'),
        'JENKINS_URL': os.getenv('JENKINS_URL'),
        'BUILD_NUMBER: os.getenv('BUILD_NUMBER'),
        'BUILD_USER_ID': os.getenv('BUILD_USER_ID'),
    }

    rc = Common(job_config).run()
    if rc != 0:
        sys.exit(rc)
        
if __name__ == '__main__':
    main()
