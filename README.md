ferm-formula
============

[SaltStack](https://www.saltstack.com/) formula for [ferm](http://ferm.foo-projects.org/).

This formula will install ferm and generate a config file based on pillar data.

# Configuration
### Default configuration
```yaml
ferm:
  lookup:
    pkg: 'ferm'  # ferm package name
    cfg: '/etc/ferm.conf'  # path to ferm config
    service: 'ferm'  # ferm service name
  rule_defaults:  # defaults for rules (merged with rule properties)
    domain:
      - 'ip'
      - 'ip6'
    table: 'filter'
    chain: 'INPUT'
    action: 'ACCEPT'
  rules: {}
```

### Rules
```yaml
rules:
  '10 - policy drop':  # domain (ip ip6) table filter chain INPUT policy DROP mod comment comment "10 - policy drop";
    policy: 'DROP'
    action: ''
  '20 - tcp 80/443':  # domain (ip ip6) table filter chain INPUT proto tcp dport (80 443) mod comment comment "10 - tcp 80/443" ACCEPT;
    proto: 'tcp'
    dport:
      - 80
      - 443
```
