#!/usr/bin/python

import glob
import os
import re

APP_STORE = '/data/CM/configManagement/AppStore'
APP_DIR = APP_STORE + '/appStore_3.2.1/'       # Enter current version here
PREV_APP_DIR = '/cm/AppStore/appStore_3.2/'    # Enter previous version here
TEAMS = ["cpt", "mdt"]

for TEAM in TEAMS:
    os.chdir(APP_DIR+TEAM)
    APPSTORELISTING = open(APP_STORE+'/Administration/'+TEAM+'AppStoreListing.txt','w')
    CHANGELOG = open(APP_STORE+'/Administration/'+TEAM+'AppStoreListingChangeLog.txt','w')
    APPSTORELISTING.write('Application, Version\n')
    CHANGELOG.write('Application, Version, Old Version\n')
    APPSTORELISTING.close()
    CHANGELOG.close()
    APPSTORELISTING = open(APP_STORE+'/Administration/'+TEAM+'AppStoreListing.txt','a')
    CHANGELOG = open(APP_STORE+'/Administration/'+TEAM+'AppStoreListingChangeLog.txt','a')
    dirs = [appdir for appdir in os.listdir('.') if os.path.isdir(appdir)]
    for appdir in dirs:
        os.chdir(appdir)
        VFILE = open('version.txt','r')
        VERSION = VFILE.readline()
        VERSION = re.sub(r"\n", "", VERSION)
        VFILE.close()
        os.chdir('..')
        APPSTORELISTING.write(appdir+', '+VERSION+'\n')
        VFILE.close()
        VFILE = open(PREV_APP_DIR+TEAM+'/'+appdir+'/version.txt','r')
        OLD_VERSION = VFILE.readline()
        OLD_VERSION = re.sub(r"\n", "", OLD_VERSION)
        VFILE.close()
        if OLD_VERSION != VERSION:
            CHANGELOG.write(appdir+', '+VERSION+', '+OLD_VERSION+'\n')
    APPSTORELISTING.close()
    CHANGELOG.close()
