Minimal example demonstrating a work-around for `pydantic-ai` event streaming.

For context, see: https://github.com/pydantic/pydantic-ai/issues/640

```console
$ uv run src/pai/agent.py
Getting weather...
Weather: 70 degrees and sunny
Text delta event: I'm currently unable to
Text delta event:  retrieve the weather information. You may want to check a reliable weather website or app for the latest updates
Text delta event: . If there's anything else I can assist you with, please
Text delta event:  let me know!
```

## To Run

1. `uv sync`
2. Add your API key to `src/pai/agent.py`
3. `uv run src/pai/agent.py`