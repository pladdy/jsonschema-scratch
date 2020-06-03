jsonschema-scratch
==================

This is a jsonschema and flask sandbox.  This enables setting up some jsonschemas and make
them available via a HTTP interface.

Goals:

- complex JSON schemas that can be resolved if they have references
  - IE DRY up schemas by sharing components but be able to view a schema de-referenced´
- store schemas in an embedded db (sqlite?)?  or just use the file system?
  - sqlite has json functions
  - instead of a file structure just have table(s)
  - if i use a db schemas need to be easy to discover (ie see a list like a filesystem?)
    - how do i list them now in flask?
- version schemas so you can update them
  - not sure if it makes sense to require a version # in the json schema, but perhaps in the db?

API
---

0.1.0
~~~~~

- [x] ``GET /schemas/<some-schema-file.json>``
  - shows the schema file, might have $refs in it
- [ ] ``GET /schemas/<some-schema-file.json>?resolve``
  - shows the schema file but resolved, refs file refs substituted (not local refs though)
- [x] ``POST /schemas/<some-schema-file.json>?validate``
  - this doesn't seem like the right interface...

  .. code-block:: JSON

    {
      "schema": "",
      "document": {}
    }

TODO
----

- when calling /schemas/ to view, if it's a dir, create links to the files so you can just click on it
- create validate blueprint and a schemas blueprint?
- print exceptions better, look into traceback
  - https://docs.python.org/3.8/library/traceback.html
- can post a schema
- how should the ref urls in the schemas be set up?
  - file uris need to be absolute path...link /var/data/schemas to ./schemas?
  - http uris need to be the url, but putting localhost:5000 in there seems dumb...
  - file uri seems best?
  - use http://localhost:5000 for now...

References
==========

- `Flask API <https://flask.palletsprojects.com/en/1.1.x/api/>`_
  - `Flask Source <https://github.com/pallets/flask>`_
  - `Routing <https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations>`_
  - `Patterns <https://flask.palletsprojects.com/en/1.1.x/patterns/>`_
- `Werkzeug Source <https://github.com/pallets/werkzeug>`_
- `Understanding JSON Schema <https://json-schema.org/understanding-json-schema/>`_
- `Serving static files in Flask <https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask>`_
- `Explore flask patterns <https://exploreflask.com/en/latest/index.html>`_
- `HTTP Status Codes <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>`_
