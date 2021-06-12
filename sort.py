import json


def serialize(arr):
    """Serialize an array into a format the visualizer can understand."""
    formatted = {
        "kind": {"grid": True},
        "rows": [
            {
                "columns": [
                    {"content": str(value), "tag": str(value)} for value in arr
                ],
            }
        ],
    }
    return json.dumps(formatted)


arr = [1,3,6,7,2,3,5,4,1,0,9]

# Put serialized into the Debug Visualizer console
serialized = serialize(arr)

# Set a breakpoint on the line below and go through the code in debug mode to
# watch it update
for target_idx in range(1, len(arr)):
    target_value = arr[target_idx]
    compare_idx = target_idx - 1

    while compare_idx >= 0 and arr[compare_idx] > target_value:
        arr[compare_idx + 1] = arr[compare_idx]
        serialized = serialize(arr)
        compare_idx -= 1

    arr[compare_idx + 1] = target_value
    serialized = serialize(arr)

assert arr == sorted(arr)