[English version](/language/english.md)
# 遠端啟動 Minecraft 伺服器的 Discord Bot

這個 README 文件說明如何設定和使用 Discord bot 來遠端啟動你的 Minecraft 伺服器。

## 前提條件

* 已經創建一個 Discord bot
* 已經安裝 Python
* 已下載源代碼

## 步驟

1. **取得 Discord Bot Token**
    * 參考 [@smallshawn95 的 HackMD](https://hackmd.io/@smallshawn95/python_discord_bot_base) 教學創建 Discord bot 並取得 token。
    * **請務必保存你的 token，因為它是你 bot 的唯一識別碼。**

2. **安裝依賴套件**
    * 在解壓縮的源代碼目錄下，開啟命令提示字元 (CMD) 
    * 輸入以下命令安裝所需的套件：
        ```bash
        pip install -r requirements.txt
        ```

3. **修改 Minecraft裡面的 `run.bat`文件**
    * 將官方的文件裡面結尾`pause`，改成 `exit`
    * 以下範例:
        ```bash
        @echo off
        REM Forge requires a configured set of both JVM and program arguments.
        REM Add custom JVM arguments to the user_jvm_args.txt
        REM Add custom program arguments {such as nogui} to this file in the next line before the %* or
        REM  pass them to this script directly
        java @user_jvm_args.txt @libraries/net/minecraftforge/forge/1.20.1-47.2.0/win_args.txt %*
        exit
        ```

4. **建立 Minecraft 伺服器啟動捷徑**
    * 在源代碼目錄中，建立你的 Minecraft 伺服器啟動檔案的捷徑。
    * **確保捷徑文件與 `Remote_server.pyw` 檔案位於同一目錄中。**

5. **設定 Bot Token**
    * 在 `Remote_server.pyw` 檔案中，找到並修改 `token` 變數，將其值替換為你的 Discord bot token。

6. **啟動 Bot**
    * 在命令提示字元 (CMD) 中，輸入以下命令啟動 bot：
        ```bash
        python Remote_server.pyw
        ```

7. **完成**
    * 你的 Discord bot 現在應該已經連線到你的 Discord 伺服器。
    * 在Discord伺服器內輸入 `%server_start` 即可遠端啟動伺服器
    * 輸入 `%TM` 可查看伺服器系統資源佔用

## 開機自啟動 (Windows)

1. **建立 Remote_server.pyw 捷徑**
2. **開啟「執行」 (win + R)**
3. **輸入「shell:startup」**
4. **將捷徑文件放置到「startup」資料夾中**

## 注意

* 停止伺服器建議輸入`stop`而非使用 (ctrl+C)
* 此項目僅適用於 Windows 系統。
* 確保你的 Minecraft 伺服器啟動檔案具有執行權限。
* 每個Minecraft版本皆可以使用

## 貢獻

歡迎對這個專案做出貢獻！請透過 pull request 提交你的更改。