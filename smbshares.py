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

    
    command = "isi smb shares create"
    path = str(i['path'])
    description = str(i['description'])
    sharename = str(i['name'])

    print(command, sharename, path," --description \"" + description + "\"") 

    for permissionitem in i['permissions']:
        permgrant = permissionitem['permission_type']
        permsid = permissionitem['trustee']['id']
        permtype = permissionitem['permission']
        command = "isi smb shares permission create " + sharename + " -d " + permgrant + " -p " + permtype + " --sid \"" + permsid + "\""
        print(command)
    print("\n")
