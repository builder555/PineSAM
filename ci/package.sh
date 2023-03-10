#!/bin/bash

name=${1}

if [[ -z $1 ]]; then
  echo "usage: $0 Package-Name"
  exit 1
fi

zip_path="$(dirname "${PWD}")/${name}.zip"

pushd dist || exit
zip -r "${zip_path}" main_server/ serve/

popd || exit
zip -u "${zip_path}" start.sh version.txt

echo "asset_path=$zip_path" >> "$GITHUB_OUTPUT"
echo "asset_name=${name}.zip" >> "$GITHUB_OUTPUT"