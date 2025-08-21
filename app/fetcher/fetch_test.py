import asyncio

from app.fetcher import DataFetcher, Database


async def main() -> None:
    fetcher = DataFetcher(Database())
    tweets = await fetcher.list()
    for i, j in enumerate(tweets):
        print(f"{i}.\n{j}")


if __name__ == '__main__':
    asyncio.run(main())
