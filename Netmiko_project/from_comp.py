

net_connect.send_command(str(cmd), strip_command=False, strip_prompt=False, expect_string="\?\s*")
if "Delete" in output or "Confirm" in output:
    output += net_connect.send_command_timing(
        "\n", strip_command=False, strip_prompt=False, delay_factor=1
    )

# !/usr/bin/python

import netmiko


def netmiko_connect(device_ip):
    # tacacs_username = "DSV.API"
    tacacs_username = "lab"
    # tacacs_password = "bale-pE3WFx!"
    tacacs_password = "cisco123"
    device_type = "cisco_ios"
    connect = {
        'device_type': 'cisco_ios',
        'host': device_ip,
        'username': tacacs_username,
        'password': tacacs_password
    }

    net_connect = ConnectHandler(**connect)
    net_connect.send_command("enable", strip_command=False, strip_prompt=False, expect_string="Password:")
    net_connect.send_command_timing("cisco123\n", strip_command=False, strip_prompt=False, delay_factor=1)
    # print(net_connect)

    return net_connect


def get_all_bins_recursively(device_ip, nmiko_connection):
    # print(nmiko_connection.find_prompt())     # IOS prompt
    cmd_dir_flash = nmiko_connection.send_command_timing("dir /recursive flash: | i bim|Directory",
                                                         delay_factor=2).split("\n")
    temporary_list = []
    files_with_paths_list = []
    for line_cmd_dir_output in cmd_dir_flash:
        if '.bim' in line_cmd_dir_output \
                and 'Directory' in (cmd_dir_flash[cmd_dir_flash.index(line_cmd_dir_output) - 1]):
            str_for_regex = (cmd_dir_flash[cmd_dir_flash.index(line_cmd_dir_output) - 1])
            filder_path = re.search("\S*$", str_for_regex)
            temporary_list.append(filder_path.group(0))
    dirs_with_bins = list(dict.fromkeys(temporary_list))
    temporary_list = []
    for line_cmd_dir_bin in dirs_with_bins:
        cmd_dir_bin = 'dir ' + line_cmd_dir_bin + ' | i bim'
        cmd_dir_flash = nmiko_connection.send_command_timing(cmd_dir_bin, delay_factor=2).split("\n")
        for line in cmd_dir_flash:
            # print(line_cmd_dir_bin)
            # print(line)
            file_name_for_regex = re.search("\S*$", line)
            files_with_paths_list.append(line_cmd_dir_bin + file_name_for_regex.group(0))
    return files_with_paths_list


def clean_all_but_running(show_version):
    for delete_file in files_to_delete:
        if show_version not in delete_file:
            print('delete ', delete_file)
        else:
            print('Not deleting', delete_file)
            print('Because show version is:', show_version)


files_to_delete = get_all_bins_recursively(str(sys.argv[1]), netmiko_connect)
clean_all_but_running(str(sys.argv[2]))