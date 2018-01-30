#!/usr/bin/env python3

import getpass
import requests
import getopt
import sys

"""
FunPDBe Deposition Client
Created on 16th January 2018
Author: Mihaly Varadi
"""


class User(object):
    """
    User object to handle prompts if no user name
    or password were provided when running the Client()
    """

    def __init__(self, user=None, pwd=None):
        self.user_name = user
        self.user_pwd = pwd
        if not self.user_name:
            while not self.user_name:
                self.user_name = self.set_user()
        if not self.user_pwd:
            while not self.user_pwd:
                self.user_pwd = self.set_pwd()

    @staticmethod
    def set_user():
        return input("funpdbe user name: ")

    @staticmethod
    def set_pwd():
        return getpass.getpass("funpdbe password: ")


class Api(object):

    def __init__(self):
        # TODO
        self.url_base = "http://127.0.0.1:8000/funpdbe_deposition"
        self.entries_url = "%s/entries/" % self.url_base


class Client(object):

    def __init__(self, user=None, pwd=None):
        self.welcome()
        self.user = User(user, pwd)
        self.api = Api()

    def welcome(self):
        print("\n####################################\n")
        print("Welcome to FunPDBe deposition client\n")
        print("####################################\n")

    def get_one(self, pdb_id, resource=None):
        url = self.api.entries_url
        if resource:
            url += "resource/%s/" % resource
        else:
            url += "pdb/"
        url += "%s/" % pdb_id
        r = requests.get(url, auth=(self.user.user_name, self.user.user_pwd))
        print(r.text)

    def get_all(self, resource=None):
        url = self.api.entries_url
        if resource:
            url += "resource/%s/" % resource
        r = requests.get(url, auth=(self.user.user_name, self.user.user_pwd))
        print(r.text)

    def post_one(self, json_data):
        pass

    def delete_one(self, pdb_id):
        url = '%spdb/%s' % (self.api.entries_url, pdb_id)
        r = requests.delete(url, auth=(self.user.user_name, self.user.user_pwd))
        print(r.text)


def main():
    user = None
    pwd = None
    mode = None
    pdbid = None
    resource = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "u:p:m:i:r:h", [
            "user=",
            "pwd=",
            "mode=",
            "pdbid=",
            "resource=",
            "help"])
    except getopt.GetoptError as err:
        print("Error: %s" % err)
        sys.exit(2)
    for option, value in opts:
        if option in ["-u", "--user"]:
            user = value
        elif option in ["-p", "--pwd"]:
            pwd = value
        elif option in ["-m", "--mode"]:
            if value in ("get", "post", "delete"):
                mode = value
        elif option in ["-i", "--pdbid"]:
            pdbid = value
        elif option in ["-r", "--resource"]:
            resource = value
        elif option in ["-h", "--help"]:
            # TODO
            pass
        else:
            assert False, "unhandled option"

    c = Client(user=user, pwd=pwd)
    if mode == "get":
        if pdbid:
            c.get_one(pdbid, resource)
        else:
            c.get_all(resource)
    elif mode == "delete":
        if not pdbid:
            while not pdbid:
                pdbid = input("pdb id to delete: ")
        c.delete_one(pdbid)


if __name__ == "__main__":
    main()
