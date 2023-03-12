#!/bin/bash

name=${1}

if [[ -z $1 ]]; then
  echo "usage: $0 Package-Name"
  exit 1
fi

zip_name="${name}.zip"
zip --verbose -x ci -x CODE_OF_CONDUCT.md -x CHANGELOG.md -r $zip_name ./
zip_path=$(realpath "$zip_name")
echo "asset_path=$zip_path" >> $GITHUB_OUTPUT
echo "asset_name=$zip_name" >> $GITHUB_OUTPUT
