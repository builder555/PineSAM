#!/bin/bash

name=${1}

if [[ -z $1 ]]; then
  echo "usage: $0 Package-Name"
  exit 1
fi

zip_path="$(dirname "${PWD}")/${name}.zip"

pushd dist || exit
zip -r "${zip_path}" Pinecil

popd || exit
zip -u -j "${zip_path}" ci/start.sh

echo "asset_path=$zip_path" >> "$GITHUB_OUTPUT"
echo "asset_name=${name}.zip" >> "$GITHUB_OUTPUT"
