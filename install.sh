#!/bin/bash

echo "🚀 INSTALL TAGALL BOT..."

# ===== UPDATE SYSTEM =====
apt update -y && apt upgrade -y

# ===== INSTALL PYTHON =====
apt install python3 python3-pip -y

# ===== INSTALL LIB =====
pip3 install telethon

# ===== BUAT FOLDER =====
mkdir -p /root/tagallbot
cd /root/tagallbot

# ===== BUAT BOT FILE =====
cat > bot.py << 'EOF'
# ===== SIMPLE START BOT (LO GANTI NANTI) =====
print("BOT FILE READY")
EOF

# ===== BUAT DATABASE =====
cat > data.json << 'EOF'
{
  "partners": {},
  "groups": [],
  "status": true
}
EOF

# ===== BUAT SERVICE =====
cat > /etc/systemd/system/tagallbot.service << 'EOF'
[Unit]
Description=Telegram Tagall Bot
After=network.target

[Service]
User=root
WorkingDirectory=/root/tagallbot
ExecStart=/usr/bin/python3 /root/tagallbot/bot.py
Restart=always
RestartSec=3
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
EOF

# ===== RELOAD SYSTEMD =====
systemctl daemon-reexec
systemctl daemon-reload

# ===== ENABLE SERVICE =====
systemctl enable tagallbot

# ===== START BOT =====
systemctl start tagallbot

echo "✅ INSTALL SELESAI!"
echo "👉 Edit bot di: /root/tagallbot/bot.py"
echo "👉 Cek status: systemctl status tagallbot"
echo "👉 Cek logs: journalctl -u tagallbot -f"
