import cohere
import openziti
import argparse

def main():
    parser = argparse.ArgumentParser(description="Cohere Chat with OpenZiti")
    parser.add_argument("--message", type=str, required=True,help="The message to send to the Cohere chat model")
    parser.add_argument("--model", type=str, default="command-a-03-2025", help="The Cohere chat model to use \"command-a-03-2025\" by default")
    parser.add_argument("--api-key", type=str, required=True, help="The Cohere API key")
    parser.add_argument("--ziti-identity", type=str, required=True, help="The OpenZiti identity file")
    args = parser.parse_args()
    ztx = openziti.load(args.ziti_identity)

    with openziti.monkeypatch():
        co = cohere.Client(args.api_key)

        response = co.chat(
            model=args.model,
            message=args.message
        )

    print(response.text)

if __name__ == "__main__":
    main()