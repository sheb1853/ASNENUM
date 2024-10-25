# ASNENUM
ASNENUM is a Python-based tool that allows users to enumerate Autonomous System Numbers (ASNs) and the associated IP address ranges for a given organization. This tool helps in gathering valuable reconnaissance information, especially useful during Red Team assessments.

## Why Enumerating ASN is Important in Red Team Assessments?

ASNs provide valuable insights into the infrastructure of a target organization. By identifying the ASNs associated with an organization, a Red Team can map out the entire range of IP addresses owned or managed by that organization. This allows attackers to:

* Identify potential attack surfaces.
* Focus network reconnaissance efforts on the identified subnets.
* Correlate infrastructure details across different environments, such as cloud and on-premise systems.

Mapping ASNs and their associated IP addresses helps in efficient footprinting, network scanning, and identifying publicly exposed systems that could be targeted for further exploitation.

## Features
* Fetches all ASNs associated with an organization.
* Retrieves IP address ranges associated with each ASN.
* Displays the results in a well-structured table format.

## Usage
```
python3 asnnum.py -o <organization_name>

```
## Installation

* Clone the repository:
```
git clone https://github.com/sheb1853/asnenum.git
cd asnenum
```
* Install the dependencies:
```
pip install -r requirements.txt
```
* Run the tool:
```
python3 asnenum.py -o <organization_name>

```
## Sample Output
```
$ python3 asnenum.py -o example.com

 AAAAA   SSSSSS  N   N  EEEEE  N   N  U   U  M   M 
A     A  S       NN  N  E      NN  N  U   U  MM MM 
AAAAAAA  SSSSS   N N N  EEEEE  N N N  U   U  M M M 
A     A       S  N  NN  E      N  NN  U   U  M   M 
A     A  SSSSSS  N   N  EEEEE  N   N   UUU   M   M 

                               
       by Timothians Shebin Mathew


ASN and IP Ranges for Organization: example.com

ASN: AS12345
+-------+---------------+
|  ASN  | IP Addresses   |
+-------+---------------+
| AS12345 | 192.0.2.0/24 |
| AS12345 | 198.51.100.0/24 |
+-------+---------------+
```

#Enumeration #ASN #Red Team #pentest #Cyber security
