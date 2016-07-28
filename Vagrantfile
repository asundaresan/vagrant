# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

VAGRANTFILE_API_VERSION = "2"
vagrant_root = File.dirname(__FILE__)
config = YAML.load_file("#{vagrant_root}/vagrant_configuration.yaml")
NUM_MACHINES = config["num_machines"]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
  end
  if File.directory?(File.expand_path("~/projects")) 
    config.vm.synced_folder "~/projects", "/home/vagrant/projects"
  end
  if File.directory?(File.expand_path("~/github")) 
    config.vm.synced_folder "~/github", "/home/vagrant/github"
  end
  if Vagrant.has_plugin?("vagrant-timezone")
    config.timezone.value = :host
  end 

  (1..NUM_MACHINES).each do |machine_id|
    host_name = "machine#{machine_id}"
    config.vm.define "machine#{machine_id}" do |machine|
      machine.vm.hostname = host_name
      ip_addr = "192.168.1.#{200+machine_id}"
      machine.vm.network "private_network",  ip: ip_addr, bridge: [
        "wlan0",
        "eth0",
        "en0",
      ]
      # Only execute the ansible provisioner, when all machines are up and ready.
      config.vm.provision :ansible do |ansible|
        # Disable default limit to connect to all the machines
        ansible.limit = "machine#{machine_id}"
        ansible.playbook = "main.yaml"
        ansible.extra_vars = { 
          host_name: host_name,
          create_keys: "True",
          ip_address: ip_addr,
        }
      end
    end
  end
  (1..NUM_MACHINES).each do |machine_id|
    host_name = "machine#{machine_id}"
    config.vm.define "machine#{machine_id}" do |machine|
      machine.vm.provision :ansible do |ansible|
        # Disable default limit to connect to all the machines
        ansible.limit = "machine#{machine_id}"
        ansible.playbook = "post.yaml"
        ansible.extra_vars = { 
          host_name: host_name,
          create_config: "True",
        }
      end
    end
  end
end
