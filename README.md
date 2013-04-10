# py-mdns
A simple python api for common zeroconf mdns operations. Py-MDNS uses the OS's native MDNS utilities to publish and find discoverable services.

## Installation

1. `git clone git@github.com:D1plo1d/py-mdns.git`
2. `cd py-mdns`
3. `sudo python setup.py install`


## Example Usage

### Publishing a Service

```python
import mdns

# This will add a new "my_test" discoverable service
# to the locahost's MDNS service daemon (bonjour or avahi).
services = ({'type': 'my_test', 'port': 1234})
mdns.publisher().save_group({'name': 'test', 'services': services })
```


## Development

### Current Status
  - Abstracted backend mechanism from regular API usage.
  - Unit test framework in place.
  - Avahi Publisher is working.
  - Example publisher & resolver is working.

### Project Goals
  - Will initially be based from avahi api. Should
    interface what we can to allow for future Bonjour impl.
  - Mostly does mdns publish & lookup.
  - Should be able to resolve a single host name, or a group of names
    (tied to a dbus service).
  - Should hide dbus and avahi calls as much as possible.
  - Should present a simple API interface to downstream callers.
  - Should allow for configurable wait time (if possible) while
    looking up a host.
  - Should not be directly tied to a GUI API.
  - API should return multiple lookup in a set or array.
  - API should allow for some basic filtering of records based upon
    common use cases of lookup.
