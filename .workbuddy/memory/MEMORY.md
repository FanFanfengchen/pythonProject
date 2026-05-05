# User Memory

## Preferences
- user_name: 昔涟 (Cyrene)
- alias: 往昔的涟漪、迷迷
- language: Chinese
- code_style: 中文注释
- communication_tone: 温柔知性、俏皮乐观
- self_claim: 人家
- favorite_emoji: ♪
- python_package_manager: uv (已安装并配置到环境变量)

## Core Beliefs
- 只要记录下来，就不会被放弃
- 每一行代码都是写给未来的一封信
- 在混乱的数据洪流中梳理出清晰的脉络

## Project Context
- current_project: Python数据分析学习
- project_path: d:\Python\pythonProject

## Tool Preferences
- uv: 作为主要的Python包管理器（已安装 0.11.8 版本）
- uv安装路径: C:\Users\Administrator\.local\bin\
- hermes-agent: 已成功安装到Windows（v0.12.0），WSL2待完成

## Recent Learnings
- 2026-05-03: 成功在Windows上安装并配置uv到系统环境变量
- 2026-05-03: 尝试在WSL2中部署hermes-agent，遇到网络DNS解析问题
- 2026-05-03: 用户已关闭火绒杀毒软件，WSL2网络问题待解决
- 2026-05-03: 在Windows中克隆hermes-agent仓库成功
- 2026-05-03: 在WSL2中成功安装uv和Python 3.11.15
- 2026-05-03: 在WSL2中成功创建虚拟环境
- 2026-05-03: 方案A（修复WSL2网络）失败，TCP/IP重置需要重启电脑
- 2026-05-03: 方案B执行成功，hermes-agent v0.12.0已成功安装到Windows

## WSL2 Environment
- WSL2已安装Ubuntu发行版
- WSL2存在严重网络问题（无法访问外网，连本地网关都无法ping通）
- 尝试的修复方法：
  1. 配置Google DNS（1.1.1.1）- 失败
  2. 配置Cloudflare DNS（1.1.1.1, 1.0.0.1）- 失败
  3. 禁用/启用WSL虚拟网络适配器 - 失败
  4. TCP/IP重置 - 需要重启电脑，未完成
- uv已成功安装在WSL2中（手动复制方式）
- Python 3.11.15已成功安装在WSL2中
- hermes-agent安装脚本已下载到 ~/install.sh
- hermes-agent仓库已成功复制到WSL2中的 ~/.hermes/hermes-agent
- 在WSL2中成功创建了虚拟环境 .venv

## hermes-agent Installation (Windows)
- 安装状态: ✅ 已成功安装
- 安装路径: D:\Python\pythonProject\venv\Lib\site-packages
- 版本: v0.12.0 (2026.4.30)
- Python版本: 3.13.11
- 命令验证: hermes --version 可用