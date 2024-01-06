# Some cool D(D)oS tools that i have developed based on "bane"
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
<h3>HTTP spamming tool:</h3>
<code>python3 ./HTTP_Flooders/http_flooder.py
</code>