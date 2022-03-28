import requests ,os ,time ,ctypes #line:1
def clear ():#line:3
    if os .name !='nt':#line:4
        os .system ('clear')#line:5
    else :#line:6
        os .system ('cls')#line:7
def ititle (O0O0O0O00O0O0OO0O ,O000O000000O0OOO0 ,OOO0OOOO00000OO0O ):#line:9
    try :#line:10
        ctypes .windll .kernel32 .SetConsoleTitleW ('Sent [{0}] | Failed [{1}] | Rate Limited [{2}]'.format (O0O0O0O00O0O0OO0O ,O000O000000O0OOO0 ,OOO0OOOO00000OO0O ))#line:11
    except :#line:12
        pass #line:13
def whsend (O00000000OOO0O0O0 :str ,OOO00OOO0O000O0O0 :str ,OO000OOOOO0O000O0 :str ,O0OO0OOOO0OOO0000 :bool ):#line:15
    clear ()#line:16
    if O0OO0OOOO0OOO0000 :#line:17
        OOOOOOOOO00O0000O =0 #line:18
        OOO00OOO000OOOOOO =0 #line:19
        OO0O00OOOO0OO0000 =0 #line:20
        while OOO00OOO000OOOOOO <20 :#line:21
            OOOOOO0OO0000OO0O =requests .post (O00000000OOO0O0O0 ,{"content":OO000OOOOO0O000O0 ,"username":OOO00OOO0O000O0O0 })#line:22
            try :#line:23
                if OOOOOO0OO0000OO0O .json ()["retry_after"]:#line:24
                    print (f'Getting rate limited, sleeping for {OOOOOO0OO0000OO0O.json()["retry_after"] / 1000}s.')#line:25
                    OO0O00OOOO0OO0000 +=1 #line:26
                    ititle (OOOOOOOOO00O0000O ,OOO00OOO000OOOOOO ,OO0O00OOOO0OO0000 )#line:27
                    time .sleep (OOOOOO0OO0000OO0O .json ()["retry_after"]/1000 )#line:28
            except :#line:29
                if OOOOOO0OO0000OO0O .status_code ==204 :#line:30
                    OOOOOOOOO00O0000O +=1 #line:31
                    ititle (OOOOOOOOO00O0000O ,OOO00OOO000OOOOOO ,OO0O00OOOO0OO0000 )#line:32
                    print (f'Successful | {OOOOOOOOO00O0000O} times.')#line:33
                else :#line:34
                    OOO00OOO000OOOOOO +=1 #line:35
                    ititle (OOOOOOOOO00O0000O ,OOO00OOO000OOOOOO ,OO0O00OOOO0OO0000 )#line:36
                    print (f'Failed | {OOO00OOO000OOOOOO} times.')#line:37
        clear ()#line:38
        exit (f'The webhook most likely does not exist anymore.\nStatistics:\nSuccessful posts: {OOOOOOOOO00O0000O}\nFailed posts: {OOO00OOO000OOOOOO}\nRate Limits: {OO0O00OOOO0OO0000}')#line:39
    else :#line:40
        OOOOOO0OO0000OO0O =requests .post (O00000000OOO0O0O0 ,{"content":OO000OOOOO0O000O0 ,"username":OOO00OOO0O000O0O0 })#line:41
        if OOOOOO0OO0000OO0O .status_code ==204 :#line:42
            print ('Successful.')#line:43
        else :#line:44
            print ('Failed.')#line:45
url =input ('Webhook URL (Hierzo moet je je webhook invullen die je wilt spammen): ')#line:48
if not url :#line:49
    print ('Dit is geen webhook!')#line:50
    exit (-1 )#line:51
un =input ('Wat moet de naam worden? (Discord naam gebruiken? Laat dan leeg.): ')#line:52
if not un :#line:53
    un ='appendable'#line:54
c =input ('Wat wil je sturen? ')#line:55
if not c :#line:56
    print ('O nee, je moet echts iets sturen.')#line:57
    exit (-1 )#line:58
sp =input ('Spammen? :) [y|n]: ')#line:59
if not sp :#line:60
    whsend (url ,un ,c ,True )#line:61
if sp .lower ()=='y':#line:62
    whsend (url ,un ,c ,True )#line:63
else :#line:64
    whsend (url ,un ,c ,False )
