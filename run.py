#!/usr/bin/env python
# ~*~ coding: utf-8 ~*~

import argparse
from rsapi import RsAPI


def ParseArgs():
    parser = argparse.ArgumentParser(
                            description="Rackspace API tool",
                            prog="CLI API Tool"
                                    )
    parser.add_argument('--username', '-u',
                        help="Account's username",
                        required=True,
                       )
    parser.add_argument('--api-key', '-k',
                        help="Account's API key",
                        required=True,
                       )
    parser.add_argument('--name', '-n',
                        help="Server or Cluser name",
                       )
    parser.add_argument('--web-nodes', '-wn',
                        help="Number of webnodes, OS and Size",
                        nargs=3,
                       )
    parser.add_argument('--mysql-nodes', '-mn',
                        help="Number of webnodes, OS and Size",
                        nargs=3,
                       )
    parser.add_argument('--cloud-files-list', '-cfl',
                        help="List CloudFiles Containers",
                        action="store_true",
                       )
    return parser.parse_args()

api = RsAPI()

args = ParseArgs()

api.getAuthentication(args.username, args.api_key)

if args.cloud_files_list:
    print 'hi'
    print api.getCloudFilesContainers()
