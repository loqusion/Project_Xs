import asyncio

from joycontrol.protocol import controller_protocol_factory
from joycontrol.server import create_hid_server
from joycontrol.controller import Controller
from joycontrol.controller_state import ControllerState, button_push, button_press, button_release

async def main():
    # switch's btaddr
    switch_bt_addr = "DC:68:EB:AF:50:BC"
    # the type of controller to create
    controller = Controller.PRO_CONTROLLER # or JOYCON_L or JOYCON_R
    # a callback to create the corresponding protocol once a connection is established
    factory = controller_protocol_factory(controller)
    # start the emulated controller
    transport, protocol = await create_hid_server(factory, reconnect_bt_addr = switch_bt_addr)
    # get a reference to the state beeing emulated.
    controller_state = protocol.get_controller_state()
    # wait for input to be accepted
    await controller_state.connect()
    # press button
    await asyncio.sleep(0.3)
    # await button_push(controller_state,"home")
    # await asyncio.sleep(0.1)
    # await button_push(controller_state,"home")
    # await asyncio.sleep(3)
    print("home")
    await button_push(controller_state,"home")
    await button_push(controller_state,"home")
    await button_push(controller_state,"home")
    await asyncio.sleep(2.5)
    await button_push(controller_state,"b")
    await asyncio.sleep(1.5)
    await button_push(controller_state,"x")
    await asyncio.sleep(1)
    for _ in range(10):
        await button_push(controller_state,"a")
        print("A")
        await asyncio.sleep(1.5)
        await button_push(controller_state,"b")
        print("B")
        await asyncio.sleep(1)
    await asyncio.sleep(0.7)
    await button_push(controller_state,"b")
    await asyncio.sleep(1.7)
    print("p")
    await button_push(controller_state,"plus")
    await button_push(controller_state,"plus")
    await asyncio.sleep(0.7)
    print("r")
    await button_push(controller_state,"right")
    await button_push(controller_state,"right")
    await asyncio.sleep(1.7)
    print("a")
    await button_push(controller_state,"a")
    await button_push(controller_state,"a")
    await asyncio.sleep(1.7)
    print("home")
    await button_push(controller_state,"home")
    await button_push(controller_state,"home")
    await button_push(controller_state,"home")
    await asyncio.sleep(2.5)
    # await asyncio.sleep(0.5)
    # await button_push(controller_state,"a")
    input()

if __name__ == "__main__":
    asyncio.run(main())