# -*- mode: ruby -*-
# vi: set ft=ruby :

require 'yaml'

VAGRANTFILE_API_VERSION = "2"
vagrant_root = File.dirname(__FILE__)
config = YAML.load_file("#{vagrant_root}/vagrant_configuration.yaml")
config_memory = config["memory"]
config_cpus = config["cpus"]
config_box = config["box"]

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = config_box
  config.vm.provider "virtualbox" do |v|
    v.memory = config_memory
    v.cpus = config_cpus
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
  config.vm.define "machine1" do |machine|
    # Only execute the ansible provisioner, when all machines are up and ready.
    config.vm.provision :ansible do |ansible|
      ansible.limit = "all"
      ansible.playbook = "main.yaml"
    end
  end
end
