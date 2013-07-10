from pyatomiadns.client import AtomiaClient

ac = AtomiaClient('http://precise64.sejo-int.be/atomiadns.json/pretty', 'test@sejo-int.be', 'test')
ac.AddZone('sejo-int.be', "3600", "precise64.sejo-int.be.", "root.precise64.sejo-int.be.", "3600", "3600", "3600",
           "3600", ["precise64.sejo-int.be.",], "default")
ac.AddDnsRecords("sejo-int.be", [{"ttl": "120", "label": "www", "class": "IN", "type": "A", "rdata": "10.0.2.15"}])
ac.GetDnsRecords('sejo-int.be', "www")
ac.DeleteZone("sejo-int.be")