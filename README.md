# ipscanner

<h2>Python Network Scanner</h2>  

This is a simple Python application that functions as an <b>ARP Network Scanner</b>. It's designed to discover all active devices (hosts) on the local network by mapping their <b>IP addresses</b> and corresponding <b>MAC addresses</b>.

<b>Core Functionality</b>

<li><b>Determine Network Range:</b> The script uses the <code>socket</code> module to find the local machine's IP address. It then derives the network range (using the <code>/24</code> subnet) to scan (e.g., <code>192.168.1.0/24</code>).</li>

<li><b>ARP Requests:</b> Utilizing the <code>scapy</code> library, it sends an <b>ARP request</b> broadcast packet to all IP addresses within the defined network.</li>

<li><b>Device Identification:</b> Devices that respond to the ARP request are identified. The script parses the responses to present a clear list of the <b>IP addresses</b> and their corresponding <b>hardware (MAC) addresses.</b><br><br></li>

<b>Requirements</b>

This script requires the <b>Scapy</b> library, a powerful interactive packet manipulation tool.<br><br>
<b>Bash</b>

<code>pip install scapy</code>

<b>Usage</b>

Execute the script using Python 3. (Administrator privileges/root access may be required, depending on your operating system, to send raw packets.)

<b>Bash</b><br><br><code>sudo python3 ipscan.py</code><br><br>

<b>Example Output</b><br>
<code>
Client IP address: 192.168.1.10
192.168.1.0/24
IPADRES             MAC

192.168.1.1         aa:bb:cc:dd:ee:ff
192.168.1.10        00:11:22:33:44:55
192.168.1.15        ff:ee:dd:cc:bb:aa
...
</code>

<b>Important Note on MAC Addresses (Privacy Feature)</b>

It's crucial to understand that on many modern devices, especially <b>mobile phones and tablets</b>, the displayed MAC address may not be the device's actual, permanent hardware address.
<li><b>MAC Address Randomization:</b> To enhance user privacy and prevent tracking across different Wi-Fi networks, these devices often use a <b>randomized or "spoofed" MAC address</b> when connecting to a new access point.</li><li><b>Impact on Scanning:</b> This means the MAC address reported by this scanner for a mobile device might be <b>different</b> from the device's true factory MAC address and may even change over time or when reconnecting. This is a normal security feature and not an error in the scan.</li>
