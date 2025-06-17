#!/bin/bash

SERVER_EXEC=./server
CLIENT_EXEC=./client
PORT=12345

# Upewnij się, że port jest wolny
lsof -i :$PORT -sTCP:LISTEN -t 2>/dev/null | xargs -r kill -9

# Uruchom serwer w tle
$SERVER_EXEC &
SERVER_PID=$!
sleep 1

pass=0
fail=0

test_case() {
    input="$1"
    expected="$2"
    result=$($CLIENT_EXEC "$input" 2>/dev/null)

    echo "== Test: input=$input, expected=$expected, received=$result =="

    if [ "$result" = "$expected" ]; then
        echo "✅ Test passed"
        pass=$((pass+1))
    else
        echo "❌ Test failed"
        fail=$((fail+1))
    fi
}

invalid_case() {
    echo "== Test: invalid input '$1' (should fail) =="
    if $CLIENT_EXEC "$1" >/dev/null 2>&1; then
        echo "❌ Test failed: invalid input accepted"
        fail=$((fail+1))
    else
        echo "✅ Test passed: invalid input rejected"
        pass=$((pass+1))
    fi
}

test_case 0 10
test_case 5 15
test_case -7 3
test_case 100 110
test_case 123456 123466

invalid_case abc
invalid_case "12abc"
invalid_case ""

echo "== Test: missing argument (should fail) =="
if $CLIENT_EXEC >/dev/null 2>&1; then
    echo "❌ Test failed: client accepted empty input"
    fail=$((fail+1))
else
    echo "✅ Test passed: empty input rejected"
    pass=$((pass+1))
fi

kill -9 $SERVER_PID 2>/dev/null
wait $SERVER_PID 2>/dev/null

echo ""
echo "✅ Passed: $pass"
echo "❌ Failed: $fail"

# if [ "$fail" -eq 0 ]; then
#     echo "🎉 All tests passed!"
#     exit 0
# else
#     echo "⚠️  Some tests failed."
#     exit 1
# fi