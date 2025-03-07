from dataclasses import dataclass
from pydantic_ai import Agent, RunContext

import os

from pai.proxy import AsyncIteratorProxy

os.environ["OPENAI_API_KEY"] = "sk-123"

@dataclass
class AgentDeps:
    event_stream: AsyncIteratorProxy

agent = Agent(
    model="gpt-4o-mini",
    system_prompt="You are a helpful assistant that can answer questions and help with tasks.",
    deps_type=AgentDeps,
)

@agent.tool
async def get_weather(ctx: RunContext[AgentDeps]):
    await ctx.deps.event_stream.emit("Getting weather...")
    await asyncio.sleep(2)
    weather = "70 degrees and sunny"
    await ctx.deps.event_stream.emit(weather)
    return weather

async def main():
    deps = AgentDeps(event_stream=AsyncIteratorProxy(asyncio.Queue()))
    asyncio.create_task(run_agent(deps))
    async for event in deps.event_stream:
        print(event)

async def run_agent(deps: AgentDeps):
    async with agent.run_stream("What is the current weather?", deps=deps) as stream:
        async for message in stream.stream_text(delta=True):
            await deps.event_stream.emit(f"Text delta event: {message}")
    await deps.event_stream.close()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())

