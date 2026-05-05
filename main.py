from agent import Agent

agent = Agent()

print("AI Study Assistant Started")
print("Type 'exit' to quit")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        break

    response = agent.process(user_input)
    print("Assistant:", response)