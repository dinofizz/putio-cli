#!/usr/bin/env python

import argparse
from putio import putio


if __name__=="__main__":
    parser = argparse.ArgumentParser(description='putiohelper')
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-L', '--list-root', help='List files and folders in the root directory', action='store_true', required=False)
    group.add_argument('-l', '--list-item', help='List files and folders in the given directory', required=False)
    group.add_argument('-d', '--download-link', help='Get the download link for the given file.', required=False)
    args = parser.parse_args()

    OAUTH_TOKEN = "" 

    client = putio.Client(OAUTH_TOKEN)

    #trek = files[3]

    #download_link = trek.get_link()

    #print download_link

    
    if args.list_root:
        print "listing root"
        files = client.File.list()
        for file in files:
            print str(file.id) + " : " + file.name
    elif args.list_item:
        item = client.File.get(int(args.list_item))
        print "[" + str(item.id) + " : " + item.name + "]"

        if item.content_type == 'application/x-directory':
            items = item.dir()
            for sub_item in items:
                print str(sub_item.id) + " : " + sub_item.name
    elif args.download_link:
        item = client.File.get(int(args.download_link))
        if item.content_type != 'application/x-directory':
            print item.get_link()
