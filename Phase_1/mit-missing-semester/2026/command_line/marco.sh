#!/bin/bash

# The marco function saves the current path into a global variable
marco() {
    export MARCO_PATH=$(pwd)
    echo "Directory saved: $MARCO_PATH"
}

# The polo function uses that variable to jump back
polo() {
    if [ -z "$MARCO_PATH" ]; then
        echo "Error: You haven't executed 'marco' yet!"
    else
        cd "$MARCO_PATH" || return
        echo "Jumped to: $(pwd)"
    fi
}