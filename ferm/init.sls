ferm_pkg:
  pkg.installed:
    - name: {{ ferm.lookup.pkg }}

ferm_cfg:
  file.managed:
    - name: {{ ferm.lookup.cfg }}
    - source: salt://ferm/files/ferm.conf
    - template: jinja
    - context:
        rule_defaults: {{ ferm.rule_defaults }}
        rules: {{ ferm.rules }}

ferm_service:
  service.running:
    - name: {{ ferm.lookup.service }}
    - enable: true
    - require:
      - pkg: ferm_pkg
      - file: ferm_cfg
    - watch:
      - file: ferm_cfg
