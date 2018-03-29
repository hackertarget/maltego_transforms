A local transform for Maltego which makes use of the [HackerTarget API](https://hackertarget.com/ip-tools/) for DNS Recon

![Maltego Transform](https://hackertarget.com/images/maltego-hackertarget.gif)

Installation
------------
1. This transform was developed and tested with Python 2.7 on Ubuntu Linux. You need python and the requests module.
2. Download and install community or commercial version of [Maltego](https://www.paterva.com/web6/products/download.php).

Configuration
-------------
1. Clone this repository to a local directory (known as the 'working directory' in Maltego).
2. For the configuration file to work out of the box, move **maltego_transforms** to **/opt/Maltego_HackerTarget**. If paths are different you can update from the manage transform screen.
3. Obtain an [HackerTarget API Key](https://hackertarget.com/scan-membership/) API key. Free users get 200 requests per day against the API (no key required).
4. Place the API key in the APIKEY variable in each transform.
5. Import HackerTarget-config-v1.mtz as a Maltego configuration file
6. Set the working directory of each transform (which should be set to /opt/Maltego_HackerTarget by default) to the working directory from step 1.
7. Ensure each transform has the proper Python path.

Tips
----
- The transforms work on Domain, NS Server and IP address entities only. You may need to resolve a DNSName entity to a domain before running the find hosts transform. Resolve the Domain to NS Server to run the DNSseach.
- Depending on your Maltego license you will be restricted by the number of entities returned by the transforms. The find hosts can return thousands of entries on the right query. 
