# Some cool D(D)oS tools that i have developed based on "bane"

<h2>Context:</h2>
<p>This repo contains sophisticated and advanced DDoS tools and botnets based on TOR. When allowing the attack to go through TOR's network using "bane" library, each request exits from random and different exit node ( = different IP for each request ) to mimic a large botnet thanks to its capabilities to reach more than 10k requests per second for some tools.</p>
<h2>DISCLAIMER</h2>
<p>This repo is intended exclusively for educational purposes and ethical use with the explicit permission from the people who this tool is used against. The author of this code expressly disclaims any responsibility for any misuse or improper application of this library. It is imperative to emphasize that the user, and the user alone, bears full accountability for their actions when utilizing this library. Any legal ramifications stemming from the misuse of this library are solely the responsibility of the user, and the author shall not be held liable for any such consequences. By utilizing this library, users are acknowledging their understanding and acceptance of these terms and conditions.</p>
<h2>installing Git:</h2>
<h4>for windows:</h4>
 download Git from <a href="https://git-scm.com/download/win">https://git-scm.com/download/win</a>
<h4>for linux:</h4>
<code>sudo apt-get update -y && sudo apt-get install git -y
</code>
<h4>for termux:</h4>
<code>apt update -y && apt install git -y
</code>

<h2>installing Tor:</h2>
<h4>for windows:</h4>
 download Tor Browser from <a href="https://www.torproject.org/download/">https://www.torproject.org/download/</a>. Then, open the browser and connect so you become connected to TOR's network as long as it is opened.
<h4>for linux:</h4>
<code>sudo apt-get update -y && sudo apt-get install tor -y
</code>
to run TOR service:<br>
<code>sudo service tor start
</code>
<h4>for termux:</h4>
<code>apt update -y && apt install tor -y
</code>
to run TOR service:<br>
<code>tor
</code>


<h2>cloning the repo:</h2>
<code>git clone https://github.com/AlaBouali/cool_ddos_tools
</code>
<code>cd cool_ddos_tools
</code>
<h2>installation:</h2>

<h4>for windows / termux :</h4>

<code>pip3 install -r requirements.txt
</code>
<h4>for linux:</h4>

<code>sudo pip3 install -r requirements.txt
</code>
<h2>Running the tools:</h2>
<h3>HTTP Flood tool: ( up to 10k requests per second from 1 machine ) </h3>
<code>python3 ./HTTP/http_flooder.py
</code>
<br>

<img src="https://github.com/AlaBouali/cool_ddos_tools/blob/main/screenshots/HTTP/tool_screenshot.png">
<img src="https://github.com/AlaBouali/cool_ddos_tools/blob/main/screenshots/HTTP/dstat_10k_2.png">
<img src="https://github.com/AlaBouali/cool_ddos_tools/blob/main/screenshots/HTTP/dstat_10k.png">
