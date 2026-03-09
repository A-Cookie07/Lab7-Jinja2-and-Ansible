#!/usr/bin/env python3
import os
import subprocess
import pandas
import yaml
import shutil

def create_directory(dir_name):
    try:
        os.mkdir(dir_name)
        print(f"created directory: {dir_name}")
    except FileExistsError:
        print(f"directory: {dir_name} already exists")
    except PermissionError:
        print(f"Permission denied, unable to create directory: {dir_name}")
    except Exception as e:
        print(f"ERROR: {e}")

def create_main_play():
    main_playbook = input("enter name of main overall playbook (ex: site.yaml)\n")
    with open(main_playbook, "w") as wptr:
        HOSTS='localhost' #I am setting this statically because we are really gonna only want to create
                          # The config files on this controlling machine
        wptr.write("- name: Generate Router Configuration Files\n")
        wptr.write(f"  hosts: {HOSTS}\n\n")
        wptr.write("  roles:\n")
        wptr.write("  - router")

def create_vars_file(filename):
    router = {}

    csvfile = pandas.read_csv("router_info.csv")
    data = csvfile.groupby("Hostname")
    for host, interface_list in data:
        new_list = interface_list.drop(columns=['Hostname']).to_dict(orient="records")
        router[host] = new_list
    
    with open(filename, 'w') as wptr:
        yaml.dump(router, wptr)
    
    return 0

def main():
    #print("This is working!")
    ##Create necessary roles files structure
    create_directory('roles')
    #create_directory('./roles/router')
    #create_directory('./roles/router/tasks')
    #create_directory('./roles/router/templates')
    #create_directory('./roles/router/vars')
    os.chdir("./roles/")
    os.system("ansible-galaxy init router")
    os.chdir("../")
    
    create_main_play()

    create_vars_file("./roles/router/vars/main.yml")

    #create_tasks
    with open("./roles/router/tasks/main.yml", "w") as wptr:
        tasks = '''---
# tasks file for router
- name: Generate Config Files
  ansible.builtin.debug:
    msg: Hello

- name: Create Conf Files
  template:
    src: router_template.j2
    dest: "./{{ item }}.txt"
  vars:
    hostname: "{{ item }}"
  loop:
    - "R1"
    - "R2"
    - "R3"
'''
        wptr.write(tasks)

    shutil.copyfile('./router_template.j2', './roles/router/templates/router_template.j2')


    return 0

    



if __name__ == "__main__":
    main()
