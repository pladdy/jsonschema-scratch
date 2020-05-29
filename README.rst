jsonschema-scratch
==================

This is a jsonschema and flask sandbox.  This enables setting up some jsonschemas and make
them available via a HTTP interface.

Goals:

- complex JSON schemas that can be resolved if they have references
  - IE DRY up schemas by sharing components but be able to view a schema de-referenced´

API
---

0.1.0
~~~~~

- [x] ``GET /schemas/<some-schema-file.json>``
  - shows the schema file, might have $refs in it
- [ ] ``GET /schemas/<some-schema-file.json>?resolve``
  - shows the schema file but resolved, refs file refs substituted (not local refs though)
- [ ] ``POST /schemas/<some-schema-file.json>?validate``
  - this doesn't seem like the right interface...

  .. code-block:: JSON

    {
      "schema": "",
      "document": {}
    }

TODO
----

- can post a schema
- can validate an object against a schema

References
==========

- `Flask API <https://flask.palletsprojects.com/en/1.1.x/api/>`_
  - `Routing <https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations>`_
- `Understanding JSON Schema <https://json-schema.org/understanding-json-schema/>`_
- `Serving static filesin Flask <https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask>`_
