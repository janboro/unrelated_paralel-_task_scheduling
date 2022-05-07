# **Debugging Python code with Bazel**

## Configuring the Python debugger

First you need to configure a `launch.json` file inside VS Code. Go to `Run and Debug` and create one if it doesn't exist already:
Select `Python` -> `Remote attach` -> `localhost` -> `5678`.

The `launch.json` file should look like this:

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Python: Remote Attach",
            "type": "python",
            "request": "attach",
            "connect": {
                "host": "localhost",
                "port": 5678
            },
            "pathMappings": [
                {
                    "localRoot": "${workspaceFolder}",
                    "remoteRoot": "."
                }
            ],
            "justMyCode": true
        }
    ]
}
```

*__Note__: You are free to change the port number.*

In order to debug a python bazel target you need to use `ptvsd` as a dependency.

Therefore the `BUILD` file should look like this:

```bash
py_library(
    name = "utils",
    srcs = ["utilities.py"],
    deps = [
        "//third_party:ptvsd",
    ],
)
```

Afterwards place the following lines at the top of the python script you wish to debug:

```python
import ptvsd

ptvsd.enable_attach(address=('localhost', 5678), redirect_output=True)
print('Attach the debugger - Run: Python: Remote Attach')
ptvsd.wait_for_attach()
```

## Running the debugger

As a first step you need to run the test you wish to debug:

```bash
bazel run //path/to:target
```

The target won't run because it will be waiting for you to attache the debugger: go to `Run and Debug` and run the configuration.

## `Address already in use` error

You need to identify the `PID` of the process using the blocked port:

```bash
sudo lsof -i:5678
sudo kill PID
```

*Note*: Replace `PID` with the number outputted from the `lsof`.
