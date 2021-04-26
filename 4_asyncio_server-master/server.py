import asyncio

HOST = 'localhost'


async def handle_echo(reader, writer):
    data = await reader.read(100)
    writer.write(data)
    await writer.drain()

    writer.close()

loop = asyncio.get_event_loop()
port = int(input("Введите номер порта:"))
coro = asyncio.start_server(handle_echo, HOST, port, loop=loop)
server = loop.run_until_complete(coro)

# Serve requests until Ctrl+C is pressed
print('Serving on {}'.format(server.sockets[0].getsockname()))
try:
    loop.run_forever()
except KeyboardInterrupt:
    pass

# Close the server
server.close()
loop.run_until_complete(server.wait_closed())
loop.close()