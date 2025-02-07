#!/bin/bash
cd "$(dirname "$0")"

# ensure PineSAM binary is present
if [ ! -f ./PineSAM ] ; then
    echo "This file is used to run a built version of the project."
    echo "Please run setup-dev.sh and use run-dev.sh to run the project"
    exit
fi

if [ "$(uname)" == "Darwin" ]; then
    # for MacOS, remove the quarantine attributes
    # this is needed because the mac will not execute binaries that are downloaded from the internet
    # see https://developer.apple.com/library/archive/technotes/tn2459/_index.html
    if xattr -p com.apple.quarantine ./PineSAM >/dev/null 2>&1; then
        xattr -rd com.apple.quarantine ./PineSAM
    fi
fi

./PineSAM
