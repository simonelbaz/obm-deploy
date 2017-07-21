class FilterModule(object):
    ''' Custom filter getting host IP corresponding to network passed as argument'''

    def filters(self):
        ''' FilterModule objects return a dict mapping filter names to
        filter functions. '''
        return {
                'get_ip': self.get_ip,
                }

    def get_ip(self, host, network):
        if "ansible_default_ipv4" in host and host["ansible_default_ipv4"]["network"] == network:
            return host["ansible_default_ipv4"]["address"]
        if "ansible_interfaces" in host:
            for iface in host["ansible_interfaces"]:
                if host["ansible_" + iface]['ipv4']["network"] == network:
                    return host["ansible_" + iface]['ipv4']["address"]

