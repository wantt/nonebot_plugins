from os import path

import nonebot

import config


if __name__ == '__main__':
    nonebot.init(config)

    nonebot.load_plugins(
            path.join(path.dirname(__file__),'awesome','plugins'),
            'awesome.plugins'
            
            )

    nonebot.load_builtin_plugins()
    nonebot.run(host='0.0.0.0', port=8080)


