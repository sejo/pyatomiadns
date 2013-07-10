#
# Copyright (c) 2012, SeJo IT BVBA
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
# 1. Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
# 2. Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
# 3. All advertising materials mentioning features or use of this software
#    must display the following acknowledgement:
#    This product includes software developed by the <organization>.
# 4. Neither the name of the <organization> nor the
#    names of its contributors may be used to endorse or promote products
#    derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY SeJo IT BVBA ''AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL <COPYRIGHT HOLDER> BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
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
        response = urllib2.urlopen(req)
        return response.read()

    def process_response(self, response):
        print response
    
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
    
    def AddDnsRecords(self, zone, records):
        """Adds a list of records to a zone.

A record dict is the following: { "ttl":  "3600", "label" : "@", "class" : "IN", "type" : "A", "rdata" : "192.168.0.1" }

:param zone: `str` the name of the zone
:param records: `list` list of dicts containing the records
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
:param nameservers: `str` a string of the hostnames of the nameservers for the zone comma separated within brackets (["dns1.example.org","dns2.example.org"])
:param nameservergroup: `str` the nameserver group that should host the zone 
        """
        arguments = [zonename,zonettl,mname,rname,refresh,retry,expire,minimum,nameservers,nameservergroup,]
        data = json.dumps(arguments)
        response = self.request("AddZone", data)
        return self.process_response(response)
    
    def DeleteNameserver(self, nameserver):
        """Remove a nameserver as a subscriber of changes to the data set in this server.

:param nameserver: `str` the servername to remove as a subscriber
        """
        arguments = [nameserver,]
        data = json.dumps(arguments)
        response = self.request("DeleteNameserver", data)
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
:param nameservers: `str` a string of the hostnames of the nameservers for the zone comma separated within brackets (["dns1.example.org","dns2.example.org"])
:param nameservergroup: `str` the nameserver group that should host the zone 
        """
        arguments = [zonename,zonettl,mname,rname,refresh,retry,expire,minimum,nameservers,nameservergroup,]
        data = json.dumps(arguments)
        response = self.request("EditZone", data)
        return self.process_response(response)
    
    def ReloadAllZones(self):
        """Mark all zones in the database as changed.
        """
        arguments = []
        data = json.dumps(arguments)
        response = self.request("ReloadAllZones", data)
        return self.process_response(response)
    