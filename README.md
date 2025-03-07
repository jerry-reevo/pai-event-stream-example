Minimal example demonstrating a work-around for `pydantic-ai` event streaming.

For context, see: https://github.com/pydantic/pydantic-ai/issues/640

```console
$ uv run src/pai/agent.py
Tool call: Getting weather...
Tool call result: 70 degrees and sunny
Text delta event: The current weather is
Text delta event:  70 degrees and sunny.
```

## To Run

1. `uv sync`
2. Add your API key to `src/pai/agent.py`
3. `uv run src/pai/agent.py`