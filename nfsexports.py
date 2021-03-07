#!/usr/bin/env python3

# python script to generate commands to create nfs mounts 
# on a new cluster from a source cluster
# where isi nfs exports list --format=json > nfsexports.json
# is used as the input

# current features tracked are:  
# clients, root clients, export description, read-only clients, read-write-clients

import json

with open('depot_nfs_exports.json') as nfsexports:
    nfs_export_data = json.load(nfsexports)


for i in nfs_export_data:
    if "paths" in i:

        # comma separated client list
        clients = ""
        if (len(i['clients']) == 0):
            # no clients listed
            pass
        else:
            for client in i['clients']:
                clients += client + ","
        # remove trailing comma
        if(clients):
            clients = " --clients " + clients[0:len(clients)-1]
        else: 
            clients = ""

        # comma separated root client list
        rootclients = ""
        if (len(i['root_clients']) == 0):
            # no clients
            pass
        else:
            for rootclient in i['root_clients']:
                rootclients += rootclient + ","
        # remove trailing comma
        if(rootclients): 
            rootclients = " --root-clients " + rootclients[0:len(rootclients)-1]
        else:
            rootclients = ""
        
        # comma separated read-write client list
        rwclients = ""
        if (len(i['read_write_clients']) == 0):
            # no read-write clients
            pass
        else:
            for rwclient in i['read_write_clients']:
                rwclients += rwclient + ","
        # remove trailing comma
        if(rwclients): 
            rwclients = " --read-write-clients " + rwclients[0:len(rwclients)-1]
        else:
            rwclients = ""

        # comma separated read-only client list
        roclients = ""
        if (len(i['read_only_clients']) == 0):
            # no read-only clients
            pass
        else:
            for roclient in i['read_only_clients']:
                roclients += roclient + ","
        # remove trailing comma
        if(roclients): 
            roclients = " --read-only-clients " + roclients[0:len(roclients)-1]
        else:
            roclients = ""

        # read only mount
        readonly = ""
        if (i['read_only'] == False):
            pass
        else:
            readonly = "--read-only yes"

        # export description
        description = ""
        if str(i['description']) == "":
            # no description data
            pass
        else:
            description = " --description \""+ str(i['description']) + "\""

        # put together the command per nfs export
        command = "isi nfs exports create "
        path = str(i['paths'][0])
        
        print(command + path + clients + rootclients + roclients + rwclients +
                description + readonly + "\n")


