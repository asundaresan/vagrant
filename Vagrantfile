# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

VAGRANTFILE_API_VERSION = "2"
vagrant_root = File.dirname(__FILE__)
# read configuration from file
conf = YAML.load_file("#{vagrant_root}/config.yaml")
conf_memory = conf["memory"]
conf_cpus = conf["cpus"]
conf_hostname = conf["hostname"]
conf_name = conf["name"]
conf_box = conf["box"]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.hostname = conf_hostname
  config.vm.box = conf_box
  config.vm.provider "virtualbox" do |v|
    v.memory = conf_memory
    v.cpus = conf_cpus
    v.name = conf_name
    # add this to fix bug for 16.04
    v.customize ["modifyvm", :id, "--cableconnected1", "on"]
  end
  # link to projects folder
  if File.directory?(File.expand_path("~/projects")) 
    config.vm.synced_folder "~/projects", "/home/vagrant/projects"
  end
  # link to projects folder
  if File.directory?(File.expand_path("~")) 
    config.vm.synced_folder "~", "/home/vagrant/host"
  end
  # set remote timezone to match host
  if Vagrant.has_plugin?("vagrant-timezone")
    config.timezone.value = :host
  end 

  # Only execute the ansible provisioner, when all machines are up and ready.
  config.vm.provision :ansible do |ansible|
    ansible.limit = "all"
    ansible.playbook = "main.yaml"
  end
end
