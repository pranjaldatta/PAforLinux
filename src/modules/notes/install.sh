#!/bin/bash

function assertInstalled() {
    for var in "$@"; do
        if ! which $var &> /dev/null; then
            echo "$var is required but not installed, exiting."
            exit 1
        fi
    done
}

function checkNotesInstalled() {

    if [ -e /usr/local/bin/notes ]
    then 
        if [ -d /usr/share/bash-completion/completions ]
        then  
            echo 0
        else    
            echo 3
        fi
    else    
        echo 2 
    fi       
}


echo "Checking for dependencies..."
assertInstalled bash curl tar mktemp install make


if [ "$1" == "i" ]
then 
    echo "Installing notes ..."
    curl https://raw.githubusercontent.com/pimterry/notes/latest-release/notes > /usr/local/bin/notes && chmod +x /usr/local/bin/notes
    echo "Installing autocompletions ..."
    curl https://raw.githubusercontent.com/pimterry/notes/latest-release/notes.bash_completion > /usr/share/bash-completion/completions/notes
elif [[ "$1" == "u" ]] && [[ "$2" == "--all" ]]
then
    ret_val=$(checkNotesInstalled)
    if [[ $ret_val == 2 ]] || [[ $ret_val == 3 ]]
    then
        echo "doesnt exist"
        exit 1
    else    
        echo "removing notes source and autocompletions ..."
        #deleting from path
        rm -rf /usr/local/bin/notes
        #deleting autocompletions from /usr/share/bash-completion/completions/notes
        rm -rf /usr/share/bash-completion/completions/notes
        echo "removing stored notes"
        rm -rf "~/notes"
    fi    
elif [ "$1" == "u" ]
then
    ret_val=$(checkNotesInstalled)
    if [[ $ret_val == 2 ]] || [[ $ret_val == 3 ]]
    then    
        echo "Doesnt exist"
        exit 1
    else    
        echo "removing notes source and autocompletions ..."
        #deleting from path
        rm -rf /usr/local/bin/notes
        #deleting autocompletions from /usr/share/bash-completion/completions/notes
        rm -rf /usr/share/bash-completion/completions/notes
fi
fi




