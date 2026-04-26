pidwait() {
    # Check if a PID was provided
    if [ -z "$1" ]; then
        echo "Usage: pidwait <PID>"
        return 1
    fi

    local pid=$1

    # Loop as long as kill -0 returns 0 (Success = Process Exists)
    while kill -0 "$pid" 2>/dev/null; do
        # Sleep to prevent the loop from maxing out a CPU core
        sleep 1
    done

    echo "Process $pid has completed."
}