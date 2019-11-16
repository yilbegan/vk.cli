from cleo import Application

from vkc import __version__


default_commands = []


def main():
    app = Application("vk.cli", __version__)
    for command in default_commands:
        app.add(command)
    app.run()


if __name__ == "__main__":
    main()
