# Introduction
### 均一網站自動答題腳本（Junyi Auto Answer Script）

此專案針對 [均一教育平台](https://www.junyiacademy.org/) 的部分線上測驗提供自動化答題功能，透過 **Selenium + Requests** 完成資料擷取與自動作答。  
使用者只需要貼上該測驗的 URL 即可運行腳本。

此專案是由先前版本重構而成：  
https://github.com/yueee69/spider/blob/master/spider/spider.py  

重構內容包含：
- 專案模組化、OOP 化
- 提高程式可維護性與可讀性
- 重寫與優化判題算法，提升穩定性

目前支援 **高中端**與**國小端**測驗。

---

# Features
- 在終端機輸入題目 URL 即可自動答題  
- 使用 Selenium 控制瀏覽器進行作答  
- 透過 Requests 取得題庫資料並與題目比對  
- 未來規劃新增：
  - GUI
  - 設定介面（如模式選擇、錯題策略等）
  - 完整用戶使用流程，不再依賴終端機

---

# Installation
你可以直接clone this repo:

```bash
git clone https://github.com/yueee69/JunYi_auto_answer_script
```

然後定位到此專案

```bash
cd JunYi_auto_answer_script/src
```

接著下載所需套件：

```bash
pip install -r requirements.txt
```

然後定位到src/中(可選)
```bash
cd src
```

---

# Usage
請在確認Installation沒有問題後，可以直接執行：

```bash
python main.py
```

或是

```bash
python src/main.py
```

---

# 檔案架構
```
JunYi_auto_answer_script
├── src/
│    ├── config/        #常數、用戶設定json以及manager統一管理
│    ├── core/          #app.py進入點
│    ├── gui/           #用戶交互gui，尚未實作
│    ├── driver/        #核心判題模塊
│    ├── utils/         #各種小工具
├── tests/              #pytest進入點
│    ├── unit_test      #小單元測試
│    ├── integration    #api交互測試
│    ├── e2e            #端對端測試
└── main.py             #專案進入點
```