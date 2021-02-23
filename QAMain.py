import urllib.request as req
import bs4
import time
import pyautogui
import selenium
import sys
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

##---初始化載入(Initializer)---##
# 非Slot的gameType清單
passNotSlot = ["Baccarat2",
    "Baccarat5T2",
    "Baccarat5T2FHD",
    "Baccarat6T2",
    "Baccarat6T2FHD",
    "Baccarat7T",
    "Baccarat7TFHD",
    "Baccarat8T2",
    "Baccarat8T2FHD",
    "BaccaratCommissionFree2",
    "BaccaratCommissionFree2FHD",
    "Bairenniuniu",
    "BenzBMW",
    "BenzBMWFHD",
    "BigWheel",
    "BlackJack",
    "CaribbeanStudPoker",
    "DeucesWild",
    "DragonPhoenix",
    "DragonPhoenixFHD",
    "DragonTiger",
    "EZBaccarat",
    "EZBaccaratFHD",
    "ForestDance",
    "GoldenShark",
    "GoldenSharkFHD",
    "HooHeyHow",
    "InternationalSicbo",
    "JourneytotheWest",
    "KingsQueen",
    "KingsQueenFHD",
    "LittleMarry",
    "LittleMarryFHD",
    "LittleMarry1",
    "LongSuperBaccarat",
    "LongSuperBaccaratFHD",
    "Lucky5",
    "MakccaratCommission",
    "MakccaratNonCommission",
    "PigRace",
    "RichRunner",
    "ShotDragon",
    "SuperBaccarat6T",
    "SuperBaccarat6TFHD",
    "SuperNewBaccarat6T",
    "SuperNewBaccarat6TFHD",
    "TaiSicbo",
    "TwSicbo",
    "Wheel",
    "XocDia",
    "JpFishing",
    "CherryMaster",
    "LuckySicbo",
    "CallOfNaughtyRacing",
    "FastballMatch",
    "TGFishShrampCrab",
    "TGLuckyWheel",
    "TGNiuNiu",
    "TGSicBo",
    "ForestDanceBNG",
    "GoldRacecourse",
    "HooHeyHowBNG",
    "LuckyRoulette",
    "MonkeyThunderbolt",
    "DamanguanSicbo",
    "Baccarat7TIF",
    "EZBaccaratIF",
    "InternationalSicboIF",
    "Lucky5IF",
    "DragonTigerIF",
    "ShotDragonIF",
    "KingsQueenIF",
    "GoldenSharkIF",
    "HooHeyHowIF",
    "BlackJackIF",
    "DInitialDIF",
    "KartRiderIF",
    "ForestDanceIF",
    "CrazyTime",
    "NiuniuIF",
    "Baccarat5T2IF",
    "RacingCar",
    "NewBlackJack",
    "SixShooter",
    "Goldracecourse3D",
    "PaiGow",
    "DragonKingI",
    "FishMachine",
    "DragonFish",
    "DragonTigerGT",
    "DeucesWildPG",
    "ShotDragonPG",
    "BlackJackPG",
    "GoldenSharkPG",
    "KingsQueenPG",
    "DragonTigerPG",
    "LittleMarryFIVA",
    "ForestDance2D",
    "CaribbeanStudPoker"]
# 未完成的gameType清單
passNotCompleterYetSlot = ["DoubleBlessings",
    "GoldMeowSushiLegend",
    "PharaohResortHotel",
    "GoldAynu",
    "MysticWitch",
    "ThewizardofOZ",
    "AtochaTreasure",
    "TrialByViking",
    "ThreeKingdoms",
    "TreasureIsland",
    "EPICAPE",
    "KingKongHoistBaby",
    "GoldMusaI",
    "DragonBlackGold",
    "Kimba",
    "TaiWangSiShen"
    ] 
# 機台Slot的gameType清單
slotMachine = ["Chaoji8",
    "Chaoji8EX",
    "Chaoji888BT",
    "FaFaFa",
    "FaFaFaEX",
    "LongLongLong",
    "LongLongLongBT",
    "LongLongLongEX"]
