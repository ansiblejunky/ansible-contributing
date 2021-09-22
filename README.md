# Ansible - Development

Information on developing Ansible modules, plugins and much more.

## Overview

Note the release schedule for Ansible if you are intending to fix a bug or add a feature or new module to a specific Ansible version. [Ansible Release Roadmaps](https://docs.ansible.com/ansible/devel/roadmap/)

For general help, use this guide: [Ansible - Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)

For shorter information use this [guide](https://tannerjc.net/wiki/index.php?title=Ansible_Developer_Filament) from tannerjc.

## Development Environment

First, let's prepare our python development environment. Using `pyenv`:

```shell
# List available Python versions
pyenv install --list | grep 3.8
# Install latest Python version
pyenv install 3.8.2
# Create virtual environment for your Ansible development
pyenv 
```

Next, let's **fork** the Ansible project:

```shell
# Fork the Ansible repo via Github: https://github.com/ansible/ansible

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

## Plugins

[Internal - Presentation by Edward Quail](https://mojo.redhat.com/docs/DOC-1168516)

[Developing plugins](https://docs.ansible.com/ansible/latest/dev_guide/developing_plugins.html)
[THE INSIDE PLAYBOOK - HOW TO EXTEND ANSIBLE THROUGH PLUGINS](https://www.ansible.com/blog/how-to-extend-ansible-through-plugins)

## Dynamic inventory

[Developing dynamic inventory](https://docs.ansible.com/ansible/latest/dev_guide/developing_inventory.html)

## Testing

[Testing Ansible](https://docs.ansible.com/ansible/latest/dev_guide/testing.html)

## Resources

The purpose of this guide is to teach you everything you need to know about being a contributing member of the Ansible community. All types of contributions are welcome, and necessary to Ansible’s continued success.
[Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html#contributing-code-features-or-bugfixes)

[Embedding and extending Ansible with Python](http://slides.com/alejandroguiraorodriguez/ee-ansible-with-python#/36)

[The Ansible Development Cycle](https://docs.ansible.com/ansible/latest/community/development_process.html)

[Internal - Ansible Module Development: a narrative](https://docs.google.com/document/d/11Ai1KrfNtl9_3yQOSJbqUpVR7G6ANuG1Igr3s6zlj1k/edit#heading=h.tt7bcolhsrid)
