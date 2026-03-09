#!/usr/bin/env python3
import pandas
import yaml

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
    create_vars_file('vars.yaml')


if __name__ == "__main__":
    main()
