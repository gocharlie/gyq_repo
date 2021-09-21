from netmiko import ConnectHandler
from netaddr import IPNetwork,cidr_merge


def iosg_router01():
    router01 = {
        'device_type': 'cisco_ios',
        'ip': '10.81.3.51',
        'username': 'admin',
        'password': 'admin'
    }
    return router01

def parse_device(**kwargs):
    with ConnectHandler(**kwargs) as connect:
        connect.send_command('terminal length 0')
        output = connect.send_command('show ip bgp',use_textfsm=True)
        connect.send_command('terminal length 10')
        return output

def strip_routes(routes):
    route_list = []
    for route in routes:
        if route.get('network') == '0.0.0.0':
            continue
        route = route.get('network') 
        route_list.append(IPNetwork(route))
    return route_list

if __name__ == "__main__":
    R1 = iosg_router01()
    router = parse_device(**R1)
    print(strip_routes(router))
    # sr = strip_routes(router)
    # print(cidr_merge(sr))
