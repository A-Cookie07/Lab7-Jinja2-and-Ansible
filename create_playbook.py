#!/usr/bin/env python3
import os
import subprocess

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

    #create_tasks
    with open("./roles/router/tasks/main.yml", "w") as wptr:
        wptr.write("---\n")
        wptr.write("# tasks file for router\n")
        wptr.write('- name: Generate Config Files\n')
        #wptr.write('  template: src=router.j2 dest=./{{ item.hostname }}.txt') 
        wptr.write('  ansible.builtin.debug:\n')
        wptr.write('    msg: Hello {{ item.hostname }}\n')
        wptr.write('  with_items: "{{ routers }}"\n')

    return 0

    



if __name__ == "__main__":
    main()
