import http.server, socketserver, os, socket, re
from time import sleep
from zeroconf import ServiceInfo, Zeroconf, IPVersion
import logging

logging.basicConfig(filename='mdns_server.log', level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

mdns_logger = logging.getLogger(__name__)

# class MDNSServer:
#     def __init__(self):
#         self.services = {}

#     def register_service(self, name, desc, domain_mdns, local_ip, port):
#         """
#             Register a new mDNS service on the local network.
#         """
#         info = ServiceInfo(
#             "_http._tcp.local.",
#             name + "._http._tcp.local.",
#             addresses=[socket.inet_aton(local_ip)],
#             port=port,
#             properties=desc,
#             server=domain_mdns+'.',
#         )
#         self.services[name] = info
#         self.zeroconf.register_service(info)
#         logging.info("Service registered: %s", info)

#     def unregister_service(self, name):
#         """
#             Unregister a previously registered mDNS service.
#         """
#         info = self.services.pop(name, None)
#         if info is not None:
#             self.zeroconf.unregister_service(info)
#             logging.info("Service unregistered: %s", info)

#     def discover_services(self, domain_mdns):
#         """
#             Discover mDNS services on the local network.
#         """
#         discovered = {}
#         for name, info in self.services.items():
#             response = self.zeroconf.get_service_info(
#                 "_http._tcp.local.",
#                 name + "._http._tcp.local.")
#             if response is not None:
#                 discovered[name] = response
#         return discovered

#     def mdns_server(self, domain_mdns):
#         """
#             Generates a mDNS server which provides the local network with a Name Service.
#         """
#         self.zeroconf = Zeroconf(ip_version=IPVersion.V4Only)
#         logging.info("mDNS server started")

#         try:
#             while True:
#                 sleep(0.1)
#         except KeyboardInterrupt:
#             pass
#         finally:
#             for name in self.services.keys():
#                 self.unregister_service(name)
#             self.zeroconf.close()
#             logging.info("mDNS server stopped")


local_ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, socket.SOCK_DGRAM)]][0][1]]) if l][0][0]

class utils:
    """
        A collection of different functions and utilities that helps to organize the program.
    """
      
    def mdns_server(self, domain_mdns):
        """
            Generates a mDNS server which provides the local network with a Name Service.
        """
        desc = {'path': '/'}
        info = ServiceInfo(
            "_http._tcp.local.",
            "_http._tcp.local.",
            addresses=[socket.inet_aton(local_ip)],
            port=8008,
            properties=desc,
            server=domain_mdns+'.',
        )

        zeroconf = Zeroconf(ip_version=IPVersion.V4Only)
        zeroconf.register_service(info)
        logging.info("mDNS: Service registered: %s", info)
        try:
            while True:
                sleep(0.1)
        except KeyboardInterrupt:
            pass
        finally:
            zeroconf.unregister_service(info)
            logging.info("Service unregistered: %s", info)
            zeroconf.close()
    def get_friendlyname(self):
        data = open('./ssdp.xml').read()
        try:
            friendlyname = re.search("<friendlyName>(.*?)</friendlyName>",data).group(1)
        except (AttributeError):
            print("FriendlyName not found.")
        return(friendlyname)
    def get_manufacturer(self):
        data = open('./ssdp.xml').read()
        try:
            manufacturer = re.search("<manufacturer>(.*?)</manufacturer>",data).group(1)
        except (AttributeError):
            print("Manufacturer not found.")
        return(manufacturer)
    def get_model(self):
        data = open('./ssdp.xml').read()
        try:
            model = re.search("<modelName>(.*?)</modelName>",data).group(1)
        except (AttributeError):
            print("Model not found.")
        return(model)
    def get_url(self):
        data = open('./ssdp.xml').read()
        try:
            url = re.search("<presentationURL>(.*?)</presentationURL>",data).group(1)
        except (AttributeError):
            url = "http://"+local_ip+"/pages/login.html"
        return(url)
    def get_device(self):
        data = open('./ssdp.xml').read()
        try:
            device = re.search("<deviceType>(.*?)</deviceType>",data).group(1)
        except (AttributeError):
            print("Device type not found.")
        return(device)
    def get_service(self):
        data = open('./ssdp.xml').read()
        try:
            service = re.search("<serviceType>(.*?)</serviceType>",data).group(1)
        except (AttributeError):
            print("Service type not found.")
        return(service)
    def get_serviceid(self):
        data = open('./ssdp.xml').read()
        try:
            serviceid = re.search("<serviceId>(.*?)</serviceId>",data).group(1)
        except (AttributeError):
            print("Device type not found.")
        return(serviceid)
    def get_uuid(self):
        data = open('ssdp.xml').read()
        search = data.find("<UDN>")
        uuid = data[search+5:]
        UUID = uuid[0:36]
        return(UUID)
    def get_friendlyname_tmp(self):
        data = open('./tmp/ssdp.xml').read()
        try:
            friendlyname = re.search("<friendlyName>(.*?)</friendlyName>",data).group(1)
        except (AttributeError):
            print("FriendlyName not found.")
        return(friendlyname)
    def get_service_tmp(self):
        data = open('./tmp/ssdp.xml').read()
        try:
            service = re.search("<serviceType>(.*?)</serviceType>",data).group(1)
        except (AttributeError):
            print("Service type not found.")
        return(service)
    def get_service_number(self, service):
        service = int(service) * 4 - 1
        return(service)
    def get_domain(self):
        data = open('./ssdp.xml').read()
        try:
            domain = re.search("http://(.*?):",data).group(1)
        except (AttributeError):
            domain = ""
        return(domain)