# BNG多福介面的gameType清單
slotBNG = ["DuoFuDuoCai5TreasuresBNG",
    "DuoFuDuoCai88FortuneBNG",
    "DuoFuDuoCaiDancingDrumBNG",
    "DuoFuDuoCaiDiamondEternityBNG",
    "DuoFuDuoCaiFlowerOfRichesBNG"]
# marvel系列(開場有動畫需跳過)的gameType清單
slotMarvelClick = ["MarvelClassic",

    "MarvelClassicEX"]
# debug用，直接執行指定gameType，不使用時填[""]
directRunDebugGametype = [""]
# debug用，從指定遊戲開始往下跑，使用時填"gameType"，不使用時填None
directRunFromGameType = None

class UrlInfo:
    def UrlConvertToGameTypesList(self):
        # 建立一個 Request 物件， 附加Request Headers 的資訊
        request=req.Request(self, headers={
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36"
        })
        with req.urlopen(request) as response:
            data=response.read().decode("utf-8")
        root=bs4.BeautifulSoup(data, "html.parser") #讓BeautifulSoup協助解析HTML格式文件
        game_types=root.find_all('a')
        game_types_list = []
        for s in game_types:
            if  "/" in s.text: #判斷字串是否含"/"
                if  "Lobby" not in s.text: #判斷字串是否不含"Lobby"
                    s1=s.text[:-1] #刪除字串中的最後一個字"/"
                    game_types_list.append(s1)
        return game_types_list
    def PrintGameTypesList(self):
        game_types_list = UrlInfo.UrlConvertToGameTypesList(self)
        for s in game_types_list:
            print(s)
        count_game_number = len(game_types_list)
        print('總數量：%d'%count_game_number)

## 開啟瀏覽器
def OpenChrome():
    d = DesiredCapabilities.CHROME                      # enable browser logging(不懂照抄)
    d['goog:loggingPrefs'] = {'browser':'ALL'}          # 'browser'才抓得到console全部 ,'performance':'SEVERE','driver':'SEVERE'
    driver = webdriver.Chrome(desired_capabilities=d)
    driver.implicitly_wait(10)                          # (不懂照抄)
    driver.set_window_size(960,1080)                    # 視窗大小
    driver.set_window_position(0,0)                     # 視窗位置
    return driver
