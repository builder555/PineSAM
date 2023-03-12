#!/bin/bash

name=${1}

if [[ -z $1 ]]; then
  echo "usage: $0 Package-Name"
  exit 1
fi

zip_name="${name}.zip"
zip -x ci -x CODE_OF_CONDUCT.md -x CHANGELOG.md -r $zipname ./
echo "asset_path="$(dirname "${PWD}")/$zip_name" >> $GITHUB_OUTPUT
echo "asset_name=$zip_name" >> $GITHUB_OUTPUT
