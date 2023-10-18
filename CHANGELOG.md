# Changelog

## v1.14.1

* fix: can adjust Hall Sensor setting. closes #33 [ddbeac2](https://github.com/builder555/PineSAM/commit/ddbeac259eb292fbe863a47107e41510e0bacd50)

## v1.14.0

* fix: removed time ticks, updated initial max power [692090f](https://github.com/builder555/PineSAM/commit/692090fe1bf6979cf78533040756636e147f51f8)
* feat: display temperature value on the chart [6039e75](https://github.com/builder555/PineSAM/commit/6039e7506901edb271b22ec7e2296014cc916c7b)

## v1.13.13

* add docker support [dbe727a](https://github.com/builder555/PineSAM/commit/dbe727a8e21e0538a6f5d5516e7856badd331732)
* Merge pull request #186 from krisstakos/master

Add docker support. Tested on RPI4 [0ba5239](https://github.com/builder555/PineSAM/commit/0ba52394483ec16abf3fc5aa0637f6e93603df32)
* fix: ensure pipenv is setup during initial run [7dd8572](https://github.com/builder555/PineSAM/commit/7dd85729b49bbd1fc0501d3e941a594f00edb67a)

## v1.13.12

* fix: minimum temperature & update links (#183)

* chore: update changelog

* chore: update changelog

* fix: minimum temperature

-  50 F = 10 C  correction on minimum temperature
- to align with new changes in 2.21 IronOS
- closes ticket  https://github.com/builder555/PineSAM/issues/182

* fix:  links to usage guides

* fix: update mkdocs

* fix: update mkdocs

---------

Co-authored-by: Robert'); DROP TABLE students; -- <85308587+builder555@users.noreply.github.com>
Co-authored-by: github-actions[bot] <github-actions[bot]@users.noreply.github.com> [c9621d3](https://github.com/builder555/PineSAM/commit/c9621d3fdbbde36b4eb471d8d8ca9c896544f7a0)

## v1.13.11

* fix(docs): fix devcontainer and docs-deploy syntax [cc3b639](https://github.com/builder555/PineSAM/commit/cc3b63909acf0447f9ec5acef0426aae4e546e62)
* fix: cleanup files that should have been deleted [ae8bcb5](https://github.com/builder555/PineSAM/commit/ae8bcb5156d029b4f0337eaaa15bf033a4f69077)
* Merge pull request #175 from neil-forks/fix/docs-build

fix(docs): fix devcontainer and docs-deploy syntax [cfea04e](https://github.com/builder555/PineSAM/commit/cfea04ed7c37695375243cf9874c22a333e92b72)

## v1.13.10

* Setup and configure mkdocs, write initial docs

We need a place to write documentation for PineSAM and accept
contributions from non-technical end users who wish to add items to the
FAQ, add information, and otherwise grow the project.

This is a fairly large PR but it is the result of about a week of work
getting things setup and configured how we think it should be. [56bd0ed](https://github.com/builder555/PineSAM/commit/56bd0ed3127856b87760a9d613c5e92b2c5b15a9)
* Merge pull request #173 from neil-forks/feature/mkdocs

Setup and configure mkdocs, write initial docs [31284fe](https://github.com/builder555/PineSAM/commit/31284feb5f0028d0528fb7d25619080ce81c17c7)
* fix: small change for version bump [38a8998](https://github.com/builder555/PineSAM/commit/38a8998f75084d10db714327b2d03f2938266d11)

## v1.13.9

* fix: update docs with new IronOS version [804c77b](https://github.com/builder555/PineSAM/commit/804c77b343e9cab324b43b57440b4c77f026db55)

## v1.13.8

* fix: smaller font for build version [48a9f8e](https://github.com/builder555/PineSAM/commit/48a9f8e2ff603e094fb02d0d42d3a3b75823818e)

## v1.13.7

* fix: build shows only number version [4f778ab](https://github.com/builder555/PineSAM/commit/4f778abd595855e9d3d54df17b9ddaeb1ee98630)

## v1.13.6

* fix: get latest os ver. + if new build available [e68b9d4](https://github.com/builder555/PineSAM/commit/e68b9d4cb4d7d38cf1221db4c0198ceaaf85b149)
* fix: update tests for new version [b07d7c5](https://github.com/builder555/PineSAM/commit/b07d7c509df10d9470accec7016ab8fcfb7e786c)
* fix: display ironOS build version [095f7c0](https://github.com/builder555/PineSAM/commit/095f7c0181e67ae865caa0dbf20b1b74d61420d5)

## v1.13.3

* feat: pass the build version from pinecil [86eb85a](https://github.com/builder555/PineSAM/commit/86eb85a0530675bf288939372c364047619ff22d)
* fix: by default send v2.20 as build version [2f3426d](https://github.com/builder555/PineSAM/commit/2f3426d089aa4966e73dac88144d70aca9716913)
* fix: ensure proper min/max range for brightness [68e9431](https://github.com/builder555/PineSAM/commit/68e943115aee0b60be49239b4804530b413566d0)
* fix: display proper brightness values for v2.21. closes #133 [3f44fc5](https://github.com/builder555/PineSAM/commit/3f44fc5e6157743b0dd1866afbeee7cdfbed6977)

## v1.12.16

* fix: bring back pinecil-id. closes #166 [0efead1](https://github.com/builder555/PineSAM/commit/0efead14e24a279a0865ecb286aac565ee8baf79)

## v1.12.15

* Mkdocs patch (#152)

* Updated assets & greeting

* Fix for too long title

* Fix view and edit buttons

* Menu fix for title being too long

* Updated lists & headings

* fix checkbox

* Display MAC adress as code

* Update mkdocs.yml

* Fix image paths

* Added back "documentaion" to title

* Major overhaul

- Welcome page fixed
- New categories
- Emojis added
- Added metadata and special settings
- Formatting corrected
- Links fixed
- other fixes

* Update docs-deploy.yml

* Moved all images into one directory

* Reworked arrangement of Installaion page

* Formatting

* Moved Debugging & Terminal section to own document

* Added link to repo in contribution section [fd840e6](https://github.com/builder555/PineSAM/commit/fd840e6fe173a390eb829d7f60856f4e4349fff1)
* fix: dummy commit to up the version [8a8315d](https://github.com/builder555/PineSAM/commit/8a8315da98375cfa04fa21e168aa2dac13b35e8d)

## v1.12.14

* Added concurrency to workflow [1120bb2](https://github.com/builder555/PineSAM/commit/1120bb2c496d4f78286f41fae85fd609cc72aadd)
* Merge pull request #151 from MagicLike/patch-1

Added concurrency to mkdocs workflow [8ce2ec8](https://github.com/builder555/PineSAM/commit/8ce2ec8a7b18e2e16c2f55d697a2b58ac3f99c46)
* fix Mkdocs  (#153)

* Update index.md

* Create test

* fix: Mkdocs 

fix: Mkdocs   add content, images, icons

* Delete test

* Add files via upload

* fix: link mkdocs

* fix: add images for mkdocs

* Delete workHUD1.png

* fix: links to images in docs

fix links so that all images are from  docs images folder and not duplicated

* Delete workHUD.png

duplicate,  all images in /docs/images now

* Delete workHUD-detailed.png

duplicate,  all images in /docs/images now

* Delete full_settings.png

duplicate,  all images in /docs/images now

* Delete PineSAM_logo-A017A5.png

duplicate,  all images in /docs/images now

* fix: broken edit link mkdocs

* fix: links

* fix: image links [556d646](https://github.com/builder555/PineSAM/commit/556d64616dab773643859de7f4c614441f1c15be)
* fix: added vertical grid. closes #54 [0a3f07f](https://github.com/builder555/PineSAM/commit/0a3f07fb28fc28315833a3a466cb593315db1e8c)

## v1.12.13

* fix: instructions, docs, wiki (#144)


fix badge links

* Update Readme.md

* fix: updated instructions

fix: closes issue https://github.com/builder555/PineSAM/issues/136

* fix: instructions

fix: instructions

* fix: links

fix: links

* Update Readme.md

* fix: add work HUD reference image

fix: add work HUD detailed reference image

* fix: added working 128 firmware

fix: added link to working 128 UUID  firmware.  old beta ironOS causes main_server terminal crash

* Update Readme.md

* fix: readme doc

fix: readme doc

* fix: typo readme

fix: typo readme [5f461fd](https://github.com/builder555/PineSAM/commit/5f461fd8aee172f85f4690e821b0ae87bfe353ae)
* fix: error from wait=process,  instruction docs (#149)

fix badge links

* Update Readme.md

* fix: updated instructions

fix: closes issue https://github.com/builder555/PineSAM/issues/136

* fix: instructions

fix: instructions

* fix: links

fix: links

* Update Readme.md

* fix: add work HUD reference image

fix: add work HUD detailed reference image

* fix: added working 128 firmware

fix: added link to working 128 UUID  firmware.  old beta ironOS causes main_server terminal crash

* Update Readme.md

* fix: readme doc

fix: readme doc

* fix: typo readme

fix: typo readme

* fix: wait-process error on windows

fix:  this closes ticket for https://github.com/builder555/PineSAM/issues/148
fix of Wait-process causing error in terminal window  start.ps1 [ed98d62](https://github.com/builder555/PineSAM/commit/ed98d6207deb6c9a4b36f1f91d30ed30a6771721)

## v1.12.11

* fix: broken if statement [e484f67](https://github.com/builder555/PineSAM/commit/e484f67929eb198925df3e35f6c45edaff582d2c)

## v1.12.10

* Use mkdocs as documentation software instead of GitHub wiki (#129)

* Added mkdocs

- Added mkdocs with all assets and my customisations to the repo
- Used elements from Wiki

* Renamed folder 'usage' to 'how-to-use'

Due to server issues

* Changed theme switcher icons

* Changed logo and adjusted colors

* Combined Usage & HUD and integrated TOC

* Fixed image paths

* Updated image path [c18cd7a](https://github.com/builder555/PineSAM/commit/c18cd7a3b768058e3762b3d76e39419a0fbcb303)
* Added logic to call xdg-open instead of open on linux [3286763](https://github.com/builder555/PineSAM/commit/3286763c2e151d8436d7a6ffab8c4495d42927b8)
* Merge pull request #139 from builder555/master

update dev [7ef05bb](https://github.com/builder555/PineSAM/commit/7ef05bb72e223d0d549ff9fe84ed432bd53677fa)
* Merge pull request #140 from Spagett1/dev

Added logic to call xdg-open instead of open on linux [ff25e61](https://github.com/builder555/PineSAM/commit/ff25e61e92d808c5a1999b194b8a5f08c6f342fa)
* fix: dummy commit to increase version [553c54a](https://github.com/builder555/PineSAM/commit/553c54ab611c61597e3cff2fe32c36afcc168779)

## v1.12.9

* fix setup-dev.bat  for Windows users (#128)

* Update Readme.md
* Update setup-dev.bat [3e27f3f](https://github.com/builder555/PineSAM/commit/3e27f3f6c35153ae3ea7dc8454d4ee48e2940b5c)
* fix: updated to work with new uuid128 [f28bc0d](https://github.com/builder555/PineSAM/commit/f28bc0db97ee072d04d406d6fc8a252a4803d949)

## v1.12.8

* can list services on a ble device [23a7d11](https://github.com/builder555/PineSAM/commit/23a7d110f01da067540d63e7151c42d7a1d95bbc)
* fix: prep work for uuid128 change [9f76308](https://github.com/builder555/PineSAM/commit/9f76308234b7b11b240f0b63a935329b4c2c5c14)
* fix: store external dependencies locally. closes #125 [72536cf](https://github.com/builder555/PineSAM/commit/72536cf8173c4c86c2b213a1e0bc24186d691140)

## v1.12.6

* Correct Readme, add Usage instructions to Wiki (#120)

* Update Readme.md

* Update Readme.md

* Update Readme.md

* Update Readme.md

* Update Readme.md

* Update Readme.md [13ecc27](https://github.com/builder555/PineSAM/commit/13ecc2781391675ee80030341e3f3b01c25c2b30)
* fix: update command for windows [ff6603e](https://github.com/builder555/PineSAM/commit/ff6603e85127d9a2742803b1d05d3b116b01a12c)
* feat: first version with live data chart [c7b689e](https://github.com/builder555/PineSAM/commit/c7b689e3eab7e8dc1e6e68be885b99788fa7600c)
* fix: prevent +/- buttons getting stuck. closes #119 [c518e6d](https://github.com/builder555/PineSAM/commit/c518e6d0265a88acfa3f558c6072353417e4cb70)
* fix: version comparison was incorrect [039fa6a](https://github.com/builder555/PineSAM/commit/039fa6a88596cb365b7bd11fa8dcfc9031fd1150)
* fix: right click triggers preset override [7ff9fd0](https://github.com/builder555/PineSAM/commit/7ff9fd0aa69ee97efc5db126e049f1432bf3879e)
* fix: work hud gets split when div is too tall [a548bd8](https://github.com/builder555/PineSAM/commit/a548bd81b20d41fda69ba98f44988a3e45b77815)
* fix: display work hud inline with graph [873a543](https://github.com/builder555/PineSAM/commit/873a543125ddb7d84ddbd639f8345382e2b2aeea)
* fix: clean up chart style and code [6b8bc30](https://github.com/builder555/PineSAM/commit/6b8bc304c0d4cc398e346dbe11c9bbad35589f0a)

## v1.11.2

* Correct Readme, add Usage instructions to Wiki (#120)

* Update Readme.md

* Update Readme.md

* Update Readme.md

* Update Readme.md

* Update Readme.md

* Update Readme.md [13ecc27](https://github.com/builder555/PineSAM/commit/13ecc2781391675ee80030341e3f3b01c25c2b30)

## v1.11.2

* Update Readme.md [906e3d9](https://github.com/builder555/PineSAM/commit/906e3d90555208b152d2eed0b6c09c2e02c916f6)

## v1.11.1

* Update TheSettings.vue [2a37927](https://github.com/builder555/PineSAM/commit/2a3792785fcfce106cf0f5f94cc91091341b8478)
* Update Readme.md [7b724b6](https://github.com/builder555/PineSAM/commit/7b724b65711dd67a72366b1be347735397645335)
* Merge pull request #108 from River-Mochi/dev
* update readme, added link to Debug Menu settings in Debug Category [25aa43f](https://github.com/builder555/PineSAM/commit/25aa43f70752cb90343626db4b65f850e1a80073)
* fix: don't show version until it's available [3be7c04](https://github.com/builder555/PineSAM/commit/3be7c0476a6799ce42c8a50195ce5e90c32cb670)
* feat: show when new version is available [f968bbf](https://github.com/builder555/PineSAM/commit/f968bbf2b09460cb2f7ab41ca01ac931b9397180)
* fix: compares semver properly [3a1fb08](https://github.com/builder555/PineSAM/commit/3a1fb08e412dce8a15589b0cc8b2b4a4c8f4635a)

## v1.10.0

* fix: removed reload settings button [0550eb4](https://github.com/builder555/PineSAM/commit/0550eb4caa730db4af79c0aa8d21324a892c80a8)
* fix: smaller font for device name [06d69e3](https://github.com/builder555/PineSAM/commit/06d69e3ecb99402a1130bb0a3e4737dbf81f4a04)
* feat: add debug data. closes #39 [98488fa](https://github.com/builder555/PineSAM/commit/98488fab5daa32abec0fbcc9a995f5864d52fc2b)

## v1.9.4

* fix: move work hud up, closes #102 [f9b3b20](https://github.com/builder555/PineSAM/commit/f9b3b20e7c8a21191893709d5e47053c6c85ff2d)
* docs: Update with information about packaged versions of PineSAM
* update and add logos [3bfb1d8](https://github.com/builder555/PineSAM/commit/3bfb1d85fa23cd1e8fdd2cf33497f2c107099feb)
* Merge pull request #103 from River-Mochi/dev

Update readme, install instructions, badges [9c8bce6](https://github.com/builder555/PineSAM/commit/9c8bce67fc8601bc37c7ece5d3e9019984ef9758)

## v1.9.3

* fix: removed duplicate job [12d55d1](https://github.com/builder555/PineSAM/commit/12d55d11630171e84a864d3b31c2958822934ed9)
* fix: tweak the therm. colour a bit. should close #57 [b9e75bd](https://github.com/builder555/PineSAM/commit/b9e75bdc9f338da4029af9ae9ec1288798d301af)

## v1.9.1

* fix: show hints by default, remember last setting. closes #64 [accede2](https://github.com/builder555/PineSAM/commit/accede2779a25f6bc2158d24203cd86d6af15383)
* fix: link to IronOS page in hints. closes #42 [1cceff7](https://github.com/builder555/PineSAM/commit/1cceff7b2d9ac5188284ca793e094a97571f3dd9)
* feat: colour and icon change with temperature. closes #66 and #57 [72d0c87](https://github.com/builder555/PineSAM/commit/72d0c87025c78ee72ea90e5815e89450d00362c4)
* fix: only include what is needed for source package [3c2375e](https://github.com/builder555/PineSAM/commit/3c2375efe58e6df935d8420827cfe92d69c6dbfa)

## v1.8.4

* fix: use proper variables in source workflow [ed0ee5f](https://github.com/builder555/PineSAM/commit/ed0ee5f5b4fb7ee0ce43c35384830b642231a996)

## v1.8.3

* fix: update permissions. agian! [6ee7bec](https://github.com/builder555/PineSAM/commit/6ee7beca3845c3cf1c61a64274f881bbaa9e4742)

## v1.8.2

* fix: use new screenshot, remove versioned ones [478629e](https://github.com/builder555/PineSAM/commit/478629e131f6efbbb3743faca6de65d74bc1d3d3)

## v1.8.1

* Merge pull request #94 from builder555/master

update dev to master [622daa8](https://github.com/builder555/PineSAM/commit/622daa8366d0c864fc472686aa283e4f8f1fc321)
* fix: pack source as one of matrix strategies [bb38857](https://github.com/builder555/PineSAM/commit/bb38857034f8c2db39ba65d6819f66813ebaf57e)

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
