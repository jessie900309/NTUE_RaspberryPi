# NTUE_RaspberryPiPractice

###### tags: `NTUE_SchoolHomework` `GitHub`

#### 國立台北教育大學 110學年度 嵌入式系統 作業

* /2022pythonPractice
    * homework0331
        * 題目: 使⽤set型別完成下列問題:
            本班期末考試
            數學及格的有: Tom, John, Mary, Jimmy, Sunny, Amy，
            英⽂及格的有: John, Mary, Tony, Bob, Pony, Tom, Alice，
            分別印出數學及格但英⽂不及格的名單、數學不及格但英⽂及格的名單、兩科都及格的名單、最後印出全班總共有幾個同學。
        * 題目: 使⽤dict，list型別完成下列問題:
            Tom作業成績為 80, 100, 90, 95，John作業成績為 100, 93, 75, 80
            請以dict型別存放兩個同學的資料key:名字，value:分數列表(list)分別算出兩位同學的平均分數並且印出。
    * homework0407
        * 題目: 撰寫一為多選題測驗打分數的程式
            假設總共有8個生與10個題目,學生的答案儲存於一個二维串列裡。
            每一學生針對各問題的答案,如以下串列所示。學生針對各問題的答案:
            學生0:ABACCDEEAD 學生1:DBABCAEEAD
            學生2:EDDACBEEAD 學生3:CBAEDCEEAD
            學生4:ABDCCDEEAD 學生5:BBECCDEEAD
            學生6:BBACCDEEAD 學生7:EBECCDEEAD
            解答:DBDCCDAEAD，撰寫的程式要對測驗評分,並顯示果。其將各生的答與答正確的題數,最後顯示結果。

* /20220421
    * 實驗一 3個LED控制
        分別給于編號 LED1,LED2,LED3，執行:
        (1) LED1:亮(ON)1分鐘;LED2&LED3暗(OFF)。
        (2) LED1:OFF；LDE2:閃爍5次，間隔1秒，當LED2 ON 時，Buzzer發出聲音；LED3:OFF。
        (3) LED1 & LED2:OFF；LED3:ON 1分鐘。
        (4) LED1:OFF；LDE2:閃爍3次，間隔1秒，當LED2 ON 時，Buzzer發出聲音；LED3:OFF。
        repeat (1)到(4)。

* /homework0428
    * homework0428_repo2
        * 實驗二 Key,7-segment, and Ultrasonic
            (1) 7-segment顯示"0"，Terminal顯示ultrasonic偵測到障礙物的距離。
            (2) Key pressed， 7-segment顯示"1"(0+1)， Terminal顯示ultrasonic偵測到障礙物的距離。
            repeat(1)到(2)， 7-segment顯示累加的效果: 0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,0,1,2,……。
    * homework0428_repo2_2
        * 實驗二(2)
            (1) 7-Segment由Key來控制。
            (2) Ultrasonic不再被Key控制，而是獨立在主程式運作，每隔3秒顯示障礙物的距離。

* /homework0505
    * 實驗三 LCD and Ultrasonic
        (1) 即時將ultrasonic偵測到的障礙物距離顯示在LCD上，包含cm 和inch。
        (2) 當障礙物距離小於5cm播放音樂。
        (3) ctrl+c 結束程式。
<!-- 
* /homework0512
    * 實驗四 (mcp3008, Photocell, and Joystick)
        (1) 沒有操作時，LCD顯示光敏電阻和搖桿的數值，顯示的格式自己定義。
        (2) 當操作時，顯示當下的數值，同時導引改變的趨勢(例如: UP, DOWN, LEFT, RIGHT, PRESSED, Light, Dark)。 -->

* /homework0519
    * 實驗五 DHT22 & Web
        (1) 完成DHT22溫溼度量測，並上傳華氏溫度，攝氏溫度，濕度，量測時間到MySQL(MariaDB)資料庫，並能夠顯示這些資料在瀏覽器上。

* /homework0526
    * 實驗六 RFID
        (1) 在編號8寫入英文名字。
        (2) 讀出名字和卡號進行簽到，連同刷卡時間，存放在mySQL資料庫。
