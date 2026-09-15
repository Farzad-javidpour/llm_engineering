from llm_engineering.llm import get_llm, LLMProvider


def main():

    print("Application started")

    print("Creating LLM...")

    llm = get_llm(LLMProvider.GEMINI)

    print("LLM created")

    response = llm.invoke(
        "what is langchain.in one sentence"
    )

    print()
    print("AI Response:")
    print(response.content)


if __name__ == "__main__":
    main()