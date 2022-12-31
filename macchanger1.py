import subprocess
import random

def change_mac_address(interface):
  # Generate a random MAC address
  new_mac_address = generate_mac_address()

  # Use the `ip link` command to change the MAC address of the interface
  subprocess.run(["ip", "link", "set", "dev", interface, "address", new_mac_address])

def generate_mac_address():
  mac_address = []
  for i in range(6):
    octet = random.randint(0, 255)
    mac_address.append(octet)
  return ":".join(["{:02x}".format(octet) for octet in mac_address])

# Change the MAC address of interface "eth0"
change_mac_address("ens33")
