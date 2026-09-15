from src.llm_engineering.llm import get_llm, LLMProvider


def main():

    print("Application started")

    print("Creating LLM...")

    llm = get_llm(LLMProvider.OLLAMA)

    print("LLM created")

    response = llm.invoke(
        "LangChain چیست؟ در دو جمله توضیح بده."
    )

    print()
    print("AI Response:")
    print(response.content)


if __name__ == "__main__":
    main()