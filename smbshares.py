#!/usr/bin/env python3

# python script to generate commands to create smb shares
# on a new cluster from a source cluster
# where isi smb shares list --format=json > smbshares.json
# is used as the input

# current features tracked are:
# permissions, description

import json

with open('depot_smb_shares.json') as smbshares:
    smb_share_data = json.load(smbshares)


for i in smb_share_data:

    
    command = "isi smb shares create "
    path = str(i['path'])
    description = str(i['description'])
    sharename = str(i['name'])

    dircreatemask = i['directory_create_mask'] 
    filecreatemask = i['file_create_mask']
    dircreatemode = i['directory_create_mode']
    filecreatemode = i['file_create_mode']

    command += sharename + " " + path
    command += " --description \"" + description + "\""
    command += " --directory-create-mask " + str(dircreatemask) 
    command += " --file-create-mask " + str(filecreatemask)
    command += " --directory-create-mode " + str(dircreatemode)
    command += " --file-create-mode " + str(filecreatemode)

    print(command) 

    for permissionitem in i['permissions']:
        permgrant = permissionitem['permission_type']
        permsid = permissionitem['trustee']['id']
        permtype = permissionitem['permission']
        command = "isi smb shares permission create " + sharename
        command += " -d " + permgrant 
        command += " -p " + permtype 
        command += " --sid \"" + permsid + "\"" 
        print(command)

    for runasroot in i['run_as_root']:
        permsid = runasroot['id']
        command = "isi smb shares permission create " + sharename + " --run-as-root --sid \"" + permsid + "\""
        print(command)

    deleveryonecmd = "isi smb shares permission delete " + sharename + " --wellknown Everyone -f"
    print(deleveryonecmd)
    print("\n")
