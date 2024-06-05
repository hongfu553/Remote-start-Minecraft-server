# 遠端啟動 Minecraft 伺服器的 Discord Bot

這個 README 文件說明如何設定和使用 Discord bot 來遠端啟動你的 Minecraft 伺服器。

## 前提條件

* 已經創建一個 Discord bot
* 已經安裝 Python
* 已下載源代碼

## 步驟

1. **取得 Discord Bot Token**
    * 參考 [小 Shawn 的 HackMD](https://hackmd.io/@smallshawn95/python_discord_bot_base) 教學創建 Discord bot 並取得 token。
    * **請務必保存你的 token，因為它是你 bot 的唯一識別碼。**

2. **安裝依賴套件**
    * 在解壓縮的源代碼目錄下，開啟命令提示字元 (CMD) 
    * 輸入以下命令安裝所需的套件：
        ```bash
        pip install -r requirements.txt
        ```

3. **建立 Minecraft 伺服器啟動捷徑**
    * 在源代碼目錄中，建立你的 Minecraft 伺服器啟動檔案的捷徑。
    * **確保捷徑文件與 `Remote_server.pyw` 檔案位於同一目錄中。**

4. **設定 Bot Token**
    * 在 `Remote_server.pyw` 檔案中，找到並修改 `token` 變數，將其值替換為你的 Discord bot token。

5. **啟動 Bot**
    * 在命令提示字元 (CMD) 中，輸入以下命令啟動 bot：
        ```bash
        python Remote_server.pyw
        ```

6. **完成**
    * 你的 Discord bot 現在應該已經連線到你的 Discord 伺服器。
    * 你可以用 `/start` 指令來啟動你的 Minecraft 伺服器。
    * 你可以用 `/stop` 指令來停止你的 Minecraft 伺服器。

## 開機自啟動 (Windows)

1. **建立 Remote_server.pyw 捷徑**
2. **開啟「執行」 (win + R)**
3. **輸入「shell:startup」**
4. **將捷徑文件放置到「startup」資料夾中**

## 注意

* 此項目僅適用於 Windows 系統。
* 確保你的 Minecraft 伺服器啟動檔案具有執行權限。

## 貢獻

歡迎對這個專案做出貢獻！請透過 pull request 提交你的更改。

## 授權

此專案使用 [MIT 授權](https://opensource.org/licenses/MIT)。