# yum_repository

https://docs.ansible.com/ansible/latest/collections/ansible/builtin/yum_repository_module.html

Bug - yum_repository shouldn't require baseurl/metalink/mirrorlist to disable a repository
https://github.com/ansible/ansible/issues/41178

yum_repository.py should be improved
- use module `find` to get all repo files in `/etc/yum.repos.d/`
- use module `file` to remove these files if `name: '*'`
- perhaps use python `configparser` to remove specific repos in a repo file; https://docs.python.org/2/library/configparser.html