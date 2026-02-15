import asyncio
from memu_sdk import MemUClient
from dotenv import load_dotenv


load_dotenv() 
api_key=os.getenv("memU_API_KEY")

async def main():
    # Initialize the client
    async with MemUClient(api_key=api_key) as client:
        # Memorize a conversation
        result = await client.memorize(
            conversation=[
                {"role": "user", "content": "I love Italian food, especially pasta."},
                {"role": "assistant", "content": "That's great! What's your favorite dish?"},
                {"role": "user", "content": "Carbonara is my absolute favorite!"}
            ],
            user_id="user_123",
            agent_id="my_assistant",
            wait_for_completion=True
        )

        print(f"Task ID: {result.task_id}")

        # Retrieve memories
        memories = await client.retrieve(
            query="What food does the user like?",
            user_id="user_123",
            agent_id="my_assistant"
        )

        print(f"Found {len(memories.items)} relevant memories")
        for item in memories.items:
            print(f"  - [{item.memory_type}] {item.content}")

asyncio.run(main())