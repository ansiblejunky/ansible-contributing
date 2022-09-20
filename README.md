# Ansible Contributing

Information on contributing to Ansible and related Collections, Roles, Modules and so on.

## Overview

General information can be found [here](https://docs.ansible.com/ansible/latest/dev_guide/index.html) for a Developer Guide.

Note the [Ansible Release Roadmaps](https://docs.ansible.com/ansible/devel/roadmap/) for Ansible if you are intending to fix a bug or add a feature or new module to a specific release.

## Development Environment

First, let's prepare our python development environment using `pyenv`:

```shell
# List latest available Python version
pyenv install --list | grep --extended-regexp "^\s*[0-9][0-9.]*[0-9]\s*$" | tail -1
# Install latest Python version
pyenv install --skip-existing $(pyenv install --list | grep --extended-regexp "^\s*[0-9][0-9.]*[0-9]\s*$" | tail -1)
# Create virtual environment for our ansible tools
pyenv virtualenv ansible-development
pyenv activate ansible-development
```

Next, follow [these steps](https://jarv.is/notes/how-to-pull-request-fork-github/) to **fork** the repo:

```shell
# Fork the via Github: https://github.com/ansible/ansible

# Clone the newly forked repo
git clone https://github.com/ansiblejunky/ansible
# Change to the repo directory
cd ansible
# List current remote configurations
git remote -v
# Add upstream remote configuration so repo will synch with original Ansible repo
git remote add upstream https://github.com/ansible/ansible.git
# List new remote configurations
git remote -v
# Synchronize the forked repo - https://help.github.com/en/github/collaborating-with-issues-and-pull-requests/syncing-a-fork
# Fetch the branches and their respective commits from the upstream repository
git fetch upstream
# Checkout the master branch
git checkout devel
# Install required python modules
pip install -r requirements.txt
# Run the environment setup script for each new dev shell process
. hacking/env-setup
```

Finally, let's prepare a folder for our testing.

```shell
# Create folder
mkdir testing && cd testing
# Create Vagrantfile
vagrant init centos/7
# Start the target machine
vagrant up
# Configure Ansible to connect to the Vagrant machine
(create ansible.cfg)
# Ensure Ansible can connect to the machine
ansible -i inventory all -m debug
```

If your module exists in a collection, you will need to **fork** that repo and clone it locally within the `collections` folder in the `testing` folder. You can find Ansible collections [here](https://github.com/ansible-collections)

```shell
# Fork the collection repo in Github. For example: https://github.com/ansible-collections/community.general

# Set the `collections_paths` setting in ansible.cfg
[defaults]
collections_paths = collections
# Create the collections folder
mkdir -p collections/ansible_collections/community/ && cd collections/ansible_collections/community/
# Clone the collection using only the last name
git clone https://github.com/ansible-collections/community.general.git general

```

## Changing existing modules, plugins, etc

Now we navigate to the module we want to work on:

```shell
# Modules
cd lib/ansible/modules/
# Plugins
cd lib/ansible/plugins/
```

## Conventions

Ansible conventions offer a predictable user interface across all modules, playbooks, and roles. To follow Ansible conventions in your module development:

[Following Ansible Conventions](https://docs.ansible.com/ansible/devel/dev_guide/developing_modules_best_practices.html)

## Modules

[Ansible module architecture](https://docs.ansible.com/ansible/latest/dev_guide/developing_program_flow_modules.html)

[Debugging modules](https://docs.ansible.com/ansible/latest/dev_guide/debugging.html)

## Resources

- [Developing plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html)
- [THE INSIDE PLAYBOOK - HOW TO EXTEND ANSIBLE THROUGH PLUGINS](https://www.ansible.com/blog/how-to-extend-ansible-through-plugins)
- [Inventory Plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html)
- [Testing Ansible](https://docs.ansible.com/ansible/latest/dev_guide/testing.html)
- [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html#contributing-code-features-or-bugfixes)
- [The Ansible Development Cycle](https://docs.ansible.com/ansible/latest/community/development_process.html)
