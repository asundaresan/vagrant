# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

VAGRANTFILE_API_VERSION = "2"
vagrant_root = File.dirname(__FILE__)
config = YAML.load_file("#{vagrant_root}/vagrant_configuration.yaml")
NUM_MACHINES = config["num_machines"]
IP_ADDR_PREFIX = "192.168.1"
IP_ADDR_SUFFIX = 201
IP_ADDR = "#{IP_ADDR_PREFIX}" + "." + "#{IP_ADDR_SUFFIX}"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
  end
  # link to projects folder
  if File.directory?(File.expand_path("~/projects")) 
    config.vm.synced_folder "~/projects", "/home/vagrant/projects"
  end
  # link to projects folder
  if File.directory?(File.expand_path("~/github")) 
    config.vm.synced_folder "~/github", "/home/vagrant/github"
  end
  # set remote timezone to match host
  if Vagrant.has_plugin?("vagrant-timezone")
    config.timezone.value = :host
  end 

  # create security.yaml configuration which is a simple map: { hostname: ip_address }
  config.vm.provision :host_shell do |host_shell|
    host_shell.inline = "python roles/racoon/scripts/configure_security.py -N #{NUM_MACHINES} -I #{IP_ADDR} -H machine -o config/security.yaml"
  end 

  (1..NUM_MACHINES).each do |machine_id|
    hostname = "machine#{machine_id}"
    config.vm.define "machine#{machine_id}" do |machine|
      machine.vm.hostname = hostname
      ip_addr = "192.168.1.#{IP_ADDR_SUFFIX+machine_id-1}"
      machine.vm.network "private_network",  ip: ip_addr, bridge: [ "wlan0", "eth0", "en0" ]
      # Only execute the ansible provisioner, when all machines are up and ready.
      if machine_id == NUM_MACHINES
        #config.vm.provision :ansible do |ansible|
        #  ansible.limit = "all"
        #  ansible.playbook = "main.yaml"
        #end
        config.vm.provision :ansible do |ansible|
          # Disable default limit to connect to all the machines
          ansible.limit = "all"
          ansible.playbook = "create_racoon_key.yaml"
        end
        machine.vm.provision :ansible do |ansible|
          # Disable default limit to connect to all the machines
          ansible.limit = "all"
          ansible.playbook = "create_racoon_conf.yaml"
        end
      end
    end
  end
end
