#!/usr/bin/env python
#-*- coding: utf-8 -*-
from utils.helper import *from utils. config import *LOG = logfactory.for module()class Common(object):ci= ConfigAttribute("CI')definit (self, defaults-None):self.config = defaults or def run(self):LOG. info(%s CI', self.ci)return getattr( import (.%s.main, % self.ci.lower(), fromlist-[ 'main'l), 'main')(self.config)def main():init log(name-LOG.name, level-'info')iob config ={#ienkins node environmentCI: os.getenv(.CI', .).strip(),yCS: os.getenv('vCS', ..).strip(),JOB TYPE : os.getenv('J0B TYPE'. .).strip(),.CATEGORY": os.getenv(CATEGORY...).strip(),CI SCRIPT DIR': os.getenv('CI SCRIPT DIR', .).strip(),,CI CONFIG DIR': os.getenv('CI CONFIG DIR', .).strip(),WORKSPACE URL': os.getenv( 'WORKSPACE URL', .).strip(./ .),WORKSPACE ROOT': os.getenv( 'WORKSPACE ROOT', .).strip(),#ienkins default environment.J0B URL': os.getenv(.JOB URL').1OB NAME: os.getenv(•JOB NAME'),BUILD URL': os.getenv('BUILD URL'),WORKSPACE': os.getenv( 'WORKSPACE.).JFNKINS URL': os.getenv('JENKINS URL').RUILD NUMBER.: os.getenv('BUILD NUMBER'),BUILD USER ID': os.getenv( 'BUILD USER ID'),-}rc=Common(job_config).run()ifrc l=a:sys.exit(rc)if namemain()==main:
