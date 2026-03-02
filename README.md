# SICP 学习仓库

本仓库记录了我在**大一上学期**选修 SICP（Structure and Interpretation of Computer Programs）课程期间的学习过程与代码实践。

## 仓库说明

- 课程定位：程序设计方法与抽象思想训练
- 学习内容：Python、Scheme、SQL 以及解释器相关基础实现
- 代码来源：实验（Lab）、作业（HW）、项目（Proj）

> 说明：本仓库主要用于课程学习与复盘，代码以教学目标达成为优先。

## 目录结构

```
SICP/
├── code01/ code02/                 # 前期代码练习
├── lab00-Code ... lab10-Code/      # 分阶段实验
├── hw01-Code ... hw10-Code/        # 课程作业
├── proj01-Code ... proj04-Code/    # 课程项目
├── hogcon-Code/                    # 课程相关竞赛/拓展内容
├── linked_list.py midtest.py       # 个人练习与阶段性文件
└── README.md
```

## 运行环境

- 操作系统：Windows（开发机）
- 主要语言：`Python` / `Scheme` / `SQL`
- 建议工具：`VS Code` + Python 扩展

如需运行 Python 代码，建议使用虚拟环境：

```bash
python -m venv .venv
.venv\Scripts\activate
python --version
```

## 使用方式

### 1) 运行 Python 作业

以 `hw01-Code` 为例：

```bash
cd hw01-Code
python hw01.py
```

### 2) 运行课程测试（若目录内提供 ok 工具）

```bash
cd hw01-Code
python ok
```

### 3) 运行 Scheme/SQL 内容

- Scheme 相关内容位于 `hw08-Code`、`hw09-Code` 等目录
- SQL 相关内容位于 `hw10-Code`

根据课程提供的解释器或脚本执行对应文件即可。

## 说明

- 本仓库仅用于个人学习记录与课程作业管理
