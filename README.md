# WifiAutoReconnect

⭐ Linux Wi-Fi 自动重连工具，适用于使用 NetworkManager 管理网络接口的环境 ⭐

## 🍭 使用说明

1. 将本脚本克隆到本地

```bash
sudo mkdir -p /gitdirectory/ && sudo git clone --depth=1 https://gitlab.soraharu.com/XiaoXi/WifiAutoReconnect.git /gitdirectory/WifiAutoReconnect/
```

2. 编辑 root 用户的 crontab

```bash
crontab -e -u root
```

3. 在 crontab 文件底部新增以下定期执行脚本，请将脚本内的 `<your-ssid>` 替换成你希望自动重连的 Wi-Fi 的 SSID：

```bash
* * * * * python3 /gitdirectory/WifiAutoReconnect/detection.py "<your-ssid>"
```

4. Done.

## 📜 开源许可

基于 [MIT License](https://choosealicense.com/licenses/mit/) 许可进行开源。