## 主測試流程
def MainTest(*args): 
    mainTestTimeStart = time.time() #紀錄開始時間
    # 抓畫布大小
    canvas = driver.find_element_by_xpath("/html/body/div/canvas") 
    maxPositionX = canvas.size['width']
    maxPositionY = canvas.size['height']
    # 點擊相對位置
    def clickPosition(scaleX,scaleY):
        positionX = int(maxPositionX * scaleX)
        positionY = int(maxPositionY * scaleY)
        ActionChains(driver).move_to_element_with_offset(canvas,positionX,positionY).click().perform()
    ## 執行旋轉動作
    # 1線機台點擊位置
    if nowGameType in slotMachine:
        clickPosition(0.158,0.785)                  #按下auto
        clickPosition(0.777,0.456)                  #按下∞
        clickPosition(0.669,0.673)                  #按下X3
        clickPosition(0.662,0.819)                  #按下確定
    # marval遊戲跳過開頭動畫 + 一般uiType=0點擊位置
    elif nowGameType in slotMarvelClick:
        clickPosition(0.1,0.1)
        time.sleep(0.2)
        clickPosition(0.1,0.1)
        time.sleep(3)
        clickPosition(0.921,0.281)                  #按下auto
        clickPosition(0.773,0.329)                  #按下∞
        clickPosition(0.673,0.550)                  #按下X3
        clickPosition(0.648,0.690)                  #按下確定
    # 一般uiType=0點擊位置
    else:
        clickPosition(0.921,0.281)                  #按下auto
        clickPosition(0.773,0.329)                  #按下∞
        clickPosition(0.673,0.550)                  #按下X3
        clickPosition(0.648,0.690)                  #按下確定
    ## 判斷直到贏錢時，再按一次旋轉按鈕來停下遊戲
    spinTimes = 0
    gameWin = False
    while gameWin == False:
        consoleResults = driver.get_log('browser')
        for result in consoleResults:
            if "MoneyWin" in result['message']:
                spinTimes += 1
                if "MoneyWin: 0" not in result['message']:
                    gameWin = True
                    if selectFuntion == 4:
                        return
    ## 判斷UI點擊旋轉按鈕位置停下
                    if nowGameType in slotMachine:
                        clickPosition(0.662,0.819)  #旋轉按鈕(uiType=0)
                        time.sleep(0.2)
                        clickPosition(0.662,0.819)  #旋轉按鈕(uiType=0)
                        time.sleep(0.2)
                    else:
                        clickPosition(0.926,0.482)  #旋轉按鈕(uiType=0)
                        time.sleep(0.2)
                        clickPosition(0.926,0.482)  #旋轉按鈕(uiType=0)
                        time.sleep(0.2)
                    break
    ## 持續點擊賠率表並判斷是否已停止中獎表演
    isGameStop = False
    while isGameStop == False:
        clickPosition(0.952,0.882)                  #選單按鈕(uiType=0)
        consoleResults = driver.get_log('browser')
        for result in consoleResults:
            if "OnOpenSetting" in result['message']:
                isGameStop = True
                break
            if "MoneyWin" in result['message']:   #如果還是沒停下(接收到"NormalWin")，則繼續按旋轉鍵
                clickPosition(0.926,0.512)          #旋轉按鈕(uiType=0)
    clickPosition(0.550,0.893)                      #賠率表(uiType=0)
    ## 判斷賠率表是否開啟，賠率表往下滾動
    isOpenPaytable = False
    while isOpenPaytable == False:
        consoleResults = driver.get_log('browser')
        for result in consoleResults:
            if "onOdds" in result['message']:
                isOpenPaytable = True
                # 嘗試打開iframe，若失敗就再往底下一層iframe開(EX:TaiWangSiShen)
                try:
                    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[2]/iframe"))
                except:
                    driver.switch_to.frame(driver.find_element_by_xpath("/html/body/div/div[3]/iframe"))
                paytablePageXpath = driver.find_element_by_xpath("/html/body")
                paytablePageXpath.click()
                keyPagedownTimes = 0
                while keyPagedownTimes < 15:
                    ActionChains(driver).send_keys(Keys.PAGE_DOWN).perform()
                    time.sleep(0.1)
                    keyPagedownTimes += 1
                driver.switch_to.parent_frame()
                break

    ## 進入遊戲紀錄流程
    # 遊戲紀錄按鈕(uiType=0)
    clickPosition(0.786,0.887)                      
    time.sleep(1)
    # 判斷遊戲紀錄是否開啟，並擷取其console網址另開分頁(※另開分頁才能抓到console印出的錯誤，例如:缺圖)
    consoleResults = driver.get_log('browser')
    for result in consoleResults:
        if "onHistorical" in result['message']:
            recordSplit = result['message'].split('"')
            recordUrl = recordSplit[1].lstrip('onHistorical: ')
            jsOpenRecordUrl = "window.open('" + recordUrl +"')"
            driver.execute_script(jsOpenRecordUrl)
            #get the window handle after a new window has opened
            windowAfter = driver.window_handles[1]
            #switch on to new child window
            driver.switch_to.window(windowAfter)

    # 打開最後一筆詳細紀錄
    recordDetail = driver.find_element_by_xpath("/html/body/div[2]/main/div[2]/table/tbody/tr/td[10]/button/i") # tr/td[9]沒有效投注前
    ActionChains(driver).move_to_element_with_offset(recordDetail,1,1).click().perform()
    time.sleep(2)
    consoleResults = driver.get_log('browser')
    
    # 若打開詳細紀錄時有SEVERE錯誤(EX:紀錄缺圖)，則會印出錯誤
    for result in consoleResults:
        if "SEVERE" == result['level'] and errorCheck(result['message'],nowGameType):
            print(nowGameType," **遊戲紀錄有錯！！**")
    # 關閉遊戲紀錄分頁
    driver.close()

    # 將主控切回原始分頁 driver.switch_to_default_content
    windowAfter = driver.window_handles[0]
    driver.switch_to.window(windowAfter)
    time.sleep(2)

    # 紀錄結束時間並印出
    mainTesttimeEnd = time.time() 
    print(nowGameType + " 第%d盤中獎"%spinTimes + " 耗時：" + str(round(mainTesttimeEnd - mainTestTimeStart,2)))
    
