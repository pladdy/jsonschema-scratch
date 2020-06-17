jsonschema-scratch
==================

|build-status| |code coverage| |codacy| |MIT license|

.. |build-status| image:: https://travis-ci.com/pladdy/jsonschema-scratch.svg?branch=master
    :alt: build status
    :scale: 100%
    :target: https://travis-ci.com/pladdy/jsonschema-scratch

.. |code coverage| image:: https://codecov.io/gh/pladdy/jsonschema-scratch/branch/master/graph/badge.svg
  :alt: code coverage
  :scale: 100%
  :target: https://codecov.io/gh/pladdy/jsonschema-scratch

.. |codacy| image:: https://app.codacy.com/project/badge/Grade/454e2ed095ed4a41b545b949a7343c30
  :alt: codacy
  :scale: 100%
  :target: https://www.codacy.com/manual/pladdy/jsonschema-scratch?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=pladdy/jsonschema-scratch&amp;utm_campaign=Badge_Grade

.. |MIT license| image:: https://img.shields.io/badge/License-MIT-blue.svg
  :alt: MIT license
  :scale: 100%
  :target: https://lbesson.mit-license.org/

This is a jsonschema and flask sandbox.  This enables setting up some jsonschemas and make
them available via a HTTP interface.

Goals / Ideas
-------------

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

Document with swagger/openapi and/or use connexion?

TODO
----

- when calling /schemas/ to view, if it's a dir, create links to the files so you can just click on it
- create validate blueprint and a schemas blueprint?
- print exceptions better, look into traceback
  - https://docs.python.org/3.8/library/traceback.html
- can post a schema

References
==========

- `Flask API <https://flask.palletsprojects.com/en/1.1.x/api/>`_
  - `Flask Source <https://github.com/pallets/flask>`_
  - `Routing <https://flask.palletsprojects.com/en/1.1.x/api/#url-route-registrations>`_
  - `Config <https://flask.palletsprojects.com/en/1.1.x/api/#configuration>`_
  - `Patterns <https://flask.palletsprojects.com/en/1.1.x/patterns/>`_
- `Werkzeug Source <https://github.com/pallets/werkzeug>`_
- `Understanding JSON Schema <https://json-schema.org/understanding-json-schema/>`_
- `Serving static files in Flask <https://stackoverflow.com/questions/20646822/how-to-serve-static-files-in-flask>`_
- `Explore flask patterns <https://exploreflask.com/en/latest/index.html>`_
- `HTTP Status Codes <https://developer.mozilla.org/en-US/docs/Web/HTTP/Status>`_
- `JSONRef <https://github.com/gazpachoking/jsonref>`_
  - `JSONRef Example <https://medium.com/grammofy/handling-complex-json-schemas-in-python-9eacc04a60cf>`_
- `Dephell <https://dephell.readthedocs.io/>`_

Refs and $ref URIs
------------------

It's possible to use relative file urls in the schemas as long as a base-uri is set to an absolute
file URI for jsonref and a RefResolver objects being used.

- https://github.com/Julian/jsonschema/issues/98
- https://jsonref.readthedocs.io/en/latest/#jsonref.loads

Tools
-----

- `JSON Schema Validation <https://www.jsonschemavalidator.net/>`_
