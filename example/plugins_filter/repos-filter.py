from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

from ansible.errors import AnsibleError, AnsibleFilterError

import json

def to_repos(repolist):
    lines = repolist.split('\n')

    current_repo = dict()
    test_dict = list()

    for line in lines:
        if line.find('Repo-') != 0 or line.strip() == '': continue;

        k, v = line.split(":", 1)
        k = k.strip()
        _, key = k.split("-")
        v = v.strip()

        if key == "id":
            current_repo = dict()
            test_dict.append(current_repo)
            vid, _ = v.split("/", 1)
            current_repo[key] = vid
        elif key == "filename":
            _, f = v.rsplit("/", 1)
            fshort, _ = f.rsplit(".", 1)
            current_repo[key] = fshort
        else:
            current_repo[key] = v
        
    return json.dumps(test_dict, indent=4, sort_keys=True)


class FilterModule(object):
    ''' filter '''

    def filters(self):
        return {
            'to_repos': to_repos
        }