## 過濾console前兩個資訊(網址與js)
def FilterConsole(self):
    self = " ".join(self.split()[2:])
    return self

## 排除已知錯誤，判斷是否該印出訊息與跳出遊戲
def errorCheck(msg,nowGameType):
    errorMsgs=['favicon','Button_Home.png','ConfigText = null','WebIcon.jpg','interact with the document first.','沒找到對應path','Invalid Jackpot Panel','Uncaught (in promise)','找不到 Confirm控制按鈕']
    unknowMsg = True
    for errorMsg in errorMsgs:
        if errorMsg in msg:
            unknowMsg = False
    if unknowMsg == True and '404' in msg:
        print(nowGameType,FilterConsole(msg))
        return True
    elif unknowMsg == True:
        print(nowGameType,FilterConsole(msg))
        return False
    else:
        assert unknowMsg == False , "Loading判斷console有誤"

## 開啟遊戲網址
def OpenUrl(driver,nowGameType,directoryUrl,account):
    url = directoryUrl + nowGameType + account
    driver.get(url)

## 測試Loading
def LoadingTest(driver,nowGameType):
    gameLoadComplete = False
    timeStart = time.time() #紀錄Loading開始時間
    timer = 0
    # 迴圈直到console出現GameLoadComplete 或 Loading超過30秒為止
    while gameLoadComplete == False and timer <=30:
        timer = time.time() - timeStart 
        time.sleep(1) #給延遲get_log才不會讀到上一款遊戲
        consoleResults = driver.get_log('browser')
        for result in consoleResults:
            if "SEVERE" == result['level'] and errorCheck(result['message'],nowGameType):
                print(nowGameType," **未完成Loading！！**")
                return 
            if 'GameLoadComplete' in result['message']:
                gameLoadComplete = True
    if gameLoadComplete == False:
        print(nowGameType + " 讀取超過30秒，最後資訊：" + FilterConsole(result['message']))
        return  

##---主流程(Main)---##
##debug中
#directoryUrl="http://bundle.bdlserver.com/InGame/AllGameResTest/"
directoryUrl="http://bundle.bdlserver.com/QATest/AllGame_Dev/"
selectFuntion = 2

# directoryUrl = input("輸入資料夾網址：")
# selectFuntion = int(input("\n1.資料夾總遊戲列\n2.資料夾全遊戲運行\n3.只跑Loading\n4.xxx\n選擇想要的方法：\n"))
print("-------------------------------------------")
accounts = ["/?gameMode=1&language=en&debug=true&mute=true","/?gameMode=1&language=tw&debug=true&mute=true","/?gameMode=1&language=kr&debug=true&mute=true","/?gameMode=1&language=th&debug=true&mute=true","/?gameMode=1&language=vn&debug=true&mute=true","/?gameMode=1&language=es&debug=true&mute=true","/?gameMode=1&language=cn&debug=true&mute=true"]
debugMode = False

## 選擇項目
# 1.資料夾總遊戲列
if selectFuntion == 1:
    UrlInfo.PrintGameTypesList(directoryUrl)
