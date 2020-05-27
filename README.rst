Ideas

API
===

0.1
---

- /path/to/schema.json
  - shows the schema file, might have $refs in it
- /path/to/schema.json?resolve
  - shows the schema file but resolved, refs file refs substituted (not local refs though)

Deps
----

- jsonschema
- flask

TODO
----

- can post a schema
- can validate an object against a schema
