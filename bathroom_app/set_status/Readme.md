
## Set Status (set_status.py)
This function will set the vacant or occupied status of a bathroom.

The bathroom record must exist for this to work.

### Payloads to test in lambda

Set a bathroom status to occupied:
```
{
    "request": "set_occupied",
    "bathroom": 2,
    "gender": "F",
    "stall": 10
}
```

Set a bathroom status to vacant:
```
{
    "request": "set_vacant",
    "bathroom": 2,
    "gender": "F",
    "stall": 10
}
```

Throw an exception for invalid requests:
```
{
    "request": "foobar",
    "bathroom": 2,
    "gender": "F",
    "stall": 10
}
```
```
{
    "request": "set_vacant",
    "bathroom": 2,
    "gender": "F1",
    "stall": 10
}
```

### Payload to test locally

One of these to the bottom of the file:

Set a bathroom status to occupied:
```
dict_request = {
    'request': 'set_occupied',
    'bathroom': 2,
    'gender': 'F',
    'stall': 10
}
lambda_handler(dict_request, {})
```


Set a bathroom status to vacant:
```
dict_request = {
    'request': 'set_vacant',
    'bathroom': 2,
    'gender': 'F',
    'stall': 10
}
lambda_handler(dict_request, {})
```


Throw an exception for invalid requests:
```
dict_request = {
    'request': 'foobar',
    'bathroom': 2,
    'gender': 'F',
    'stall': 10
}
lambda_handler(dict_request, {})
```
```
dict_request = {
    'request': 'set_vacant',
    'bathroom': 2,
    'gender': 'F1',
    'stall': 10
}
lambda_handler(dict_request, {})
```