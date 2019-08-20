#Showing us type of suppoted devices

#!/usr/bin/env python
from netmiko import Netmiko
from credentials import password1, username1
cisco1 = {
    "host": "10.223.244.86",
    "username": username1,
    "password": password1,
    "device_type": "cisco_ios",
}

net_connect = Netmiko(**cisco1)
print(net_connect.find_prompt())
net_connect.disconnect()

# Interestiing thing, using juniper I was able to connect to Cisco

# ValueError: Unsupported device_type: currently supported platforms are:
# a10
# accedian
# alcatel_aos
# alcatel_sros
# apresia_aeos
# arista_eos
# aruba_os
# avaya_ers
# avaya_vsp
# brocade_fastiron
# brocade_netiron
# brocade_nos
# brocade_vdx
# brocade_vyos
# calix_b6
# checkpoint_gaia
# ciena_saos
# cisco_asa
# cisco_ios
# cisco_nxos
# cisco_s300
# cisco_tp
# cisco_wlc
# cisco_xe
# cisco_xr
# cloudgenix_ion
# coriant
# dell_dnos9
# dell_force10
# dell_isilon
# dell_os10
# dell_os6
# dell_os9
# dell_powerconnect
# eltex
# endace
# enterasys
# extreme
# extreme_ers
# extreme_exos
# extreme_netiron
# extreme_nos
# extreme_slx
# extreme_vdx
# extreme_vsp
# extreme_wing
# f5_linux
# f5_ltm
# f5_tmsh
# flexvnf
# fortinet
# generic_termserver
# hp_comware
# hp_procurve
# huawei
# huawei_vrpv8
# ipinfusion_ocnos
# juniper
# juniper_junos
# linux
# mellanox
# mellanox_mlnxos
# mikrotik_routeros
# mikrotik_switchos
# mrv_lx
# mrv_optiswitch
# netapp_cdot
# netscaler
# oneaccess_oneos
# ovs_linux
# paloalto_panos
# pluribus
# quanta_mesh
# rad_etx
# ruckus_fastiron
# ubiquiti_edge
# ubiquiti_edgeswitch
# vyatta_vyos
# vyos