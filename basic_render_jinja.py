#!/usr/bin/env python3
import jinja2

def main():
    test_item = {
        'address00': "10.0.0.1 255.255.255.0",
        'if0ospfarea': '0',
        'if0processid': '1',
        'if0ospfarea': '0',
        'address10': "10.0.1.1 255.255.255.0",
        'address20': "10.0.2.1 255.255.255.0",
        'addresslo': "25.25.25.25 255.255.255.255"
    }

    print("This is working!")
    templateLoader = jinja2.FileSystemLoader(searchpath="./")
    templateEnv = jinja2.Environment(loader=templateLoader)
    TEMPLATE_FILE = "router_template.j2"
    template = templateEnv.get_template(TEMPLATE_FILE)
    print(template.render(item=test_item))

if __name__ == "__main__":
    main()
