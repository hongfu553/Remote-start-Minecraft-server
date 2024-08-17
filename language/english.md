# Remote Start Minecraft Server Discord Bot

This README provides instructions on how to set up and use a Discord bot to remotely start your Minecraft server.

## Prerequisites

* A created Discord bot
* Python installed
* Source code downloaded

## Steps

1. **Obtain Discord Bot Token**
    * Refer to [This page](https://www.toptal.com/chatbot/how-to-make-a-discord-bot) tutorial to create a Discord bot and obtain the token.
    * **Make sure to save your token, as it is the unique identifier for your bot.**

2. **Install Dependencies**
    * Open the Command Prompt (CMD) in the directory where the source code is extracted.
    * Enter the following command to install the required packages:
        ```bash
        pip install -r requirements.txt
        ```

3. **Modify the `run.bat` File in Minecraft**
    * Replace the `pause` at the end of the official file with `exit`.
    * Example:
        ```bash
        @echo off
        REM Forge requires a configured set of both JVM and program arguments.
        REM Add custom JVM arguments to the user_jvm_args.txt
        REM Add custom program arguments {such as nogui} to this file in the next line before the %* or
        REM  pass them to this script directly
        java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.2.0/win_args.txt %*
        exit
        ```

4. **Create a Shortcut for Minecraft Server Start**
    * In the source code directory, create a shortcut to your Minecraft server start file.
    * **Ensure the shortcut file is located in the same directory as `Remote_server.pyw`.**

5. **Set Up Bot Token**
    * In the `Remote_server.pyw` file, find and modify the `token` variable, replacing its value with your Discord bot token.

6. **Start the Bot**
    * In the Command Prompt (CMD), enter the following command to start the bot:
        ```bash
        python Remote_server.pyw
        ```

7. **Completion**
    * Your Discord bot should now be connected to your Discord server.
    * Enter `%server_start` in your Discord server to remotely start the Minecraft server.
    * Enter `%TM` to view server system resource usage

## Auto-Startup (Windows)

1. **Create a Shortcut for Remote_server.pyw**
2. **Open "Run" (win + R)**
3. **Enter "shell:startup"**
4. **Place the shortcut file in the "startup" folder**

## Notes

* It is recommended to stop the server using `stop` instead of (ctrl+C).
* This project is only applicable to Windows systems.
* Ensure that your Minecraft server start file has execution permissions.
* All Minecraft versions are supported.

## Contributing

Contributions to this project are welcome! Please submit your changes via a pull request.