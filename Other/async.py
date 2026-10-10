import asyncio, time

async def brew_coffee() -> str:
    print('Starting to brew coffee...')
    await asyncio.sleep(3)
    print('Brewing done!')
    return 'Coffee ready!'
    
async def toast_bagel() -> str:
    print('Staring to toast bagel...')
    await asyncio.sleep(2)
    print('Toasting done!')
    return 'Bagel ready!'

# This program is a demonstration of async programming using the 'asyncio' module
async def main() -> None:
    start_time: int = time.time()
    batch = asyncio.gather(brew_coffee(), toast_bagel())
    result_coffee, result_bagel = await batch
    end_time: int = time.time()
    elapsed_time: float = end_time - start_time
    print(f'Results of brew_coffee(): {result_coffee}')
    print(f'Results of toast_bagel(): {result_bagel}')
    print(f'Elapsed time: {elapsed_time:.2f}s')

if __name__ == '__main__':
    asyncio.run(main())
