# Vagrant example with ansible provisioners

This will fire up an Ubuntu VirtualBox VM. 

You will need to edit main.yaml to select or deselect different roles as follows.

```
---
- name: Install and configure all components
  hosts: all
  become: yes
  become_method: sudo
  roles: 
  - base
  - timezone
  - ntp
  - ros 
```

The roles are git sub-modules. You can add more sub-modules as follows.

```
git submodule add https://github.com/asundaresan/ansible-role-timezone.git roles/timezone
```
