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
