# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

VAGRANTFILE_API_VERSION = "2"
vagrant_root = File.dirname(__FILE__)
# read configuration from file
conf = YAML.load_file("#{vagrant_root}/vagrant_configuration.yaml")
conf_memory = conf["memory"]
conf_cpus = conf["cpus"]
conf_hostname = conf["hostname"]
conf_name = conf["name"]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.hostname = conf_hostname
  config.vm.provider "virtualbox" do |v|
    v.memory = conf_memory
    v.cpus = conf_cpus
    v.name = conf_name
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

  hostname = "quirm"
  # Only execute the ansible provisioner, when all machines are up and ready.
  config.vm.provision :ansible do |ansible|
    ansible.limit = "all"
    ansible.playbook = "main.yaml"
  end
end
