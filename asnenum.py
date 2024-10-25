import requests
import re
import argparse
from prettytable import PrettyTable
from termcolor import colored


# Banner
BANNER = """

 AAAAA   SSSSSS  N   N  EEEEE  N   N  U   U  M   M 
A     A  S       NN  N  E      NN  N  U   U  MM MM 
AAAAAAA  SSSSS   N N N  EEEEE  N N N  U   U  M M M 
A     A       S  N  NN  E      N  NN  U   U  M   M 
A     A  SSSSSS  N   N  EEEEE  N   N   UUU   M   M 

                               
       by Timothians Shebin Mathew


"""

def get_asns_for_org(org_name):
    """Fetch all ASNs associated with an organization from bgp.he.net."""
    url = f"https://bgp.he.net/search?search%5Bsearch%5D={org_name}&commit=Search"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extract ASNs using regex
        asns = re.findall(r"AS\d+", response.text)
        if asns:
            return list(set(asns))  # Return unique ASNs
        else:
            print(f"[INFO]: No ASNs found for organization '{org_name}'.")
            return []
    else:
        print(f"[ERROR]: Failed to fetch ASNs for organization '{org_name}'.")
        return []

def get_ip_ranges_for_asn(asn):
    """Fetch all IP ranges associated with a specific ASN from bgp.he.net."""
    url = f"https://bgp.he.net/{asn}#_prefixes"
    response = requests.get(url)
    
    if response.status_code == 200:
        # Extract IP ranges using regex
        ip_ranges = re.findall(r"\d{1,3}(?:\.\d{1,3}){3}/\d+", response.text)
        return ip_ranges
    else:
        print(f"[ERROR]: Failed to fetch IP ranges for ASN '{asn}'.")
        return []

def display_asn_and_ip_ranges(org_name):
    """Display all ASNs and IP ranges associated with an organization."""
    asns = get_asns_for_org(org_name)
    
    if asns:
        print(f"\n{colored('ASN and IP Ranges for Organization:', 'cyan')} {colored(org_name, 'yellow')}\n")
        
        for asn in asns:
            # Print the ASN number first
            print(colored(f"ASN: {asn}", "green"))

            # Create a table for each ASN and its IP ranges
            table = PrettyTable()
            table.field_names = [colored("ASN", "green"), colored("IP Addresses", "blue")]

            # Fetch the IP ranges for the ASN
            ip_ranges = get_ip_ranges_for_asn(asn)
            
            if ip_ranges:
                for ip in ip_ranges:
                    table.add_row([asn, ip])
            else:
                table.add_row([asn, colored("No IP ranges found", "red")])
            
            print(table)
    else:
        print(f"{colored('[INFO]:', 'yellow')} No ASNs found for organization '{org_name}'.")

def main():
    print(BANNER)  # Display banner
    parser = argparse.ArgumentParser(description="ASN and IP Range Finder for an Organization")
    parser.add_argument("-o", "--org", help="Organization name to find ASNs and IP ranges for.", required=True)
    args = parser.parse_args()

    org_name = args.org
    display_asn_and_ip_ranges(org_name)

if __name__ == "__main__":
    main()

