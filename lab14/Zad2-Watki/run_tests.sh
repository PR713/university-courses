#!/bin/bash

EXEC=./main
pass=0
fail=0

test_case() {
    input="$1"
    expected="$2"
    result=$($EXEC "$input" 2>/dev/null)

    echo "== Test: input=$input, expected=$expected =="
    echo "ℹ️  received=$result"

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
    if [ -z "$1" ]; then
        $EXEC >/dev/null 2>&1
    else
        $EXEC "$1" >/dev/null 2>&1
    fi

    if [ $? -eq 0 ]; then
        echo "❌ Test failed: invalid input accepted"
        fail=$((fail+1))
    else
        echo "✅ Test passed: invalid input rejected"
        pass=$((pass+1))
    fi
}
# Testy poprawne
test_case 0 6
test_case 5 11
test_case -10 -4
test_case 100 106
test_case 123456 123462

# Testy błędne
invalid_case abc
invalid_case "12abc"
invalid_case ""
invalid_case

echo ""
echo "✅ Passed: $pass"
echo "❌ Failed: $fail"
