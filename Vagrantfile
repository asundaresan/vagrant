# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
vagrant_root = File.dirname(__FILE__)

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|
  config.vm.box = "ubuntu/trusty64"
  config.vm.provider "virtualbox" do |v|
    v.memory = 1024
    v.cpus = 1
  end

  #config.vm.synced_folder git_root, "/opt/sros"
  #master_ip_addr = "192.168.1.201"
  #config.vm.provision :host_shell do |host_shell|
  #  host_shell.inline = "python scripts/config_ipsec.py -N #{N} -I #{master_ip_addr} -H machine"
  #  #host_shell.name = "Configure ipsec.yml: N=#{N}"
  #end
  #config.vm.provision :host_shell do |host_shell|
  #  host_shell.inline = "python scripts/make_ipsec_config.py"
  #  #host_shell.name = "Create IPSec configuruation files and keys"
  #end

	host_name = "test"
	config.vm.define "machine1" do |machine|
		if Vagrant.has_plugin?("vagrant-timezone")
			config.timezone.value = :host
		end 
		machine.vm.hostname = host_name
		# Only execute once the Ansible provisioner,
		# when all the machines are up and ready.
		machine.vm.provision :ansible do |ansible|
			# Disable default limit to connect to all the machines
			ansible.limit = "machine1"
			ansible.playbook = "main.yaml"
			ansible.extra_vars = { 
				files_root: vagrant_root,
				host_name: host_name,
				time_zone: config.timezone.value
			}
		end
	end
end
