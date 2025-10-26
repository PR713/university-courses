#!/bin/bash

FIFO_PATH="./myfifo"

run_test () {
    local buffer_size=$1
    local message="$2"
    local description="$3"

    echo "Testing: $description"
    echo "Buffer size: $buffer_size"
    echo "Message: '$message'"

    ./reader $FIFO_PATH $buffer_size &
    local READER_PID=$!
    sleep 1

    if ! ps -p $READER_PID > /dev/null; then
        echo "Reader failed to start."
    else
        ./writer $FIFO_PATH "$message"
    fi

    wait $READER_PID
    echo "Test done."
    echo ""
}

make
rm -f $FIFO_PATH
mkfifo $FIFO_PATH

run_test 100 "Short message" "small buffer and short message"
run_test 1024 "Short message" "large buffer and short message"
run_test 10 "This is a very long message that exceeds the buffer size to test partial reads and writes." "small buffer and long message"
run_test 34 "Exactly thirty-four characters!" "buffer size exactly matching message length"
run_test 1 "Msg" "extremely small buffer size"
run_test 50 "This should not fail" "normal length message"

rm -f $FIFO_PATH
