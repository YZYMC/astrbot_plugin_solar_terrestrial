from astrbot.api.event import filter, AstrMessageEvent, MessageEventResult
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

@register("astrbot_plugin_solar_terrestrial", "yzymc", "一个简单的插件，可以提供太阳活动和传播状态等信息。", "2.1.0")
class MyPlugin(Star):
    def __init__(self, context: Context):
        super().__init__(context)

    async def initialize(self):
        """可选择实现异步的插件初始化方法，当实例化该插件类之后会自动调用该方法。"""
    
    # 注册指令的装饰器。指令名为 helloworld。注册成功后，发送 `/helloworld` 就会触发这个指令，并回复 `你好, {user_name}!`
    @filter.command("s")
    async def s(self, event: AstrMessageEvent):
        """获取 solarn0nbh 图像""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        yield event.image_result("https://www.hamqsl.com/solarn0nbh.php") # 发送图像。
        
    @filter.command("sp")
    async def sp(self, event: AstrMessageEvent):
        """获取 solarpic 图像""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        yield event.image_result("https://www.hamqsl.com/solarpic.php") # 发送图像。

    @filter.command("ss")
    async def ss(self, event: AstrMessageEvent):
        """获取 solarsystem 图像""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        yield event.image_result("https://www.hamqsl.com/solarsystem.php") # 发送图像。

    @filter.command("bs")
    async def bs(self, event: AstrMessageEvent):
        """获取 sun 图像""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        yield event.image_result("https://www.hamqsl.com/solarsun.php") # 发送图像。

    @filter.command("muf")
    async def muf(self, event: AstrMessageEvent):
        """获取 MUF Map""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        import cairosvg

        # 转换为PNG
        cairosvg.svg2png(
            url="https://prop.kc2g.com/renders/current/mufd-normal-now.svg",
            write_to="muf.png"
        )
        
        yield event.image_result("muf.png") # 发送图像。
    
    @filter.command("help")
    async def help(self, event: AstrMessageEvent):
        """获取帮助信息（YZYNetwork麦麦）""" # 这是 handler 的描述，将会被解析方便用户了解插件内容。建议填写。
        yield event.plain_result(f"YZYNetwork麦麦-菜单\n\n/s 获取太阳活动和传播情况图\n/sp 获取太阳活动图\n/ss 获取星系图\n/bs 获取太阳图\n/muf 获取MUF地图\n/weather 请用'/weather help'获取详细信息\n/status 获取YZYNetwork-BJ1服务器状态\n/抽取 随机抽取一位群成员\nEmojiMix：发送两个Emoji来触发。\n\n此外，您还可以和“麦麦”进行对话。")

    
    async def terminate(self):
        """可选择实现异步的插件销毁方法，当插件被卸载/停用时会调用。"""
