age=20
year=3
grade=4
if age>=18:
    print("您已成年")
    if age<30:
        print("您的年龄已达标")
        if year>2:
            print("恭喜你，年龄和入职时间都达标。可以领取礼物")
        elif grade>3:
            print("感谢您，年龄和等级都达标。可以领取礼物")
        else:
            print("不好意思虽然您的年龄达标，但是级别和入职时间不达标")
    else:
        print("您年龄太大，无法领取礼物")
else:
    print("您未成年，无法领取礼物")