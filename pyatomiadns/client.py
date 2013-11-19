import json
import urllib2


class AtomiaClient():
    """The AtomiaClient plugs in on the json API from atomiadns.
    """

    def __init__(self, url, email, password):
        """Initalizes the AtomiaClient Object,

        The main task for AtomiaClient is to provide all possible API functions that can be executed on the atomiadns soap api.
        We however do not use the SOAP implementation but the json implementation.

        :param url: URL for the atomiadns.json entrypoint
        :param email: email for the user, remember for admin functions one needs the admin email
        :param password: password for the user
        """
        self.url = url
        self.email = email
        self.password = password

    def request(self, method, data):
        req = urllib2.Request(url=self.url + "/" + method)
        req.add_header('X-Auth-Username', self.email)
        req.add_header('X-Auth-Password', self.password)
        req.add_data(data)

        try:
            response = urllib2.urlopen(req)
            return response.read()
        except urllib2.URLError, e:
            return e.read()

    def process_response(self, response):
        return response
    
    def GetLabels(self, zone):
        """GetLabels returns all the labels for a certain zone.


:param zone: `str` zone (example.org, sejo-it.be,...)

        """
        arguments = [zone,]
        data = json.dumps(arguments)
        response = self.request("GetLabels", data)
        return self.process_response(response)
    
    def DeleteZone(self, zone):
        """Deletes a zone from the database.

 :param zone: `str` the name of the zone

        """
        arguments = [zone,]
        data = json.dumps(arguments)
        response = self.request("DeleteZone", data)
        return self.process_response(response)
    
    def AddDNSSECKey(self, algorithm, keysize, keytype, activated):
        """Adds a DNSSEC key to the database.

default algorithm:  RSASHA256
for KSK use keysize 2048, for ZSK use 1024

:param algorithm: `str` defaults to RSASHA256
:param keysize: `int` size of key in bit (1024, 2048,...)
:param keytype: `str` KSK or ZSK
:param activated: `str` yes or no

        """
        arguments = [algorithm,keysize,keytype,activated,]
        data = json.dumps(arguments)
        response = self.request("AddDNSSECKey", data)
        return self.process_response(response)
    
    def AddNameserverGroup(self, groupname):
        """Add a nameserver group.

 :param groupname: `str` name of the group you wish to add

        """
        arguments = [groupname,]
        data = json.dumps(arguments)
        response = self.request("AddNameserverGroup", data)
        return self.process_response(response)
    
    def AddDnsRecords(self, zone, records):
        """Adds a list of records to a zone.


 A record dict is the following:
 {
      "ttl":  "3600",
      "label" : "@",
      "class" : "IN",
      "type" : "A",
      "rdata" : "192.168.0.1"
 }


 :param zone: `str` the name of the zone

 :param records: `list` list of dicts containing the records'

        """
        arguments = [zone,records,]
        data = json.dumps(arguments)
        response = self.request("AddDnsRecords", data)
        return self.process_response(response)
    
    def AddZone(self, zonename, zonettl, mname, rname, refresh, retry, expire, minimum, nameservers, nameservergroup):
        """Add a zone to the Atomia DNS master database.


 :param zonename: `str` the name of the zone

 :param zonettl: `int` the ttl of the SOA-record and the NS-records

 :param mname: `str` the SOA mname field

 :param rname: `str` the SOA rname field

 :param refresh: `int` the SOA refresh field

 :param retry: `int` the SOA retry field

 :param expire: `int` the SOA expire field

 :param minimum: `int` the SOA minimum field

 :param nameservers: `str` a string of the hostnames of the nameservers for the zone comma separated within brackets ([\"dns1.example.org\",\"dns2.example.org\"])

 :param nameservergroup: `str` the nameserver group that should host the zone

        """
        arguments = [zonename,zonettl,mname,rname,refresh,retry,expire,minimum,nameservers,nameservergroup,]
        data = json.dumps(arguments)
        response = self.request("AddZone", data)
        return self.process_response(response)
    
    def DeleteDnsRecords(self, zone, records):
        """Removes the given records.

One should only provide the labels in a following format

'[{"label": "www"}, {"label": "bleh"}]'

        """
        arguments = [zone,records,]
        data = json.dumps(arguments)
        response = self.request("DeleteDnsRecords", data)
        return self.process_response(response)
    
    def GetAllZones(self):
        """GetAllZones returns all the zone names that are defined. This is an ADMIN only method
        """
        arguments = []
        data = json.dumps(arguments)
        response = self.request("GetAllZones", data)
        return self.process_response(response)
    
    def EditZone(self, zonename, zonettl, mname, rname, refresh, retry, expire, minimum, nameservers, nameservergroup):
        """Edits a zone. This is only for completeness, and could be done by editing the SOA and NS-records directly as well.

 :param zonename: `str` the name of the zone
 :param zonettl: `int` the ttl of the SOA-record and the NS-records
 :param mname: `str` the SOA mname field
 :param rname: `str` the SOA rname field
 :param refresh: `int` the SOA refresh field
 :param retry: `int` the SOA retry field
 :param expire: `int` the SOA expire field
 :param minimum: `int` the SOA minimum field
 :param nameservers: `str` a string of the hostnames of the nameservers for the zone comma separated within brackets ([\"dns1.example.org\",\"dns2.example.org\"])
 :param nameservergroup: `str` the nameserver group that should host the zone

        """
        arguments = [zonename,zonettl,mname,rname,refresh,retry,expire,minimum,nameservers,nameservergroup,]
        data = json.dumps(arguments)
        response = self.request("EditZone", data)
        return self.process_response(response)
    
    def DeleteAccount(self, email):
        """Removes a soap account

:param email: `str` email off the account
        """
        arguments = [email,]
        data = json.dumps(arguments)
        response = self.request("DeleteAccount", data)
        return self.process_response(response)
    
    def GetNameserver(self, nameserver):
        """Gets the group name that a nameserver is configured as a subscriber for.


 :param nameserver: `str` the servername to get information for

        """
        arguments = [nameserver,]
        data = json.dumps(arguments)
        response = self.request("GetNameserver", data)
        return self.process_response(response)
    
    def GetDnsRecords(self, zone, label):
        """GetRecord will fetch full record information for zone and label given
        """
        arguments = [zone,label,]
        data = json.dumps(arguments)
        response = self.request("GetDnsRecords", data)
        return self.process_response(response)
    
    def DeleteNameServerGroup(self, groupname):
        """Delete a nameserver group.

 :param groupname: `str` name of the group you wish to delete

        """
        arguments = [groupname,]
        data = json.dumps(arguments)
        response = self.request("DeleteNameServerGroup", data)
        return self.process_response(response)
    
    def DeleteNameserver(self, nameserver):
        """Remove a nameserver as a subscriber of changes to the data set in this server.

:param nameserver: `str` the servername to remove as a subscriber

        """
        arguments = [nameserver,]
        data = json.dumps(arguments)
        response = self.request("DeleteNameserver", data)
        return self.process_response(response)
    
    def AddAccount(self, email, password_soap):
        """Add an account for soap

:param email: `str` email used as login
:param paswword_soap: `str` password for the user

        """
        arguments = [email,password_soap,]
        data = json.dumps(arguments)
        response = self.request("AddAccount", data)
        return self.process_response(response)
    
    def GetZone(self, zone):
        """GetZone returns the complete zone info with all records

:param zone: `str` zone (example.org, sejo-it.be,...)

        """
        arguments = [zone,]
        data = json.dumps(arguments)
        response = self.request("GetZone", data)
        return self.process_response(response)
    
    def AddNameserver(self, nameserver, nameservergroup):
        """Add a nameserver as a subscriber of changes to the data set in this server.

 :param nameserver: `str` the servername to add as a subscriber
 :param nameservergroup: `str` the nameserver group that this nameserver should subscribe to changes for

        """
        arguments = [nameserver,nameservergroup,]
        data = json.dumps(arguments)
        response = self.request("AddNameserver", data)
        return self.process_response(response)
    
    def ReloadAllZones(self):
        """Mark all zones in the database as changed.
        """
        arguments = []
        data = json.dumps(arguments)
        response = self.request("ReloadAllZones", data)
        return self.process_response(response)
    