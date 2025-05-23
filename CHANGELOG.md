## [2.2.1](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.2.0...v2.2.1) (2025-05-23)

### Bug Fixes

* remove option --no-type-objects from build ([6e4fbc0](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/6e4fbc01079ec3f8f3c19b465a9af76c1a36ae1d))

## [2.2.0](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.1.3...v2.2.0) (2025-05-22)

### Features

* add name and version on conformity_assessment_scheme. Remove unneeded multiple: true ([b0bc39b](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/b0bc39b0c84c613ab046a9f6d173e8964a8b9ed8))

### Bug Fixes

* **ci:** fix until https://github.com/cycjimmy/semantic-release-action/pull/245 is resolved ([d7308c5](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/d7308c53d2c9676e1d0827daca333b117712ae6f))

## [2.1.3](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.1.2...v2.1.3) (2025-05-05)

### Bug Fixes

* fix the ontology URL (http -> https and remove trailing #) ([f309ff8](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/f309ff82da291316b6ca959db73f8730a2297455))

## [2.1.2](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.1.1...v2.1.2) (2025-05-05)

### Bug Fixes

* remove default .owl.tll suffix in the ontology IRI ([00c92b0](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/00c92b0dc8ca8dd2929a6b2f1718d5f2ae74d7e2))

## [2.1.1](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.1.0...v2.1.1) (2025-05-05)

### Bug Fixes

* **shape:** open the shape for an open-world ontology ([41754c4](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/41754c459a5c4c962caca4f7b9124712f42285e5))
* **shape:** open the shape for an open-world ontology ([d38db38](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/d38db38e580cf11135ae7e66e6aa65c8bb36d545))

## [2.1.0](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.0.1...v2.1.0) (2025-05-03)

### Features

* update Attestation.previous_attestation to Statement.previous_statement ([22ab9c7](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/22ab9c70701de49d94197f46214d201a1b25eea4))

## [2.0.1](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v2.0.0...v2.0.1) (2025-05-03)

### Bug Fixes

* **release:** add missing ontology in XML format ([ed922ca](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/ed922cad9d5cd98cbfd350b26c661f2192597422))

## [2.0.0](https://github.com/eclipse-dataspace-cap/cap-ontology/compare/v1.0.0...v2.0.0) (2025-05-03)

### ⚠ BREAKING CHANGES

* error when defining custom datetime with regex. Removed types and lean on xsd:datetime
* turn all range to ObjectProperty except date. Remove mandatory id

### Features

* turn all range to ObjectProperty except date. Remove mandatory id ([3dd9efc](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/3dd9efc5649c239d5154905795e0e6dbe32575ec))

### Bug Fixes

* error when defining custom datetime with regex. Removed types and lean on xsd:datetime ([b72ddc5](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/b72ddc509414c0ebf4838c399a5fe07105ab88d9))

# 1.0.0 (2025-03-26)


### Bug Fixes

* fix inconsistancy in range declaration. Thanks [@twur](https://github.com/twur) ([3a7ff5f](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/3a7ff5f08e8a00b3c0053c089ea1d80a98ba6f03))
* fix md syntax ([670b9ad](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/670b9addf0c1cc91724041ced4a408e27c03ba24))
* fix navigation for emuns/slots/types ([218e866](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/218e8668778e901f285bebf97e174da64113a811))
* use of old field name subject instead of object ([92fb271](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/92fb271118dfbf509eb8b475d469d594c73b4efe))


### Features

* add Surveillance class and valid_from/valid_until field on Attestation ([31a6c90](https://github.com/eclipse-dataspace-cap/cap-ontology/commit/31a6c905ccc2925d373ea49f1ddcc971cc8e3513))