# 2.資料夾全遊戲運行
elif selectFuntion == 2: 
    for account in accounts:
        print(account)
        totalTimeStart = time.time()
        gameTypes = UrlInfo.UrlConvertToGameTypesList(directoryUrl)
        driver = OpenChrome()

        # directRunDebugGame
        for nowGameType in gameTypes:
            if nowGameType in directRunDebugGametype:
                debugMode = True
                OpenUrl(driver,nowGameType,directoryUrl,account)
                LoadingTest(driver,nowGameType)
                MainTest(driver,nowGameType,directoryUrl,passNotSlot,passNotCompleterYetSlot,slotMachine,slotBNG,slotMarvelClick,directRunDebugGametype,directRunFromGameType,selectFuntion)
        if debugMode == True:
            #driver.close()
            sys.exit()
        
        # directRunFromGameType
        stopPass = False
        if directRunFromGameType is not None:
            for nowGameType in gameTypes:
                if stopPass == False and nowGameType == directRunFromGameType:
                    stopPass = True
                elif stopPass == True and nowGameType in passNotSlot:
                    consoleMsg = nowGameType + " 不是Slot,故跳過"
                    print(consoleMsg)
                    continue
                elif stopPass == True and nowGameType in slotBNG:
                    consoleMsg = nowGameType + " BNG尚未處理,故跳過"
                    print(consoleMsg)
                    continue            
                elif stopPass == True and nowGameType in passNotCompleterYetSlot:
                    consoleMsg = nowGameType + " 遊戲尚未完成,故跳過"
                    print(consoleMsg)
                    continue     
                elif stopPass == True:
                    OpenUrl(driver,nowGameType,directoryUrl,account)
                    LoadingTest(driver,nowGameType)
                    MainTest(driver,nowGameType,directoryUrl,passNotSlot,passNotCompleterYetSlot,slotMachine,slotBNG,slotMarvelClick,directRunDebugGametype,directRunFromGameType,selectFuntion)
                else:
                    assert stopPass == False, "directRunFromGameType判斷有誤"

        # 過濾跳尚無法自動化的遊戲
        for nowGameType in gameTypes:
            if nowGameType in passNotSlot:
                consoleMsg = nowGameType + " 不是Slot,故跳過"
                print(consoleMsg)
                continue
            elif nowGameType in slotBNG:
                consoleMsg = nowGameType + " BNG尚未處理,故跳過"
                print(consoleMsg)
                continue            
            elif nowGameType in passNotCompleterYetSlot:
                consoleMsg = nowGameType + " 遊戲尚未完成,故跳過"
                print(consoleMsg)
                continue     
            else:
                OpenUrl(driver,nowGameType,directoryUrl,account)
                LoadingTest(driver,nowGameType)
                MainTest(driver,nowGameType,directoryUrl,passNotSlot,passNotCompleterYetSlot,slotMachine,slotBNG,slotMarvelClick,directRunDebugGametype,directRunFromGameType,selectFuntion)
        totalTimeEnd = time.time()
        totalRunTime = totalTimeEnd - totalTimeStart
        print("總耗時:" + str(round(totalRunTime,2)) + "秒")
        driver.close()
# 3.只測Loading
elif selectFuntion == 3: 
    for account in accounts:
        print(account)
        totalTimeStart = time.time()
        gameTypes = UrlInfo.UrlConvertToGameTypesList(directoryUrl)
        driver = OpenChrome()
        for nowGameType in gameTypes:
            if nowGameType in directRunDebugGametype:
                OpenUrl(driver,nowGameType,directoryUrl,account)
                LoadingTest(driver,nowGameType)
        stopPass = 0
        for nowGameType in gameTypes:
            if directRunFromGameType is not None and stopPass == 0:
                if nowGameType == directRunFromGameType:
                    stopPass += 1
            elif nowGameType in passNotCompleterYetSlot:
                consoleMsg = nowGameType + " 遊戲尚未完成,故跳過"
                print(consoleMsg)
                continue     
            else:
                OpenUrl(driver,nowGameType,directoryUrl,account)
                LoadingTest(driver,nowGameType)
        totalTimeEnd = time.time()
        totalRunTime = totalTimeEnd - totalTimeStart
        print("總耗時:" + str(round(totalRunTime,2)) + "秒")
        print("-------------------------------------------")
        driver.close()
# 4.跑100帳號gameMode=1直到中獎
elif selectFuntion == 4: 
    account = "/?gameMode=1&debug=true"
    n=0
    driver = OpenChrome()  
    while n < 100:
        gameTypes = UrlInfo.UrlConvertToGameTypesList(directoryUrl)              
        for nowGameType in gameTypes:
            if nowGameType in directRunDebugGametype:
                OpenUrl(driver,nowGameType,directoryUrl,account)
                LoadingTest(driver,nowGameType)
                MainTest(driver,nowGameType,directoryUrl,passNotSlot,passNotCompleterYetSlot,slotMachine,slotBNG,slotMarvelClick,directRunDebugGametype,directRunFromGameType,selectFuntion)
        n += 1
    sys.exit()
# 輸入錯誤
else: 
    print("輸入錯誤")
 





