.. open-elis documentation master file, created by
   sphinx-quickstart on Sun Sep 28 16:42:31 2025.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

open-elis documentation
=======================

Elis is a therapy recommendation API that helps match users with appropriate therapy clusters based on questionnaire responses.

Features
--------

* Questionnaire processing with 26 questions across 4 categories
* Therapy cluster recommendation based on scoring algorithm
* RESTful API for integration with frontend applications
* Support for multiple therapy method clusters (PA, VT, SYS, PZ, G)

App Modules
-----------

.. toctree::
   :maxdepth: 2
   :caption: Core Application:

   calculations
   main

API Endpoints
-------------

.. toctree::
   :maxdepth: 2
   :caption: Endpoints:

   endpoints.calculate_result
   endpoints.root
   endpoints.therapists
   endpoints.therapy_clusters
   endpoints.therapy_methods
   endpoints.therapy_types

Utils Package
-------------

.. toctree::
   :maxdepth: 2
   :caption: Utilities:

   utils.api_key_generator
   utils.db_session
   utils.middleware
   utils.validate_api_key

Data Package
------------

.. toctree::
   :maxdepth: 2
   :caption: Data Management:

   data.models
   data.import_data
   data.populate_tables
   data.run_mappings

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

