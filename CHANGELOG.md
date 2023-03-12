# Changelog

## v1.8.0

* feat: testing new speed improvement [1ce828c](https://github.com/builder555/PineSAM/commit/1ce828cc7e3ec8531220b64c24e8b21f3f415ce4)
* fix: move start commands used for binaries [48b1a18](https://github.com/builder555/PineSAM/commit/48b1a184594f6be7106be9792097b40ab44c85fd)
* update readme [35621ae](https://github.com/builder555/PineSAM/commit/35621ae4f1aa353ac4c10b26930ae9da209eeaab)
* feat: messing around with css [14e89a9](https://github.com/builder555/PineSAM/commit/14e89a9cb9e5a04db3345f7630aa959aaa5d7924)
* fix: cleaned up styling issues [cc85c89](https://github.com/builder555/PineSAM/commit/cc85c89d75cb0dd43f19f849ef9874ee152777d2)
* fix: updated settings colours to match work hud [94985dc](https://github.com/builder555/PineSAM/commit/94985dcd3487e660f954a26b3ae41603403534d3)
* fix: prevent crash when BLE sends 'turned off' error [8016111](https://github.com/builder555/PineSAM/commit/801611113d801b7194cbe716cd219186c9b2999c)
* feat: add source code as separate zip [7814979](https://github.com/builder555/PineSAM/commit/7814979df4a6533d368f2b0373d6ab34747ac63e)

## v1.5.7

* fix: crash on start when device is not connected [4db6189](https://github.com/builder555/PineSAM/commit/4db61890c8fb47af5692f253d0fce669c21cb71a)
* fix: display brightness values 1-10. closes #82 [1ece9b8](https://github.com/builder555/PineSAM/commit/1ece9b80fd04ede1b89636d07a64630fe72affef)

## v1.5.5

* fix: ensure correct ci files permissions [04f9c37](https://github.com/builder555/PineSAM/commit/04f9c37e73d8c6b648f725a87203b3e27897d490)

## v1.5.4

* feat: using proper vue.js framework [9badfe8](https://github.com/builder555/PineSAM/commit/9badfe86ec9597cd54f198aac5bd00502ff63622)
* fix: ensure settings are fetched at most once a second [764d52c](https://github.com/builder555/PineSAM/commit/764d52cd9bd80bc271910505a92629c2b2ede39b)
* feat: using new build process [9b2c65c](https://github.com/builder555/PineSAM/commit/9b2c65cbed9b19e3d2e59c65b3d878b9e3097dfd)
* fix: updated instructions and convenience scripts [61177fc](https://github.com/builder555/PineSAM/commit/61177fcd430ceb1da52c1bc66b15776f001f7157)
* fix: don't use relative path to get version [64c0ce7](https://github.com/builder555/PineSAM/commit/64c0ce7eb4413d6b4e3b5e998fcb08b692f67a56)
* fix: typo [21636f6](https://github.com/builder555/PineSAM/commit/21636f6f086051f92af04626e668dd1845b774c0)
* update readme [c0434c8](https://github.com/builder555/PineSAM/commit/c0434c8697672aa64f0092e1ef063462a8351bf8)
* update instructions [1de1ffa](https://github.com/builder555/PineSAM/commit/1de1ffaf6b17027764b062325d4c444eeddf1ef7)
* fix: cleaned up setup scripts [b2cd75a](https://github.com/builder555/PineSAM/commit/b2cd75ada8a4dc9765e54a43b2058b2edbb7283b)

## [1.3.1](https://github.com/builder555/PineSAM/compare/v1.3.0...v1.3.1) (2023-02-28)


### Bug Fixes

* hide pinecil name by default. closes [#56](https://github.com/builder555/PineSAM/issues/56) ([0593657](https://github.com/builder555/PineSAM/commit/059365762526d980c09de1e5cbe1890964c7de20))

## [1.3.0](https://github.com/builder555/PineSAM/compare/v1.2.1...v1.3.0) (2023-02-28)


### Features

* holding +/- speeds up change ([9c766a2](https://github.com/builder555/PineSAM/commit/9c766a2971f576692adb923854415576e4e852ed))

## [1.2.1](https://github.com/builder555/PineSAM/compare/v1.2.0...v1.2.1) (2023-02-27)


### Bug Fixes

* numbers shifted up ([fcd2fe7](https://github.com/builder555/PineSAM/commit/fcd2fe7755869e5bfd5aca47dee7a50f3145bd9e))
* prevent console errors when pinecil not connected ([dd660c3](https://github.com/builder555/PineSAM/commit/dd660c39b116c57478bfbb23e76a3490b940ea50))
* use actual settings value instead of ref ([8c34f05](https://github.com/builder555/PineSAM/commit/8c34f05ec822aa497b904cbb80ac3526286774e0))

## [1.2.0](https://github.com/builder555/PineSAM/compare/v1.1.0...v1.2.0) (2023-02-27)


### Features

* broadcast live data to clients [#48](https://github.com/builder555/PineSAM/issues/48) ([bd532a3](https://github.com/builder555/PineSAM/commit/bd532a304118601c528d9a0c6459c8758e468d0c))
* Merge pull request [#55](https://github.com/builder555/PineSAM/issues/55) from NeilHanlon/work-screen_buttons ([764c714](https://github.com/builder555/PineSAM/commit/764c714aaf0556d4c1c73d31bfa53ae7dbcde98a))
* show live temperature + electricals ([5533ec0](https://github.com/builder555/PineSAM/commit/5533ec05957584ca8aec44f9721c591170a4293e))
* Work screen improvements and functionality implmementation ([7291869](https://github.com/builder555/PineSAM/commit/729186984caad2deff45dace91641b2aebb08c5a))


### Bug Fixes

* screen disappears if no device found ([88cf666](https://github.com/builder555/PineSAM/commit/88cf66633782f6358b22e6a04a8145a5b69560de))

## [1.1.0](https://github.com/builder555/PineSAM/compare/v1.0.16...v1.1.0) (2023-02-24)


### Features

* keep the screen awake, closes [#46](https://github.com/builder555/PineSAM/issues/46) ([a337afc](https://github.com/builder555/PineSAM/commit/a337afccf28bf7e27ad2da855b736e7408ab4761))

## [1.0.16](https://github.com/builder555/PineSAM/compare/v1.0.15...v1.0.16) (2023-02-22)


### Bug Fixes

* [#15](https://github.com/builder555/PineSAM/issues/15) ([c21ea39](https://github.com/builder555/PineSAM/commit/c21ea391fa32544af86352cdce67b5498d04df85))

## [1.0.15](https://github.com/builder555/PineSAM/compare/v1.0.14...v1.0.15) (2023-02-22)


### Bug Fixes

* closes [#38](https://github.com/builder555/PineSAM/issues/38) ([6f6fcaa](https://github.com/builder555/PineSAM/commit/6f6fcaad5cc4c93dccfb73ce483a482d1ad2f996))

## [1.0.14](https://github.com/builder555/PineSAM/compare/v1.0.13...v1.0.14) (2023-02-22)


### Bug Fixes

* added link to BLE fw [#36](https://github.com/builder555/PineSAM/issues/36) ([b91b9f8](https://github.com/builder555/PineSAM/commit/b91b9f85e8049651fcc55e441b7218d800c1ba0c))
* aligned controls ([6f8d371](https://github.com/builder555/PineSAM/commit/6f8d3716134ac4067b0df6bf6ad4807405f770e2))
* colour+ui tweaks ([1d60d6f](https://github.com/builder555/PineSAM/commit/1d60d6fb871935a8d3e51aa1792d75d755247a20))
* minor ui cleanup on mobile, fix GH link on ios [#15](https://github.com/builder555/PineSAM/issues/15) ([77b61c7](https://github.com/builder555/PineSAM/commit/77b61c705380ec52653d2bf59d882ef3734b40c3))
* trying to improve [#40](https://github.com/builder555/PineSAM/issues/40) ([175309b](https://github.com/builder555/PineSAM/commit/175309be2990d6f67655822027d3a95b532632ac))
* was an easy fix for [#41](https://github.com/builder555/PineSAM/issues/41) ([1e3a629](https://github.com/builder555/PineSAM/commit/1e3a629bea8d938720cf5abac1dc2d92edcc085b))

## [1.0.13](https://github.com/builder555/PineSAM/compare/v1.0.12...v1.0.13) (2023-02-21)


### Bug Fixes

* potentially addresses [#34](https://github.com/builder555/PineSAM/issues/34) ([3abbcd3](https://github.com/builder555/PineSAM/commit/3abbcd3a55a46b5706261bef1866262f97cd7df6))

## [1.0.12](https://github.com/builder555/PineSAM/compare/v1.0.11...v1.0.12) (2023-02-20)


### Bug Fixes

* left-align labels ([931828c](https://github.com/builder555/PineSAM/commit/931828c077ad1644e6787bdb711d6105be4807d1))

## [1.0.11](https://github.com/builder555/PineSAM/compare/v1.0.10...v1.0.11) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* don't trigger another workflow (hopefully) ([0858bfb](https://github.com/builder555/PineSAM/commit/0858bfbfa08e06da3ca6ab1a07649cd1a7e458e2))
* gh-token didn't work ([4dc73d4](https://github.com/builder555/PineSAM/commit/4dc73d4d0834269eb278c078c0019835ff519f89))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove automerge ([408236b](https://github.com/builder555/PineSAM/commit/408236b83707503d76eab46d1d56db5ef221f064))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.10](https://github.com/builder555/PineSAM/compare/v1.0.9...v1.0.10) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* don't trigger another workflow (hopefully) ([0858bfb](https://github.com/builder555/PineSAM/commit/0858bfbfa08e06da3ca6ab1a07649cd1a7e458e2))
* gh-token didn't work ([4dc73d4](https://github.com/builder555/PineSAM/commit/4dc73d4d0834269eb278c078c0019835ff519f89))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.9](https://github.com/builder555/PineSAM/compare/v1.0.8...v1.0.9) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* don't trigger another workflow (hopefully) ([0858bfb](https://github.com/builder555/PineSAM/commit/0858bfbfa08e06da3ca6ab1a07649cd1a7e458e2))
* gh-token didn't work ([4dc73d4](https://github.com/builder555/PineSAM/commit/4dc73d4d0834269eb278c078c0019835ff519f89))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.8](https://github.com/builder555/PineSAM/compare/v1.0.7...v1.0.8) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* don't trigger another workflow (hopefully) ([0858bfb](https://github.com/builder555/PineSAM/commit/0858bfbfa08e06da3ca6ab1a07649cd1a7e458e2))
* gh-token didn't work ([4dc73d4](https://github.com/builder555/PineSAM/commit/4dc73d4d0834269eb278c078c0019835ff519f89))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.7](https://github.com/builder555/PineSAM/compare/v1.0.6...v1.0.7) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.6](https://github.com/builder555/PineSAM/compare/v1.0.5...v1.0.6) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.5](https://github.com/builder555/PineSAM/compare/v1.0.4...v1.0.5) (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* adding separate automerge workflow ([e219228](https://github.com/builder555/PineSAM/commit/e219228408f36353f93bd838ff2cc35d402e1ca6))
* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* remove dependencies ([b14426f](https://github.com/builder555/PineSAM/commit/b14426f909c2f63191f43912bf3407000dac92fe))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))
* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))
* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## [1.0.4](https://github.com/builder555/PineSAM/compare/v1.0.3...v1.0.4) (2023-02-20)


### Bug Fixes

* again ([5c59726](https://github.com/builder555/PineSAM/commit/5c59726d45fbb5f506916db75e50b4b7d9091d41))
* another automerge test ([8cce26c](https://github.com/builder555/PineSAM/commit/8cce26c9c83897cc4935c769974739e382175855))
* auto-merge isn't working ([c7dc301](https://github.com/builder555/PineSAM/commit/c7dc301907c0922a111e2dba01a20093d2d6a9ce))
* auto-merge version PRs ([abb6dc9](https://github.com/builder555/PineSAM/commit/abb6dc95caddc6921c254e53e9bbeb3d40dac42e))
* automerge test 4 ([4af1be1](https://github.com/builder555/PineSAM/commit/4af1be1eb84e59b67e328b15932a4f541e50f0a2))
* automerge test 5 ([22daaec](https://github.com/builder555/PineSAM/commit/22daaece3a74ffb7965c1e000fd22ac9612c4abf))
* hopefully last attempt at automerge ([af3fa34](https://github.com/builder555/PineSAM/commit/af3fa34530b2e4e0c871a69ca0330bb623a9e0c6))
* log automerge test ([bff6bc0](https://github.com/builder555/PineSAM/commit/bff6bc049ed7a9800311affdf904a969acb8d1aa))
* release-please should be its own job ([3988999](https://github.com/builder555/PineSAM/commit/398899999bc65d3bd7ed4bf66e16ca8770b6a8a1))
* testing another auto-merge ([6a88d5a](https://github.com/builder555/PineSAM/commit/6a88d5ad85b48ced6920cbc0a391d6d19fd98e7a))

## [1.0.3](https://github.com/builder555/PineSAM/compare/v1.0.2...v1.0.3) (2023-02-20)


### Bug Fixes

* display version number ([f2a74d3](https://github.com/builder555/PineSAM/commit/f2a74d3e9755c7d3c46126274b7854883a46d94f))

## [1.0.2](https://github.com/builder555/PineSAM/compare/v1.0.1...v1.0.2) (2023-02-20)


### Bug Fixes

* testing version.txt file ([5a10888](https://github.com/builder555/PineSAM/commit/5a1088881c898384e4fe635cfa84464ead3abe58))

## [1.0.1](https://github.com/builder555/PineSAM/compare/v1.0.0...v1.0.1) (2023-02-20)


### Bug Fixes

* testing versioning ([b6a3052](https://github.com/builder555/PineSAM/commit/b6a3052b738ee61e2122fe828023ea863a0954d9))

## 1.0.0 (2023-02-20)


### Bug Fixes

* added token, hopefully ([20a4824](https://github.com/builder555/PineSAM/commit/20a48247c4202d2f382333e8adcfd642724e17f6))
* attempt 3 at secrets ([c45d4ea](https://github.com/builder555/PineSAM/commit/c45d4ea890616ffa1024d4b3e451e4f4c5830853))
* corrected branch name in gh workflow ([d45ddd3](https://github.com/builder555/PineSAM/commit/d45ddd30cb7f4c39c9440ddd89e632aff2ba9c89))
* maybe now? ([96393bb](https://github.com/builder555/PineSAM/commit/96393bb65def3887d82a1d03cfd19b7768c3f279))
* minor refactor ([8874b73](https://github.com/builder555/PineSAM/commit/8874b73808147417ff44e25fd6cf0453d8e63bff))
