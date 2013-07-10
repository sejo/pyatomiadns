from pyatomiadns.client import AtomiaClient

# TODO: add vagrant setup and create real testcase
# this is how I setup my vagrant and prepare for testing
#repo="$(wget -q -O - http://public.apt.atomia.com/setup.sh.shtml | sed s/%distcode/`lsb_release -c | awk '{ print $2 }'`/g)"; echo "$repo"
#echo "$repo" | sh
#apt-get install atomiadns-masterserver atomiadns-client
#apt-get install vim
#apt-get install rng-tools
#apt-get install atomiadns-webapp
#apt-get install atomiadns-powerdns-database
#wget http://powerdnssec.org/downloads/packages/pdns-static_3.2-rc4-1_amd64.deb
#dpkg -i pdns-static_3.2-rc4-1_amd64.deb
#add soap username and password, and change uri to precise64
#
#atomiadnsclient --method AddDNSSECKey --arg RSASHA256 --arg 2048 --arg KSK --arg 1
#atomiadnsclient --method AddDNSSECKey --arg RSASHA256 --arg 1024 --arg ZSK --arg 1
#atomiadnsclient --method AddDNSSECKey --arg RSASHA256 --arg 1024 --arg ZSK --arg 0
#atomiadnsclient --method AddNameserverGroup --arg default



ac = AtomiaClient('http://precise64.sejo-int.be/atomiadns.json/pretty', 'test@sejo-int.be', 'test')
ac.AddZone('sejo-int.be', "3600", "precise64.sejo-int.be.", "root.precise64.sejo-int.be.", "3600", "3600", "3600",
           "3600", ["precise64.sejo-int.be.",], "default")
ac.AddDnsRecords("sejo-int.be", [{"ttl": "120", "label": "www", "class": "IN", "type": "A", "rdata": "10.0.2.15"}])
ac.GetDnsRecords('sejo-int.be', "www")
ac.DeleteZone("sejo-int.be")