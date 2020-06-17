Changelog
=========

Project changes based on `changelog <https://keepachangelog.com/en/1.0.0/>`_ format.

[0.2.0] - 2020-06-16
~~~~~~~~~~~~~~~~~~~~

Fixed
-----

- Out of date docs

Added
-----

- badges for build, codacy, coverage, and license
- dephell with a requirements.txt file

[0.1.0] - 2020-06-12
~~~~~~~~~~~~~~~~~~~~

Added
-----

- GET ``/schemas`` endpoint to view schemas
  - ?resolve parameter to resolve schema refs
- POST ``/validate`` endpoint that takes a ``?schema=<name of schema from /schemas>``
- Travis CI set up
