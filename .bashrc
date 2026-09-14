run_public() {
    read -p "Enter port number (Press ENTER for default 8080): " PORT
    PORT=${PORT:-8080}
    
    "$@" &
    PID=$!
    echo "Starting tool and launching public link for Port $PORT... please wait..."
    sleep 3
    ssh -R 80:localhost:$PORT localhost.run
}

