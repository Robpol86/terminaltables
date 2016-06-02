#!/bin/bash
# Trigger building of docs in the gh-pages branch.

set -e  # Exit immediately if a command exits non-zero.
set -f  # Disable filename expansion (globbing).
set -u  # Treat unset variables as an error.
set -o pipefail  # Fail if any commands in a pipeline exits non-zero.

prefix="AUTO Travis $TRAVIS_BUILD_ID"
travis_disabled=".disabled.travis.yml"
travis_enabled=".travis.yml"

# Set/decrement recursion limit.
if [ -z ${RETRIES_LEFT+placeholder} ]; then
    export RETRIES_LEFT=3
else
    ((RETRIES_LEFT--))
fi

# Push or retry.
function push {
    if git push --atomic origin gh-pages; then
        echo "Success"
        return 0
    fi
    if (( $RETRIES_LEFT > 0 )); then
        popd  # Go back to original directory before entering mktemp dir.
        ./$0  # Re-run script.
        return 0
    fi
    return 1
}

# Clone the repo into empty directory and cd into it.
pushd $(mktemp -d)
git clone --depth=1 --branch=gh-pages "https://github.com/$TRAVIS_REPO_SLUG.git" .
if [ ! -e "$travis_disabled" ]; then
    if [ ! -e "$travis_enabled" ]; then
        echo "No Travis YAML file present. Aborting!"
        exit 1
    fi
    echo "File .disabled.travis.yml does not exist. Trying again in 10 seconds."
    sleep 10
    git pull
    if [ ! -e "$travis_disabled" ]; then
        echo "File still does't exist. Triggering with empty commit."  # Possible gh-pages job failure.
        git commit --allow-empty -m "$prefix: Empty commit to trigger build."
        push
        exit $?
    fi
fi

# Enable Travis CI for gh-pages.
git mv "$travis_disabled" "$travis_enabled"
git commit -m "$prefix: Enabling Travis CI."
push
exit $?
