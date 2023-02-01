### IP Address
#### Types
- IP V4
- IP V6

#### IP V4
```
192.168.0.40
```
- Each of the segment of the IP can holds up to 256 number. So, total IP possible `256^4` [4 segments] = 4 billion.
- Changing part of Ip called `Host Portion` like `*.*.*.40`.
- Unchanging part of Ip called `Network Portion` like `192.168.0.*`.

### Types of IP V4
 - 127.0.0.1 `[Local Loop Address/LocalHost]`
 - LAN IP
    - 10.*.*.*
    - 172.*.*.*
    - 192.*.*.*

### Subnet Mask
An IP address
```
10.10.11.4
```

Binary Representation of the IP
```
00001010.00001010.00001011.00000100
```
- The part that we don't want to change or keep common will be represent with all `1`.
```
11111111.11111111.11111111.00000000
```
which is also means
```
255.255.255.0
```

- It means only the last part will change and first 3 portion will be same for all devices in the same network.


### Ping
```
ping IP_ADDRESS
```
- If ping success it means the IP is reachable. If not, there could be 2 meaning,
    - Either the IP is not reachable.
    - Or, it's reachable but not respoding.


### Default Gateway
All the connected device data will be send/receive through the default gateway.

### DNS Server
Server that map all sites `URL` and `IP`. All networks needs an DNS Server. Otherwise we would need to use direct IP address instead of site url like google.com.