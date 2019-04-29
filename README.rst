PKI Profile xml generator
=========================
* pkiprofilexmlgen Generate the relavant PKI(Dogtag) Profile xml which can be used to add the profile using PKI cli. 


Setup
-----
* Git clone the project::

      git clone https://gitlab.cee.redhat.com/mniranja/pkiprofilexmlgenerator.git
      cd pkiprofilexmlgenerator 
      python setup.py install


Usage
----

* Create a sample User profile xml::
  
     $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" --output /tmp/test1.xml

     $ pki -h <ca-host> -p <ca_port> -d <certdb_dir> -c <certdb_dir_password> -n "valid Agent Cert" ca-profile-add /tmp/test1.xml 

     $ pki -h <ca-host> -p <ca_port> -d <certdb_dir> -c <certdb_dir_password> -n "valid Agent Cert" ca-profile-enable Foobar1 

* Create a custom profile which is valid for 15 days with graceperiod of 5 days
  before and after::
  
     $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
       --notBefore 5 --notAfter 5 --validfor 15 --maxvalidity 30 --outputfile /tmp/test1.xml

* Create a user profile which adds key Encipher and decipher Extensions::

     $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
       --keyusageextensions "keyUsageCritical,keyUsageDigitalSignature,keyUsageNonRepudiation,keyUsageKeyEncipherment,keyUsageEncipherOnly"  \
       --outputfile /tmp/test1.xml

* Create a user profile which add Netscape Extensions nsCertSSLClient and
  nsCertEmail::

    $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
      --netscapeextensions "nsCertCritical,nsCertSSLClient,nsCertEmail" --outputfile /tmp/test1.xml

* Create a user profile with subject Name pattern UID=QAGROUP-.*::

    $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
      --subjectNamePattern UID=QAGROUP-.* --outputfile /tmp/test1.xml

* Create a user profile which adds CRL extension with url 'https://myocsp.example.org/fullCRL' ::

    $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
      --crlextension  "https://myocsp.example.org/fullCRL"  --outputfile /tmp/test1.xml


* Create a user profile which SubjectAlt Name Extension having Requestor Email::

    $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
      --altType RFC822Name --altPattern \\$request.requestor_email$  --outputfile /tmp/test1.xml

* Create a smime profile xml and add the profile::


    $ pkiprofilexmlgen --new smime --profileId FoobarBarSmime1 --output /tmp/test2.xml

* Create a custom server profile which rejects request if if subject DN doesnt have \*.otherexample.org::

    $ pkiprofilexmlgen --new server --profileId FooBarServer1 --profilename "FoobarServer1 Enrollment Profile" \
      --subjectNamePattern "CN=.*.otherexample.org.*"  --outputfile /tmp/test1.xml


* Create a custom server profile with subject Name Pattern having having
  CN=[^,]+,.+ and adding dc=example,dc=org by default to subject DN::


    $ pkiprofilexmlgen --new server --profileId FooBarServer1 --profilename \
      "FoobarServer1 Enrollment Profile" --subjectNamePattern \
      CN=[^,]+,.+  --subjectNameDefault  CN=\\\$request.req_subject_name.cn$,dc=example,dc=org  --outputfile /tmp/test1.xml

* Create custom Server profile with Maximum validity period of 15 days with
  graceperiod of 5 days before and after::

    $ pkiprofilexmlgen --new server --profileId FooBarServer1 --profilename \
    "FoobarServer1 Enrollment Profile" --notBefore 5 --notAfter 5 --validfor \
    15 --maxvalidity 30  --outputfile /tmp/test1.xml

* Create a server profile which SubjectAlt Name Extension having DNSName
  foobar.example.org::

    $ pkiprofilexmlgen --new server --profileId FooBarServer1 --profilename \
    "FoobarServer1 Enrollment Profile" --altType DNSName  --altPattern \
    www.foobar.example.org  --outputfile /tmp/test1.xml
 
* Create a custome server profile with maximum validity period of 30 minutes with
  graceperiod of 5 minutes before and after::

    $ pkiprofilexmlgen --new user --profileId Foobar1 --profilename "Foobar1 Enrollment Profile" \
      --notBefore 5 --notAfter 5 --validfor 15 --rangeunit min --maxvalidity 30 --outputfile /tmp/test1.xml

    
